"""
Audio Backend Plugin Architecture for Siege6 MCP
Provides extensible spatial audio processing with multiple backend support
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class AudioBackendType(Enum):
    """Available audio backend types"""
    OPENAL = "openal"
    WINDOWS_SPATIAL = "windows_spatial"
    NONE = "none"


@dataclass
class SpatialPosition:
    """3D position in space"""
    x: float
    y: float
    z: float

    def to_dict(self) -> Dict:
        return {"x": self.x, "y": self.y, "z": self.z}


@dataclass
class AudioMetadata:
    """Enhanced audio metadata for operators and sounds"""
    name: str
    description: str
    frequency_range: Tuple[float, float]  # Hz (low, high)
    volume_db: float  # Base volume in decibels
    spatial_falloff: float  # Distance attenuation factor
    reverb_amount: float  # 0.0 to 1.0
    occlusion_factor: float  # Material penetration (0.0 = blocked, 1.0 = passes through)
    directional: bool  # Whether sound is directional
    position: Optional[SpatialPosition] = None

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "description": self.description,
            "frequency_range": {"low": self.frequency_range[0], "high": self.frequency_range[1]},
            "volume_db": self.volume_db,
            "spatial_falloff": self.spatial_falloff,
            "reverb_amount": self.reverb_amount,
            "occlusion_factor": self.occlusion_factor,
            "directional": self.directional,
            "position": self.position.to_dict() if self.position else None
        }


@dataclass
class AudioProcessingResult:
    """Result of audio processing operation"""
    success: bool
    message: str
    processed_audio: Optional[Dict] = None
    backend_info: Optional[Dict] = None


class AudioBackend(ABC):
    """Abstract base class for audio backend plugins"""

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.initialized = False
        self.backend_type = AudioBackendType.NONE

    @abstractmethod
    def initialize(self) -> bool:
        """Initialize the audio backend. Returns True on success."""
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Cleanup and shutdown the audio backend"""
        pass

    @abstractmethod
    def process_spatial_audio(
        self,
        audio_metadata: AudioMetadata,
        listener_position: SpatialPosition,
        listener_orientation: Tuple[float, float, float]
    ) -> AudioProcessingResult:
        """
        Process audio with spatial positioning

        Args:
            audio_metadata: Enhanced audio metadata
            listener_position: Position of the listener (player)
            listener_orientation: Direction listener is facing (yaw, pitch, roll)

        Returns:
            AudioProcessingResult with processing details
        """
        pass

    @abstractmethod
    def get_capabilities(self) -> Dict[str, bool]:
        """Return dictionary of backend capabilities"""
        pass

    @abstractmethod
    def get_backend_info(self) -> Dict[str, str]:
        """Return information about the backend"""
        pass

    def is_available(self) -> bool:
        """Check if this backend is available on the current system"""
        try:
            return self.initialize()
        except Exception:
            return False


class NullAudioBackend(AudioBackend):
    """Fallback backend that provides metadata without actual audio processing"""

    def __init__(self, config: Optional[Dict] = None):
        super().__init__(config)
        self.backend_type = AudioBackendType.NONE

    def initialize(self) -> bool:
        """Always succeeds - no initialization needed"""
        self.initialized = True
        return True

    def shutdown(self) -> None:
        """No cleanup needed"""
        self.initialized = False

    def process_spatial_audio(
        self,
        audio_metadata: AudioMetadata,
        listener_position: SpatialPosition,
        listener_orientation: Tuple[float, float, float]
    ) -> AudioProcessingResult:
        """Provide metadata analysis without actual processing"""

        # Calculate basic distance
        if audio_metadata.position:
            dx = audio_metadata.position.x - listener_position.x
            dy = audio_metadata.position.y - listener_position.y
            dz = audio_metadata.position.z - listener_position.z
            distance = (dx**2 + dy**2 + dz**2) ** 0.5

            # Basic volume attenuation
            attenuated_volume = audio_metadata.volume_db - (distance * audio_metadata.spatial_falloff)
        else:
            distance = 0.0
            attenuated_volume = audio_metadata.volume_db

        result = {
            "metadata": audio_metadata.to_dict(),
            "distance": distance,
            "attenuated_volume_db": attenuated_volume,
            "listener_position": listener_position.to_dict(),
            "note": "Using NullAudioBackend - metadata only, no actual audio processing"
        }

        return AudioProcessingResult(
            success=True,
            message="Audio metadata analyzed (no backend active)",
            processed_audio=result,
            backend_info=self.get_backend_info()
        )

    def get_capabilities(self) -> Dict[str, bool]:
        """Null backend has no real capabilities"""
        return {
            "spatial_positioning": False,
            "hrtf_processing": False,
            "reverb": False,
            "occlusion": False,
            "real_time_processing": False
        }

    def get_backend_info(self) -> Dict[str, str]:
        """Return backend information"""
        return {
            "name": "Null Audio Backend",
            "type": "none",
            "version": "1.0.0",
            "description": "Fallback backend providing metadata analysis without audio processing"
        }


class AudioBackendManager:
    """Manages audio backend plugins and provides unified interface"""

    def __init__(self):
        self.backends: Dict[AudioBackendType, AudioBackend] = {}
        self.active_backend: AudioBackend = NullAudioBackend()
        self.active_backend.initialize()

    def register_backend(self, backend: AudioBackend) -> bool:
        """Register an audio backend plugin"""
        try:
            self.backends[backend.backend_type] = backend
            return True
        except Exception as e:
            print(f"Failed to register backend: {e}")
            return False

    def set_active_backend(self, backend_type: AudioBackendType) -> bool:
        """Switch to a different audio backend"""
        if backend_type == AudioBackendType.NONE:
            if self.active_backend:
                self.active_backend.shutdown()
            self.active_backend = NullAudioBackend()
            return self.active_backend.initialize()

        if backend_type not in self.backends:
            return False

        backend = self.backends[backend_type]

        if not backend.is_available():
            return False

        # Shutdown current backend
        if self.active_backend:
            self.active_backend.shutdown()

        # Initialize new backend
        if backend.initialize():
            self.active_backend = backend
            return True

        # Fallback to null backend if initialization fails
        self.active_backend = NullAudioBackend()
        self.active_backend.initialize()
        return False

    def get_active_backend(self) -> AudioBackend:
        """Get the currently active backend"""
        return self.active_backend

    def list_available_backends(self) -> List[Dict[str, str]]:
        """List all available backends on this system"""
        available = []

        # Always include null backend
        null_backend = NullAudioBackend()
        available.append(null_backend.get_backend_info())

        # Check registered backends
        for backend_type, backend in self.backends.items():
            if backend.is_available():
                available.append(backend.get_backend_info())

        return available

    def get_backend_capabilities(self) -> Dict[str, bool]:
        """Get capabilities of active backend"""
        return self.active_backend.get_capabilities()


# Global backend manager instance
_backend_manager: Optional[AudioBackendManager] = None


def get_backend_manager() -> AudioBackendManager:
    """Get or create the global backend manager instance"""
    global _backend_manager
    if _backend_manager is None:
        _backend_manager = AudioBackendManager()
    return _backend_manager
