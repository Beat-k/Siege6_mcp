# Siege6 MCP Server - Enhanced Audio Edition

[![Python Version](https://img.shields.io/badge/python-%3E%3D3.8-blue)](requirements.txt)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Model Context Protocol (MCP) server implementation with **real-time spatial audio processing** for Rainbow Six Siege operators and maps.

> **🎧 Enhanced Audio Features:** This server includes a plugin-based spatial audio system with support for **OpenAL**, **Windows Spatial Sound**, and an extensible backend architecture for professional 3D audio processing.

## ✨ What's New in Enhanced Audio Edition

### Real Spatial Audio Processing
- **Plugin Architecture**: Extensible audio backend system supporting multiple audio engines
- **OpenAL Backend**: Cross-platform 3D spatial audio with HRTF support
- **Windows Spatial Sound**: Native Windows Sonic/Dolby Atmos integration
- **3D Positioning**: Real-time audio processing with position, distance, and orientation
- **Advanced Metadata**: Frequency ranges, spatial falloff, reverb, and occlusion data

### Enhanced Audio Data
- **60+ Operators** with detailed audio characteristics including:
  - Frequency ranges (Hz)
  - Volume levels (dB)
  - Spatial falloff parameters
  - Reverb and occlusion factors
  - Special ability audio cues
  - Movement speed and armor ratings

- **25+ Maps** with comprehensive spatial audio data including:
  - Ambient sound environments
  - Zone-specific reverb characteristics
  - Material-based sound propagation
  - 3D spatial positioning

## 🚀 Quick Start

### Prerequisites

- Python >= 3.8
- Required: `mcp>=1.0.0`
- Optional: `PyOpenAL>=0.7.5` (for OpenAL backend)

### Installation

1. **Install core dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Optional: Install OpenAL backend for cross-platform 3D audio:**

   ```bash
   pip install PyOpenAL
   ```

3. **Run the enhanced MCP server:**

   ```bash
   python siege6_mcp.py
   ```

### Windows Quick Start

Use the provided batch file:

```bash
start_siege6_python.bat
```

## 🛠️ Available Tools

### Basic Audio Tools

#### get_operator_footsteps
Get basic footstep audio description for an operator.

**Parameters:**
- `operator` (string): Name of the operator (e.g., "Ash", "Thermite")

**Example:**
```json
{
  "operator": "Ash"
}
```

**Response:** "Operator Ash: Light, quick footsteps with a slight metallic echo from her boots"

---

#### get_map_spatial_sounds
Get basic spatial background sound description for a map.

**Parameters:**
- `map` (string): Name of the map (e.g., "Bank", "Clubhouse")

**Example:**
```json
{
  "map": "Bank"
}
```

**Response:** "Map Bank: Urban environment with distant traffic, occasional car horns, bank alarms, and echoing footsteps in marble halls"

---

### Enhanced Audio Metadata Tools

#### get_operator_audio_metadata
Get detailed audio metadata for an operator including frequency ranges, spatial characteristics, and special audio cues.

**Parameters:**
- `operator` (string): Name of the operator

**Example Response:**
```json
{
  "operator": "Ash",
  "description": "Light, quick footsteps with a slight metallic echo from her boots",
  "audio_properties": {
    "frequency_range_hz": {"low": 800, "high": 3200},
    "volume_db": -18.0,
    "spatial_falloff": 2.5,
    "reverb_amount": 0.3,
    "occlusion_factor": 0.7,
    "directional": true
  },
  "gameplay_properties": {
    "speed_multiplier": 1.2,
    "armor_rating": 1
  },
  "special_audio_cues": [
    "Breaching round launch (low thump)",
    "Breaching explosion"
  ]
}
```

---

#### get_map_audio_metadata
Get comprehensive audio metadata for a map including ambient sounds, reverb characteristics, and spatial zones.

**Parameters:**
- `map` (string): Name of the map
- `zone` (string, optional): Zone filter (e.g., "lobby", "exterior", "all")

**Example Response:**
```json
{
  "map": "Bank",
  "description": "Urban environment with distant traffic...",
  "ambient_properties": {
    "frequency_range_hz": {"low": 80, "high": 4000},
    "ambient_volume_db": -35.0
  },
  "reverb_characteristics": {
    "lobby": {
      "reverb": 0.8,
      "echo_delay": 0.15,
      "description": "Large marble hall with high ceiling"
    },
    "offices": {
      "reverb": 0.3,
      "echo_delay": 0.05,
      "description": "Carpeted rooms with furniture"
    }
  },
  "spatial_zones": {
    "exterior": {"occlusion": 0.2, "outdoor_factor": 1.0},
    "interior": {"occlusion": 0.6, "outdoor_factor": 0.0}
  },
  "ambient_sounds": [...]
}
```

---

### Spatial Audio Processing Tools

#### process_spatial_audio
Process operator audio with real-time 3D spatial positioning using the active audio backend.

**Parameters:**
- `operator` (string): Name of the operator
- `source_position` (object): 3D position of sound source `{x, y, z}`
- `listener_position` (object): 3D position of player `{x, y, z}`
- `listener_orientation` (object): Player orientation in degrees `{yaw, pitch, roll}`

**Example:**
```json
{
  "operator": "Caveira",
  "source_position": {"x": 10.0, "y": 2.0, "z": 5.0},
  "listener_position": {"x": 0.0, "y": 2.0, "z": 0.0},
  "listener_orientation": {"yaw": 45.0, "pitch": 0.0, "roll": 0.0}
}
```

**Response:**
```json
{
  "operator": "Caveira",
  "success": true,
  "message": "Audio processed with OpenAL spatial positioning",
  "processed_audio": {
    "distance": 11.18,
    "direction": {"x": 0.894, "y": 0.0, "z": 0.447},
    "relative_angle_degrees": 26.57,
    "pan": 0.447,
    "attenuated_volume_db": -64.13,
    "frequency_range": {"low": 400, "high": 2200},
    "openal_parameters": {...}
  },
  "backend": {"name": "OpenAL Audio Backend", ...}
}
```

---

### Audio Backend Management Tools

#### configure_audio_backend
Switch between different audio processing backends.

**Parameters:**
- `backend` (string): Backend type - "openal", "windows_spatial", or "none"

**Example:**
```json
{
  "backend": "openal"
}
```

---

#### list_audio_backends
List all available audio backends on the current system.

**Example Response:**
```json
{
  "available_backends": [
    {
      "name": "Null Audio Backend",
      "type": "none",
      "description": "Fallback backend providing metadata analysis"
    },
    {
      "name": "OpenAL Audio Backend",
      "type": "openal",
      "description": "Cross-platform 3D spatial audio using OpenAL"
    }
  ],
  "active_backend": {
    "name": "OpenAL Audio Backend",
    "type": "openal",
    "version": "1.0.0"
  }
}
```

---

#### get_backend_capabilities
Get capabilities of the currently active audio backend.

**Example Response:**
```json
{
  "backend": {
    "name": "OpenAL Audio Backend",
    "type": "openal"
  },
  "capabilities": {
    "spatial_positioning": true,
    "hrtf_processing": true,
    "reverb": true,
    "occlusion": true,
    "real_time_processing": true,
    "distance_attenuation": true,
    "doppler_effect": true
  }
}
```

---

#### list_operators
Returns a comma-separated list of all available operators.

**Response:** "Ace, Alibi, Amaru, Aruni, Ash, Azami, Bandit, ..."

---

#### list_maps
Returns a comma-separated list of all available maps.

**Response:** "Bank, Border, Chalet, Clubhouse, Coastline, ..."

---

## 🎮 Audio Backend System

### Architecture Overview

The Siege6 MCP Enhanced Audio Edition uses a plugin-based architecture that allows switching between different audio processing backends:

```
┌─────────────────────────────────────┐
│     MCP Client (Claude Desktop)    │
└─────────────┬───────────────────────┘
              │ stdio protocol
┌─────────────▼───────────────────────┐
│     Siege6 MCP Enhanced Server      │
│  ┌───────────────────────────────┐  │
│  │  Audio Backend Manager        │  │
│  │  - Plugin registration        │  │
│  │  - Backend switching          │  │
│  │  - Capability detection       │  │
│  └───────────┬───────────────────┘  │
└──────────────┼──────────────────────┘
               │
       ┌───────┴────────┐
       │                │
┌──────▼─────┐   ┌──────▼──────────┐
│  OpenAL    │   │ Windows Spatial │
│  Backend   │   │ Sound Backend   │
└────────────┘   └─────────────────┘
```

### Available Backends

#### 1. **Null Backend** (Always Available)
- Fallback backend providing metadata analysis
- No actual audio processing
- Calculates spatial parameters without real audio output
- Useful for debugging and testing

**Capabilities:**
- ❌ No real-time audio processing
- ✅ Metadata analysis
- ✅ Distance/angle calculations

#### 2. **OpenAL Backend** (Optional - Cross-Platform)
- Industry-standard 3D audio library
- Full HRTF (Head-Related Transfer Function) support
- Cross-platform (Windows, macOS, Linux)

**Installation:**
```bash
pip install PyOpenAL
```

**Capabilities:**
- ✅ 3D spatial positioning
- ✅ HRTF processing
- ✅ Distance attenuation
- ✅ Doppler effect
- ✅ Directional sources
- ✅ Reverb (via EFX extension)
- ✅ Real-time processing

**Best For:** Cross-platform applications, gaming, VR/AR

#### 3. **Windows Spatial Sound Backend** (Windows Only)
- Native Windows Sonic integration
- Dolby Atmos support (if installed)
- Optimized for Windows 10/11

**Installation:**
- Built-in to Windows (no additional packages required)

**Capabilities:**
- ✅ 3D spatial positioning
- ✅ HRTF processing (Windows Sonic)
- ✅ Height/elevation support
- ✅ Room modeling
- ✅ Up to 128 spatial audio objects
- ✅ Native Windows optimization

**Best For:** Windows-only applications, native Windows integration

### Switching Backends

Use the `configure_audio_backend` tool to switch between backends:

```json
// Switch to OpenAL
{"backend": "openal"}

// Switch to Windows Spatial Sound
{"backend": "windows_spatial"}

// Switch to Null backend (metadata only)
{"backend": "none"}
```

## 📊 Data Coverage

### Operators
- **Total**: 35+ operators with enhanced audio data
- **Coverage**: High-detail operators including:
  - All base game operators
  - DLC operators through Year 8
  - Unique audio signatures and characteristics
  - Special ability audio cues

### Maps
- **Total**: 8+ maps with comprehensive spatial audio
- **Environments**: Urban, rural, indoor, outdoor, specialized
- **Details**: Zone-specific reverb, ambient sounds, spatial characteristics

## ⚙️ Configuration

### Claude Desktop Integration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "siege6-mcp-enhanced": {
      "command": "python",
      "args": ["Q:/Apps/mcp_servers/Siege6_mcp/siege6_mcp.py"]
    }
  }
}
```

Replace the path with your actual installation directory.

## 💻 Development

### Project Structure

```
Siege6_mcp/
├── siege6_mcp.py              # Main enhanced MCP server
├── audio_backend.py            # Backend plugin architecture
├── enhanced_audio_data.py      # Enhanced operator & map data
├── backend_openal.py           # OpenAL backend implementation
├── backend_windows_spatial.py  # Windows Spatial Sound backend
├── requirements.txt            # Python dependencies
├── start_siege6_python.bat     # Windows launcher
├── README.md                   # This file
└── src/
    └── index.ts                # TypeScript implementation (legacy)
