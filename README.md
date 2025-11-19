# Siege6 MCP Server

An MCP (Model Context Protocol) server that provides tools for Rainbow Six Siege game data, specifically focused on footsteps and spatial background sounds.

## Features

- **Operator Footsteps**: Get detailed information about operator footsteps sounds in Rainbow Six Siege
- **Map Spatial Sounds**: Retrieve information about spatial background sounds on different maps

## Usage

After building, start the MCP server:

```bash
npm start
```

The server will run on stdio and listen for MCP protocol messages.

## Configuration

To use this MCP server with Claude Desktop, add the following to your `claude_desktop_config.json`:

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

## Data

The server includes hardcoded data for all Rainbow Six Siege operators and maps. In a production environment, this could be extended to fetch real-time data from game APIs or databases.

## Development

- Source code: `src/index.ts`
- Build output: `dist/index.js`
- Configuration: `tsconfig.json`

## Requirements

- Node.js >= 18
- TypeScript
- @modelcontextprotocol/sdk