# Siege6 Audio Reference

A comprehensive audio reference system for Rainbow Six Siege that provides instant access to operator footsteps and map spatial sounds during gameplay.

## 🚀 Quick Start

### Desktop App (Recommended for In-Game Use)

1. Navigate to the `desktop-app` folder
2. Install dependencies: `npm install`
3. Start the app: `npm start`
4. The app runs in the background
5. Press `Ctrl+Alt+F12` during gameplay to instantly access audio references
6. The reference window appears instantly with search functionality
7. Press the hotkey again or click outside to hide

**Status**: ✅ Working - No freezing, global hotkey functional, search enabled

### MCP Server (For AI Integration)

An MCP (Model Context Protocol) server that provides tools for Rainbow Six Siege game data, specifically focused on footsteps and spatial background sounds.

#### TypeScript Version (Original)

```bash
npm start
```

#### Python Version (Alternative)

```bash
pip install -r requirements.txt
python siege6_mcp.py
```

## Features

- **Operator Footsteps**: Get detailed information about operator footsteps sounds in Rainbow Six Siege
- **Map Spatial Sounds**: Retrieve information about spatial background sounds on different maps
- **In-Game Access**: Desktop app with global hotkey for instant reference during matches
- **System Tray**: Minimizes to tray for zero distraction
- **Quick Search**: Filter operators and maps instantly
- **Always-on-Top**: Window stays visible when activated

## Desktop App Usage

The desktop application provides true in-game performance benefits:

- **Global Hotkey**: `Ctrl+Alt+F12` to show/hide instantly
- **System Tray**: Runs in background, no taskbar clutter
- **Quick Search**: Type to filter operators/maps instantly
- **Always-on-Top**: Stays visible when you need it
- **Click to Hide**: Click outside or press hotkey again to hide

### Installation

```bash
cd desktop-app
npm install
npm start
```

### Building for Distribution

```bash
npm run dist
```

This creates executable files in the `dist` folder for Windows, macOS, and Linux.

## Usage

After building, start the MCP server:

```bash
npm start
```

The server will run on stdio and listen for MCP protocol messages.

## Configuration

To use this MCP server with Claude Desktop, add the following to your `claude_desktop_config.json`:

### TypeScript Version
```json
{
  "mcpServers": {
    "siege6-mcp": {
      "command": "node",
      "args": ["path/to/your/project/dist/index.js"]
    }
  }
}
```

### Python Version
```json
{
  "mcpServers": {
    "siege6-mcp": {
      "command": "python",
      "args": ["path/to/your/project/siege6_mcp.py"]
    }
  }
}
```

Replace `path/to/your/project` with the actual path to this project folder.

## Tools Provided

### get_operator_footsteps

Returns information about a specific operator's footsteps sounds.

**Parameters:**
- `operator` (string): Name of the operator (e.g., "Ash", "Thermite")

**Example:**
```json
{
  "operator": "Ash"
}
```

### get_map_spatial_sounds

Returns information about spatial background sounds on a specific map.

**Parameters:**
- `map` (string): Name of the map (e.g., "Bank", "Clubhouse")

**Example:**
```json
{
  "map": "Bank"
}
```

### list_operators (Python version only)

Returns a list of all available operators.

**Returns:** Comma-separated list of operator names

### list_maps (Python version only)

Returns a list of all available maps.

**Returns:** Comma-separated list of map names

### list_operators (Python version only)

Returns a list of all available operators.

**Returns:** Comma-separated list of operator names

### list_maps (Python version only)

Returns a list of all available maps.

**Returns:** Comma-separated list of map names
```json
{
  "map": "Bank"
}
```

## Data

The server includes hardcoded data for all Rainbow Six Siege operators and maps. In a production environment, this could be extended to fetch real-time data from game APIs or databases.

## Development

- Source code: `src/index.ts`
- Build output: `dist/index.js`
- Configuration: `tsconfig.json`

## Requirements

### TypeScript Version
- Node.js >= 18
- TypeScript
- @modelcontextprotocol/sdk

### Python Version
- Python >= 3.8
- mcp package
- See `requirements.txt` for dependencies