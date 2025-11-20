# Siege6 MCP Server (Python)

[![Python Version](https://img.shields.io/badge/python-%3E%3D3.8-blue)](requirements.txt)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Model Context Protocol (MCP) server implementation in Python that provides comprehensive audio reference data for Rainbow Six Siege operators and maps.

> **🎵 Sound Enhancement Note:** For optimal 4D audio integration and spatial sound processing, this server works best with [BEA Aura Console VM](https://github.com/Beat-k/BEA_Aura_Console_VM).

## 🚀 Quick Start

### Prerequisites

- Python >= 3.8
- Required packages (see `requirements.txt`)

### Installation

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the MCP server:

   ```bash
   python siege6_mcp.py
   ```

### Batch File (Windows)

For convenience, use the provided batch file:

   ```bash
   start_siege6_python.bat
   ```

This automatically activates the virtual environment and starts the server.

## ✨ Features

- **Operator Footsteps Database**: Detailed audio descriptions for all Rainbow Six Siege operators
- **Map Spatial Sounds**: Environmental audio references for all game maps
- **MCP Protocol Support**: Full Model Context Protocol implementation for AI integration
- **Comprehensive Coverage**: Data for all current operators and maps
- **Easy Integration**: Simple stdio-based communication for Claude Desktop and other MCP clients

## 🛠️ Available Tools

### get_operator_footsteps

Retrieves detailed audio information about a specific operator's footsteps.

**Parameters:**

- `operator` (string): Name of the operator (e.g., "Ash", "Thermite")

**Example:**

```json
{
  "operator": "Ash"
}
```

**Response:** "Operator Ash: Light, quick footsteps with a slight metallic echo from her boots"

### get_map_spatial_sounds

Provides information about spatial background sounds on a specific map.

**Parameters:**

- `map` (string): Name of the map (e.g., "Bank", "Clubhouse")

**Example:**

```json
{
  "map": "Bank"
}
```

**Response:** "Map Bank: Urban environment with distant traffic, occasional car horns, bank alarms, and echoing footsteps in marble halls"

### list_operators

Returns a comma-separated list of all available operators.

**Parameters:** None

**Response:** "Ace, Alibi, Amaru, Aruni, Ash, Azami, Bandit, ..."

### list_maps

Returns a comma-separated list of all available maps.

**Parameters:** None

**Response:** "Bank, Border, Chalet, Clubhouse, Coastline, ..."

## 📊 Data Coverage

### Operators

- **Total**: 60+ operators
- **Categories**: Attackers and Defenders from all seasons
- **Details**: Unique audio characteristics for each operator's footsteps

### Maps

- **Total**: 25+ maps
- **Environments**: Urban, rural, indoor, outdoor, and special locations
- **Audio**: Spatial sound descriptions including ambient effects

## ⚙️ Configuration

To use this MCP server with Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "siege6-mcp-python": {
      "command": "python",
      "args": ["path/to/your/project/siege6_mcp.py"]
    }
  }
}
```

Replace `path/to/your/project` with the actual path to this project folder.

## 💻 Development

### Project Structure

- `siege6_mcp.py`: Main MCP server implementation
- `requirements.txt`: Python dependencies
- `start_siege6_python.bat`: Windows batch launcher

### Data Storage

Currently uses hardcoded dictionaries for operator and map data. Can be extended to:

- Database integration
- Real-time API data
- Dynamic content updates

### Extending the Server

To add new tools or modify existing ones:

1. Update the `list_tools()` function to include new tool definitions
2. Add corresponding logic in the `call_tool()` function
3. Update data structures as needed

## 📋 Requirements

- **Python**: >= 3.8
- **Dependencies**:
  - `mcp>=1.0.0`: Model Context Protocol library
  - `asyncio`: Built-in async support
  - `typing`: Built-in type hints

## 🔧 Troubleshooting

### Server Won't Start

1. Ensure Python 3.8+ is installed: `python --version`
2. Install dependencies: `pip install -r requirements.txt`
3. Check for import errors in the console output

### MCP Client Connection Issues

1. Verify the path in `claude_desktop_config.json` is correct
2. Ensure the server starts without errors
3. Check that the MCP client supports stdio-based servers

### Data Not Found

- Operator names are case-sensitive
- Use exact map names as listed in `list_maps`
- Check console output for any data loading errors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add/update operator or map data
4. Test the changes
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎮 About Rainbow Six Siege

Rainbow Six Siege is a tactical first-person shooter developed by Ubisoft. This MCP server provides audio reference data to help players identify operators and navigate maps through sound cues during gameplay.</content>
<parameter name="filePath">q:\Apps\mcp_servers\Siege6_mcp\README.md
