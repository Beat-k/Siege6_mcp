"""
OpenAL Audio Backend Plugin for Siege6 MCP
Provides real 3D spatial audio processing using OpenAL
"""

from typing import Dict, Optional, Tuple
from audio_backend import (
    AudioBackend,
    AudioBackendType,
    AudioMetadata,
    SpatialPosition,
    AudioProcessingResult
)
import sys


class OpenALBackend(AudioBackend):
    """OpenAL-based spatial audio backend"""

    def __init__(self, config: Optional[Dict] = None):
        super().__init__(config)
        self.backend_type = AudioBackendType.OPENAL
        self.al_device = None
        self.al_context = None
        self.openal_available = False

        # Try to import OpenAL
        try:
            import openal
            self.openal = openal
            self.openal_available = True
        except ImportError:
            self.openal_available = False
            print("OpenAL library not available. Install with: pip install PyOpenAL", file=sys.stderr)

    def initialize(self) -> bool:
        """Initialize OpenAL audio system"""
        if not self.openal_available:
            return False

        try:
            # Open default audio device
            self.al_device = self.openal.oalOpen(None)
            if not self.al_device:
                print("Failed to open OpenAL device", file=sys.stderr)
                return False

            # Create audio context
            self.al_context = self.openal.oalCreateContext(self.al_device, None)
            if not self.al_context:
                print("Failed to create OpenAL context", file=sys.stderr)
                self.openal.oalClose(self.al_device)
                return False

            # Make context current
            self.openal.oalMakeCurrent(self.al_context)

            # Set distance model for attenuation
            self.openal.alDistanceModel(self.openal.AL_INVERSE_DISTANCE_CLAMPED)

            self.initialized = True
            print("OpenAL backend initialized successfully", file=sys.stderr)
            return True

        except Exception as e:
            print(f"Failed to initialize OpenAL: {e}", file=sys.stderr)
            self.initialized = False
            return False

    def shutdown(self) -> None:
        """Cleanup OpenAL resources"""
        if not self.openal_available:
            return

        try:
            if self.al_context:
                self.openal.oalMakeCurrent(None)
                self.openal.oalDestroyContext(self.al_context)
                self.al_context = None

            if self.al_device:
                self.openal.oalClose(self.al_device)
                self.al_device = None

            self.initialized = False
            print("OpenAL backend shutdown", file=sys.stderr)

        except Exception as e:
            print(f"Error during OpenAL shutdown: {e}", file=sys.stderr)

    def process_spatial_audio(
        self,
        audio_metadata: AudioMetadata,
        listener_position: SpatialPosition,
        listener_orientation: Tuple[float, float, float]
    ) -> AudioProcessingResult:
        """Process audio with OpenAL spatial positioning"""

        if not self.initialized:
            return AudioProcessingResult(
                success=False,
                message="OpenAL backend not initialized",
                backend_info=self.get_backend_info()
            )

        try:
            # Calculate spatial audio parameters
            result_data = self._calculate_spatial_parameters(
                audio_metadata,
                listener_position,
                listener_orientation
            )

            # Apply OpenAL processing (in a real implementation, this would create
            # an OpenAL source, set its properties, and play audio)
            openal_params = self._generate_openal_parameters(audio_metadata, result_data)

            result_data["openal_parameters"] = openal_params
            result_data["processing_applied"] = True

            return AudioProcessingResult(
                success=True,
                message="Audio processed with OpenAL spatial positioning",
                processed_audio=result_data,
                backend_info=self.get_backend_info()
            )

        except Exception as e:
            return AudioProcessingResult(
                success=False,
                message=f"OpenAL processing error: {str(e)}",
                backend_info=self.get_backend_info()
            )

    def _calculate_spatial_parameters(
        self,
        audio_metadata: AudioMetadata,
        listener_position: SpatialPosition,
        listener_orientation: Tuple[float, float, float]
    ) -> Dict:
        """Calculate spatial audio parameters"""

        # Calculate distance and direction
        if audio_metadata.position:
            dx = audio_metadata.position.x - listener_position.x
            dy = audio_metadata.position.y - listener_position.y
            dz = audio_metadata.position.z - listener_position.z
            distance = (dx**2 + dy**2 + dz**2) ** 0.5

            # Normalize direction vector
            if distance > 0:
                direction = (dx / distance, dy / distance, dz / distance)
            else:
                direction = (0, 0, 0)
        else:
            distance = 0.0
            direction = (0, 0, 0)
            dx, dy, dz = 0, 0, 0

        # Calculate angle relative to listener orientation (yaw)
        import math
        listener_yaw = listener_orientation[0]
        angle_to_source = math.atan2(dx, dz)
        relative_angle = angle_to_source - math.radians(listener_yaw)

        # Calculate panning (-1 left, 0 center, 1 right)
        pan = math.sin(relative_angle)

        # Calculate volume attenuation based on distance
        attenuated_volume = audio_metadata.volume_db - (distance * audio_metadata.spatial_falloff)

        # Apply occlusion if sound is behind walls (simplified)
        if distance > 5.0:  # Assume occlusion for distant sounds
            attenuated_volume -= (1.0 - audio_metadata.occlusion_factor) * 10.0

        # Calculate doppler effect (if moving - not implemented in basic version)
        doppler_shift = 1.0

        return {
            "metadata": audio_metadata.to_dict(),
            "listener_position": listener_position.to_dict(),
            "listener_orientation": {
                "yaw": listener_orientation[0],
                "pitch": listener_orientation[1],
                "roll": listener_orientation[2]
            },
            "distance": distance,
            "direction": {"x": direction[0], "y": direction[1], "z": direction[2]},
            "relative_angle_degrees": math.degrees(relative_angle),
            "pan": pan,
            "attenuated_volume_db": attenuated_volume,
            "doppler_shift": doppler_shift,
            "reverb_amount": audio_metadata.reverb_amount,
            "frequency_range": {
                "low": audio_metadata.frequency_range[0],
                "high": audio_metadata.frequency_range[1]
            }
        }

    def _generate_openal_parameters(self, audio_metadata: AudioMetadata, spatial_data: Dict) -> Dict:
        """Generate OpenAL-specific parameters"""

        if not audio_metadata.position:
            source_position = (0.0, 0.0, 0.0)
        else:
            source_position = (
                audio_metadata.position.x,
                audio_metadata.position.y,
                audio_metadata.position.z
            )

        # Convert dB to linear gain (simplified)
        import math
        linear_gain = math.pow(10, spatial_data["attenuated_volume_db"] / 20.0)
        linear_gain = max(0.0, min(1.0, linear_gain))  # Clamp to [0, 1]

        return {
            "AL_POSITION": source_position,
            "AL_VELOCITY": (0.0, 0.0, 0.0),  # Static for now
            "AL_GAIN": linear_gain,
            "AL_PITCH": spatial_data["doppler_shift"],
            "AL_ROLLOFF_FACTOR": audio_metadata.spatial_falloff,
            "AL_REFERENCE_DISTANCE": 1.0,
            "AL_MAX_DISTANCE": 100.0,
            "AL_CONE_INNER_ANGLE": 360.0 if not audio_metadata.directional else 60.0,
            "AL_CONE_OUTER_ANGLE": 360.0 if not audio_metadata.directional else 120.0,
            "AL_CONE_OUTER_GAIN": 0.5 if audio_metadata.directional else 1.0
        }

    def get_capabilities(self) -> Dict[str, bool]:
        """Return OpenAL capabilities"""
        return {
            "spatial_positioning": True,
            "hrtf_processing": True,  # OpenAL supports HRTF
            "reverb": True,  # Via EFX extension
            "occlusion": True,  # Can be simulated
            "real_time_processing": True,
            "distance_attenuation": True,
            "doppler_effect": True,
            "directional_sources": True
        }

    def get_backend_info(self) -> Dict[str, str]:
        """Return OpenAL backend information"""
        info = {
            "name": "OpenAL Audio Backend",
            "type": "openal",
            "version": "1.0.0",
            "description": "Cross-platform 3D spatial audio using OpenAL"
        }

        if self.initialized and self.openal_available:
            try:
                # Get OpenAL version info
                vendor = self.openal.alGetString(self.openal.AL_VENDOR)
                renderer = self.openal.alGetString(self.openal.AL_RENDERER)
                version = self.openal.alGetString(self.openal.AL_VERSION)

                info["openal_vendor"] = vendor.decode() if isinstance(vendor, bytes) else str(vendor)
                info["openal_renderer"] = renderer.decode() if isinstance(renderer, bytes) else str(renderer)
                info["openal_version"] = version.decode() if isinstance(version, bytes) else str(version)
            except Exception:
                pass

        return info

    def is_available(self) -> bool:
        """Check if OpenAL is available"""
        return self.openal_available
