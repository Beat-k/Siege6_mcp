#!/usr/bin/env python3
"""
Siege6 MCP Server - Enhanced Audio Edition
A Model Context Protocol server for Rainbow Six Siege with real spatial audio processing
"""

import asyncio
import sys
import json
from typing import Any, Sequence
from mcp import Tool
from mcp.server import Server
from mcp.types import TextContent, PromptMessage, ListToolsRequest, CallToolRequest

# Import enhanced audio backend system
from audio_backend import (
    AudioBackendType,
    SpatialPosition,
    get_backend_manager
)
from enhanced_audio_data import (
    get_operator_audio_metadata,
    list_operators,
    list_maps,
    ENHANCED_OPERATOR_AUDIO,
    ENHANCED_MAP_AUDIO
)

# Try to import optional backends
try:
    from backend_openal import OpenALBackend
    OPENAL_AVAILABLE = True
except ImportError:
    OPENAL_AVAILABLE = False

try:
    from backend_windows_spatial import WindowsSpatialBackend
    WINDOWS_SPATIAL_AVAILABLE = True
except ImportError:
    WINDOWS_SPATIAL_AVAILABLE = False

# Initialize the server
server = Server("siege6-mcp-enhanced")

# Initialize backend manager and register available backends
backend_manager = get_backend_manager()

if OPENAL_AVAILABLE:
    backend_manager.register_backend(OpenALBackend())
    print("OpenAL backend registered", file=sys.stderr)

if WINDOWS_SPATIAL_AVAILABLE:
    backend_manager.register_backend(WindowsSpatialBackend())
    print("Windows Spatial Sound backend registered", file=sys.stderr)