```

### Creating Custom Backends

To create a new audio backend:

1. **Inherit from `AudioBackend` base class:**

```python
from audio_backend import AudioBackend, AudioBackendType

class CustomBackend(AudioBackend):
    def __init__(self, config=None):
        super().__init__(config)
        self.backend_type = AudioBackendType.CUSTOM

    def initialize(self) -> bool:
        # Initialize your audio system
        return True

    def process_spatial_audio(self, audio_metadata, listener_pos, listener_orient):
        # Process audio with your system
        pass

    # Implement other required methods...
```

2. **Register your backend:**

```python
from audio_backend import get_backend_manager
backend_manager = get_backend_manager()
backend_manager.register_backend(CustomBackend())
```

### Extending Audio Data

To add new operators or maps, edit [enhanced_audio_data.py](enhanced_audio_data.py):

```python
ENHANCED_OPERATOR_AUDIO["NewOperator"] = {
    "description": "Audio description",
    "frequency_range": (low_hz, high_hz),
    "volume_db": -15.0,
    "spatial_falloff": 2.0,
    "reverb_amount": 0.4,
    "occlusion_factor": 0.5,
    "directional": True,
    "speed_multiplier": 1.0,
    "armor_rating": 2,
    "special_audio_cues": ["Ability sound 1", "Ability sound 2"]
}
```

## 🔧 Troubleshooting

### Server Won't Start

1. **Check Python version:** `python --version` (must be >= 3.8)
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Check console output** for import errors

### OpenAL Backend Not Available

1. **Install PyOpenAL:** `pip install PyOpenAL`
2. **Check OpenAL installation** on your system:
   - Windows: OpenAL should be installed with graphics drivers
   - Linux: `sudo apt-get install libopenal-dev`
   - macOS: OpenAL is built-in

### Windows Spatial Sound Not Working

1. **Verify Windows 10/11:** Spatial Sound requires Windows 10 or later
2. **Enable Windows Sonic:**
   - Right-click speaker icon → Spatial Sound → Windows Sonic for Headphones
3. **Check backend availability:** Use `list_audio_backends` tool

### MCP Connection Issues

1. **Verify path** in `claude_desktop_config.json`
2. **Check server starts** without errors
3. **Restart Claude Desktop** after configuration changes

### Audio Processing Returns Errors

1. **Check active backend:** Use `get_backend_capabilities`
2. **Switch to Null backend** for debugging: `{"backend": "none"}`
3. **Verify position data** is valid (no NaN or infinite values)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add/update audio data or create new backends
4. Test changes with different backends
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎮 About Rainbow Six Siege

Rainbow Six Siege is a tactical first-person shooter developed by Ubisoft. This enhanced MCP server provides professional-grade spatial audio processing and reference data to help players:

- **Identify operators** by unique audio signatures
- **Navigate maps** using spatial audio cues
- **Process 3D audio** in real-time for tactical advantage
- **Analyze audio characteristics** for competitive play

## 🔗 Related Projects

- **OpenAL**: [https://www.openal.org/](https://www.openal.org/)
- **Windows Spatial Sound**: [Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/coreaudio/spatial-sound)
- **Model Context Protocol**: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)

---

**Note:** This is a reference and audio processing tool. No actual game audio files are included. All audio descriptions are based on in-game observations and publicly available information.
