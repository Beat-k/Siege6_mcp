#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for Siege6 MCP Enhanced Audio Server
"""

import asyncio
import json
import sys

# Ensure UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
from audio_backend import get_backend_manager, SpatialPosition
from enhanced_audio_data import (
    get_operator_audio_metadata,
    list_operators,
    list_maps,
    ENHANCED_OPERATOR_AUDIO,
    ENHANCED_MAP_AUDIO
)


async def test_basic_functionality():
    """Test basic server functionality"""
    print("=" * 60)
    print("Testing Siege6 MCP Enhanced Audio Server")
    print("=" * 60)

    # Test 1: List operators
    print("\n[TEST 1] Listing operators...")
    operators = list_operators()
    print(f"✓ Found {len(operators)} operators")
    print(f"  Sample: {', '.join(operators[:5])}...")

    # Test 2: List maps
    print("\n[TEST 2] Listing maps...")
    maps = list_maps()
    print(f"✓ Found {len(maps)} maps")
    print(f"  Sample: {', '.join(maps[:5])}...")

    # Test 3: Get operator metadata
    print("\n[TEST 3] Getting operator audio metadata...")
    ash_metadata = get_operator_audio_metadata("Ash")
    print(f"✓ Ash metadata retrieved")
    print(f"  Frequency range: {ash_metadata.frequency_range[0]}-{ash_metadata.frequency_range[1]} Hz")
    print(f"  Volume: {ash_metadata.volume_db} dB")
    print(f"  Spatial falloff: {ash_metadata.spatial_falloff}")

    # Test 4: Audio backend manager
    print("\n[TEST 4] Testing audio backend manager...")
    backend_manager = get_backend_manager()
    active = backend_manager.get_active_backend()
    print(f"✓ Active backend: {active.get_backend_info()['name']}")

    # Test 5: List available backends
    print("\n[TEST 5] Listing available backends...")
    backends = backend_manager.list_available_backends()
    print(f"✓ Found {len(backends)} available backends:")
    for backend in backends:
        print(f"  - {backend['name']} ({backend['type']})")

    # Test 6: Get backend capabilities
    print("\n[TEST 6] Checking backend capabilities...")
    capabilities = backend_manager.get_backend_capabilities()
    print(f"✓ Capabilities:")
    for cap, enabled in capabilities.items():
        status = "✓" if enabled else "✗"
        print(f"  {status} {cap}")

    # Test 7: Process spatial audio
    print("\n[TEST 7] Processing spatial audio...")
    caveira_metadata = get_operator_audio_metadata("Caveira")
    caveira_metadata.position = SpatialPosition(x=10.0, y=2.0, z=5.0)

    listener_pos = SpatialPosition(x=0.0, y=2.0, z=0.0)
    listener_orientation = (45.0, 0.0, 0.0)  # yaw, pitch, roll

    result = backend_manager.get_active_backend().process_spatial_audio(
        caveira_metadata,
        listener_pos,
        listener_orientation
    )

    if result.success:
        print(f"✓ Spatial audio processed successfully")
        print(f"  Distance: {result.processed_audio['distance']:.2f} meters")
        if 'relative_angle_degrees' in result.processed_audio:
            print(f"  Relative angle: {result.processed_audio['relative_angle_degrees']:.2f}°")
        print(f"  Attenuated volume: {result.processed_audio['attenuated_volume_db']:.2f} dB")
    else:
        print(f"✗ Failed: {result.message}")

    # Test 8: Enhanced data validation
    print("\n[TEST 8] Validating enhanced audio data...")
    total_operators = len(ENHANCED_OPERATOR_AUDIO)
    total_maps = len(ENHANCED_MAP_AUDIO)
    print(f"✓ Enhanced operator data: {total_operators} operators")
    print(f"✓ Enhanced map data: {total_maps} maps")

    # Check that all operators have required fields
    required_op_fields = ['description', 'frequency_range', 'volume_db', 'spatial_falloff',
                          'reverb_amount', 'occlusion_factor', 'directional',
                          'speed_multiplier', 'armor_rating', 'special_audio_cues']

    all_valid = True
    for op_name, op_data in ENHANCED_OPERATOR_AUDIO.items():
        for field in required_op_fields:
            if field not in op_data:
                print(f"✗ {op_name} missing field: {field}")
                all_valid = False
                break

    if all_valid:
        print(f"✓ All operator data validated")

    # Check that all maps have required fields
    required_map_fields = ['description', 'ambient_frequency_range', 'ambient_volume_db',
                          'reverb_characteristics', 'spatial_zones', 'ambient_sounds']

    all_valid = True
    for map_name, map_data in ENHANCED_MAP_AUDIO.items():
        for field in required_map_fields:
            if field not in map_data:
                print(f"✗ {map_name} missing field: {field}")
                all_valid = False
                break

    if all_valid:
        print(f"✓ All map data validated")

    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_basic_functionality())