print(f"Active backend: {backend_manager.get_active_backend().get_backend_info()['name']}", file=sys.stderr)


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="get_operator_footsteps",
            description="Get basic information about operator footsteps sounds in Rainbow Six Siege",
            inputSchema={
                "type": "object",
                "properties": {
                    "operator": {
                        "type": "string",
                        "description": "Name of the operator (e.g., 'Ash', 'Thermite')"
                    }
                },
                "required": ["operator"]
            }
        ),
        Tool(
            name="get_operator_audio_metadata",
            description="Get enhanced audio metadata for an operator including frequency range, volume, spatial characteristics, and special audio cues",
            inputSchema={
                "type": "object",
                "properties": {
                    "operator": {
                        "type": "string",
                        "description": "Name of the operator (e.g., 'Ash', 'Thermite')"
                    }
                },
                "required": ["operator"]
            }
        ),
        Tool(
            name="get_map_spatial_sounds",
            description="Get basic information about spatial background sounds on a map",
            inputSchema={
                "type": "object",
                "properties": {
                    "map": {
                        "type": "string",
                        "description": "Name of the map (e.g., 'Bank', 'Clubhouse')"
                    }
                },
                "required": ["map"]
            }
        ),
        Tool(
            name="get_map_audio_metadata",
            description="Get enhanced audio metadata for a map including ambient sounds, reverb characteristics, and spatial zones",
            inputSchema={
                "type": "object",
                "properties": {
                    "map": {
                        "type": "string",
                        "description": "Name of the map (e.g., 'Bank', 'Clubhouse')"
                    },
                    "zone": {
                        "type": "string",
                        "description": "Optional zone filter (e.g., 'lobby', 'exterior', 'all')",
                        "default": "all"
                    }
                },
                "required": ["map"]
            }
        ),
        Tool(
            name="process_spatial_audio",
            description="Process audio with 3D spatial positioning using the active audio backend (OpenAL, Windows Spatial Sound, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "operator": {
                        "type": "string",
                        "description": "Name of the operator making the sound"
                    },
                    "source_position": {
                        "type": "object",
                        "description": "3D position of the sound source (x, y, z)",
                        "properties": {
                            "x": {"type": "number"},
                            "y": {"type": "number"},
                            "z": {"type": "number"}
                        },
                        "required": ["x", "y", "z"]
                    },
                    "listener_position": {
                        "type": "object",
                        "description": "3D position of the listener (player) (x, y, z)",
                        "properties": {
                            "x": {"type": "number"},
                            "y": {"type": "number"},
                            "z": {"type": "number"}
                        },
                        "required": ["x", "y", "z"]
                    },
                    "listener_orientation": {
                        "type": "object",
                        "description": "Orientation of the listener (yaw, pitch, roll in degrees)",
                        "properties": {
                            "yaw": {"type": "number"},
                            "pitch": {"type": "number"},
                            "roll": {"type": "number"}
                        },
                        "required": ["yaw", "pitch", "roll"]
                    }
                },
                "required": ["operator", "source_position", "listener_position", "listener_orientation"]
            }
        ),
        Tool(
            name="configure_audio_backend",
            description="Switch to a different audio backend (openal, windows_spatial, none)",
            inputSchema={
                "type": "object",
                "properties": {
                    "backend": {
                        "type": "string",
                        "description": "Backend type: 'openal', 'windows_spatial', or 'none'",
                        "enum": ["openal", "windows_spatial", "none"]
                    }
                },
                "required": ["backend"]
            }
        ),
        Tool(
            name="list_audio_backends",
            description="List all available audio backends on this system",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_backend_capabilities",
            description="Get capabilities of the currently active audio backend",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="list_operators",
            description="Get a list of all available operators",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="list_maps",
            description="Get a list of all available maps",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""

    if name == "get_operator_footsteps":
        operator = arguments.get("operator")
        if operator in ENHANCED_OPERATOR_AUDIO:
            description = ENHANCED_OPERATOR_AUDIO[operator]["description"]
            return [TextContent(type="text", text=f"Operator {operator}: {description}")]
        else:
            return [TextContent(type="text", text=f"No footsteps data available for operator: {operator}")]

    elif name == "get_operator_audio_metadata":
        operator = arguments.get("operator")
        if operator in ENHANCED_OPERATOR_AUDIO:
            data = ENHANCED_OPERATOR_AUDIO[operator]
            result = {
                "operator": operator,
                "description": data["description"],
                "audio_properties": {
                    "frequency_range_hz": {"low": data["frequency_range"][0], "high": data["frequency_range"][1]},
                    "volume_db": data["volume_db"],
                    "spatial_falloff": data["spatial_falloff"],
                    "reverb_amount": data["reverb_amount"],
                    "occlusion_factor": data["occlusion_factor"],
                    "directional": data["directional"]
                },
                "gameplay_properties": {
                    "speed_multiplier": data["speed_multiplier"],
                    "armor_rating": data["armor_rating"]
                },
                "special_audio_cues": data["special_audio_cues"]
            }
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        else:
            return [TextContent(type="text", text=f"No audio metadata available for operator: {operator}")]

    elif name == "get_map_spatial_sounds":
        map_name = arguments.get("map")
        if map_name in ENHANCED_MAP_AUDIO:
            description = ENHANCED_MAP_AUDIO[map_name]["description"]
            return [TextContent(type="text", text=f"Map {map_name}: {description}")]
        else:
            return [TextContent(type="text", text=f"No spatial sound data available for map: {map_name}")]

    elif name == "get_map_audio_metadata":
        map_name = arguments.get("map")
        zone = arguments.get("zone", "all")

        if map_name in ENHANCED_MAP_AUDIO:
            data = ENHANCED_MAP_AUDIO[map_name]
            result = {
                "map": map_name,
                "description": data["description"],
                "ambient_properties": {
                    "frequency_range_hz": {"low": data["ambient_frequency_range"][0], "high": data["ambient_frequency_range"][1]},
                    "ambient_volume_db": data["ambient_volume_db"]
                },
                "reverb_characteristics": data["reverb_characteristics"],
                "spatial_zones": data["spatial_zones"],
                "ambient_sounds": []
            }

            # Add ambient sounds for the requested zone
            for ambient in data.get("ambient_sounds", []):
                if zone == "all" or ambient["position"] == zone or ambient["position"] == "all":
                    result["ambient_sounds"].append(ambient)

            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        else:
            return [TextContent(type="text", text=f"No audio metadata available for map: {map_name}")]

    elif name == "process_spatial_audio":
        operator = arguments.get("operator")
        source_pos = arguments.get("source_position")
        listener_pos = arguments.get("listener_position")
        listener_orient = arguments.get("listener_orientation")

        # Get operator audio metadata
        audio_metadata = get_operator_audio_metadata(operator)

        # Set source position
        audio_metadata.position = SpatialPosition(
            x=source_pos["x"],
            y=source_pos["y"],
            z=source_pos["z"]
        )

        # Create listener position
        listener_position = SpatialPosition(
            x=listener_pos["x"],
            y=listener_pos["y"],
            z=listener_pos["z"]
        )

        # Create orientation tuple
        orientation = (
            listener_orient["yaw"],
            listener_orient["pitch"],
            listener_orient["roll"]
        )

        # Process with active backend
        result = backend_manager.get_active_backend().process_spatial_audio(
            audio_metadata,
            listener_position,
            orientation
        )

        output = {
            "operator": operator,
            "success": result.success,
            "message": result.message,
            "processed_audio": result.processed_audio,
            "backend": result.backend_info
        }

        return [TextContent(type="text", text=json.dumps(output, indent=2))]

    elif name == "configure_audio_backend":
        backend_str = arguments.get("backend")

        # Map string to enum
        backend_map = {
            "openal": AudioBackendType.OPENAL,
            "windows_spatial": AudioBackendType.WINDOWS_SPATIAL,
            "none": AudioBackendType.NONE
        }

        backend_type = backend_map.get(backend_str)
        if backend_type is None:
            return [TextContent(type="text", text=f"Unknown backend: {backend_str}")]

        success = backend_manager.set_active_backend(backend_type)

        if success:
            info = backend_manager.get_active_backend().get_backend_info()
            return [TextContent(type="text", text=f"Successfully switched to: {info['name']}\n{json.dumps(info, indent=2)}")]
        else:
            return [TextContent(type="text", text=f"Failed to switch to backend: {backend_str}. Backend may not be available on this system.")]

    elif name == "list_audio_backends":
        backends = backend_manager.list_available_backends()
        result = {
            "available_backends": backends,
            "active_backend": backend_manager.get_active_backend().get_backend_info()
        }
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "get_backend_capabilities":
        capabilities = backend_manager.get_backend_capabilities()
        backend_info = backend_manager.get_active_backend().get_backend_info()
        result = {
            "backend": backend_info,
            "capabilities": capabilities
        }
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "list_operators":
        operators = list_operators()
        return [TextContent(type="text", text=", ".join(operators))]

    elif name == "list_maps":
        maps = list_maps()
        return [TextContent(type="text", text=", ".join(maps))]

    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    """Main entry point for the MCP server."""
    from mcp.server.stdio import stdio_server

    print("=" * 60, file=sys.stderr)
    print("Siege6 MCP Enhanced Audio Server", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print(f"Active Backend: {backend_manager.get_active_backend().get_backend_info()['name']}", file=sys.stderr)
    print(f"Operators: {len(list_operators())}", file=sys.stderr)
    print(f"Maps: {len(list_maps())}", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
