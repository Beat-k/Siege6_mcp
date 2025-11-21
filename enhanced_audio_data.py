"""
Enhanced Audio Data for Rainbow Six Siege
Includes spatial audio metadata, frequency ranges, and 3D characteristics
"""

from typing import Dict, List
from audio_backend import AudioMetadata, SpatialPosition


# Enhanced Operator Audio Data with Spatial Metadata
ENHANCED_OPERATOR_AUDIO: Dict[str, Dict] = {
    "Ash": {
        "description": "Light, quick footsteps with a slight metallic echo from her boots",
        "frequency_range": (800, 3200),  # Hz - higher frequency, lighter footsteps
        "volume_db": -18.0,
        "spatial_falloff": 2.5,  # Quiet, falls off quickly
        "reverb_amount": 0.3,
        "occlusion_factor": 0.7,  # Light sounds pass through walls somewhat
        "directional": True,
        "speed_multiplier": 1.2,  # Faster than average
        "armor_rating": 1,  # Light armor
        "special_audio_cues": ["Breaching round launch (low thump)", "Breaching explosion"]
    },
    "Thermite": {
        "description": "Heavy, deliberate footsteps with rattling equipment and gear",
        "frequency_range": (200, 1800),  # Lower frequency, heavier
        "volume_db": -12.0,
        "spatial_falloff": 1.8,
        "reverb_amount": 0.5,
        "occlusion_factor": 0.4,  # Heavy sounds more blocked
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 2,
        "special_audio_cues": ["Exothermic charge placement", "Thermite burning (intense crackling)"]
    },
    "Sledge": {
        "description": "Heavy footsteps with the distinctive sound of his hammer against his leg",
        "frequency_range": (180, 1600),
        "volume_db": -11.0,
        "spatial_falloff": 1.7,
        "reverb_amount": 0.6,
        "occlusion_factor": 0.3,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 2,
        "special_audio_cues": ["Hammer swing (whoosh)", "Hammer impact (loud crash)", "Debris falling"]
    },
    "Thatcher": {
        "description": "Medium-weight footsteps with slight gear jingling",
        "frequency_range": (300, 2000),
        "volume_db": -14.0,
        "spatial_falloff": 2.0,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.5,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 2,
        "special_audio_cues": ["EMP grenade throw", "EMP detonation (electronic buzz)", "Electronics fizzling"]
    },
    "Twitch": {
        "description": "Quick, light footsteps with tactical gear sounds",
        "frequency_range": (600, 2800),
        "volume_db": -16.0,
        "spatial_falloff": 2.3,
        "reverb_amount": 0.35,
        "occlusion_factor": 0.6,
        "directional": True,
        "speed_multiplier": 1.1,
        "armor_rating": 2,
        "special_audio_cues": ["Shock drone deployment", "Drone motor whirring", "Taser shot (electric zap)"]
    },
    "Montagne": {
        "description": "Very heavy, slow footsteps with loud metallic shield dragging",
        "frequency_range": (120, 1400),
        "volume_db": -8.0,  # Very loud
        "spatial_falloff": 1.5,  # Heard from far away
        "reverb_amount": 0.7,
        "occlusion_factor": 0.2,  # Very blocked by walls
        "directional": True,
        "speed_multiplier": 0.8,
        "armor_rating": 3,
        "special_audio_cues": ["Shield extending (mechanical whir)", "Shield fully extended (loud clang)", "Shield impacts"]
    },
    "IQ": {
        "description": "Light, athletic footsteps with minimal gear noise",
        "frequency_range": (700, 3000),
        "volume_db": -19.0,
        "spatial_falloff": 2.6,
        "reverb_amount": 0.3,
        "occlusion_factor": 0.75,
        "directional": True,
        "speed_multiplier": 1.15,
        "armor_rating": 1,
        "special_audio_cues": ["Electronics detector activation (beeping)", "Signal detection (increasing beep frequency)"]
    },
    "Caveira": {
        "description": "Nearly silent footsteps when using Silent Step ability, otherwise light padding",
        "frequency_range": (400, 2200),
        "volume_db": -25.0,  # Extremely quiet
        "spatial_falloff": 3.5,  # Very short range
        "reverb_amount": 0.15,  # Minimal reverb
        "occlusion_factor": 0.9,  # Passes through walls easily (quiet)
        "directional": False,  # Hard to locate
        "speed_multiplier": 1.3,
        "armor_rating": 1,
        "special_audio_cues": ["Silent Step activation (whisper)", "Interrogation (muffled screams)"]
    },
    "Bandit": {
        "description": "Quick footsteps with electrical equipment jingling",
        "frequency_range": (500, 2400),
        "volume_db": -15.0,
        "spatial_falloff": 2.2,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.6,
        "directional": True,
        "speed_multiplier": 1.1,
        "armor_rating": 1,
        "special_audio_cues": ["Shock wire placement", "Electrical buzzing", "Electricity arcing"]
    },
    "Jager": {
        "description": "Medium footsteps with distinctive equipment clanking",
        "frequency_range": (400, 2200),
        "volume_db": -14.0,
        "spatial_falloff": 2.1,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.55,
        "directional": True,
        "speed_multiplier": 1.05,
        "armor_rating": 2,
        "special_audio_cues": ["ADS placement", "ADS activation (rapid mechanical clicking)", "Projectile interception"]
    },
    "Rook": {
        "description": "Heavy footsteps with armor plates and gear rattling",
        "frequency_range": (180, 1500),
        "volume_db": -11.0,
        "spatial_falloff": 1.8,
        "reverb_amount": 0.55,
        "occlusion_factor": 0.35,
        "directional": True,
        "speed_multiplier": 0.95,
        "armor_rating": 3,
        "special_audio_cues": ["Armor plate bag drop (heavy thud)", "Plate pickup (clanking)"]
    },
    "Doc": {
        "description": "Medium-heavy footsteps with medical equipment rattling",
        "frequency_range": (280, 1900),
        "volume_db": -13.0,
        "spatial_falloff": 2.0,
        "reverb_amount": 0.45,
        "occlusion_factor": 0.5,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 3,
        "special_audio_cues": ["Stim pistol shot (pneumatic hiss)", "Healing boost activation"]
    },
    "Vigil": {
        "description": "Stealthy footsteps with electronic equipment hum",
        "frequency_range": (450, 2300),
        "volume_db": -17.0,
        "spatial_falloff": 2.4,
        "reverb_amount": 0.35,
        "occlusion_factor": 0.65,
        "directional": True,
        "speed_multiplier": 1.15,
        "armor_rating": 2,
        "special_audio_cues": ["ERC-7 activation (electronic whine)", "Video disruption effect", "Drone static"]
    },
    "Ela": {
        "description": "Quick, light footsteps with mine canisters clinking",
        "frequency_range": (600, 2700),
        "volume_db": -16.0,
        "spatial_falloff": 2.3,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.6,
        "directional": True,
        "speed_multiplier": 1.1,
        "armor_rating": 1,
        "special_audio_cues": ["Grzmot mine deployment", "Mine detonation (loud concussive blast)", "Concussion ringing"]
    },
    "Lesion": {
        "description": "Medium footsteps with Gu mine canisters rustling",
        "frequency_range": (350, 2100),
        "volume_db": -15.0,
        "spatial_falloff": 2.1,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.55,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 2,
        "special_audio_cues": ["Gu mine throw", "Mine cloaking (electronic shimmer)", "Needle impact", "Poison damage tick"]
    },
    "Alibi": {
        "description": "Light, tactical footsteps with hologram projectors",
        "frequency_range": (550, 2600),
        "volume_db": -16.0,
        "spatial_falloff": 2.2,
        "reverb_amount": 0.35,
        "occlusion_factor": 0.65,
        "directional": True,
        "speed_multiplier": 1.05,
        "armor_rating": 1,
        "special_audio_cues": ["Prisma deployment", "Hologram activation (electronic hum)", "Hologram detection alert"]
    },
    "Maestro": {
        "description": "Heavy footsteps with camera turret equipment",
        "frequency_range": (200, 1700),
        "volume_db": -12.0,
        "spatial_falloff": 1.9,
        "reverb_amount": 0.5,
        "occlusion_factor": 0.4,
        "directional": True,
        "speed_multiplier": 0.95,
        "armor_rating": 3,
        "special_audio_cues": ["Evil Eye deployment", "Turret rotation (mechanical servo)", "Laser shot (high-pitched zap)"]
    },
    "Clash": {
        "description": "Heavy footsteps with CCE Shield electrical systems",
        "frequency_range": (180, 1600),
        "volume_db": -10.0,
        "spatial_falloff": 1.7,
        "reverb_amount": 0.6,
        "occlusion_factor": 0.3,
        "directional": True,
        "speed_multiplier": 0.85,
        "armor_rating": 3,
        "special_audio_cues": ["Shield extension", "Taser activation (continuous zapping)", "Shield bash"]
    },
    "Kaid": {
        "description": "Medium-heavy footsteps with Rtila Electroclaw equipment",
        "frequency_range": (250, 1800),
        "volume_db": -13.0,
        "spatial_falloff": 2.0,
        "reverb_amount": 0.45,
        "occlusion_factor": 0.5,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 3,
        "special_audio_cues": ["Electroclaw throw", "Claw attachment (metal clink)", "Electrification (buzzing)"]
    },
    "Mozzie": {
        "description": "Light footsteps with Pest launcher and drones",
        "frequency_range": (650, 2800),
        "volume_db": -17.0,
        "spatial_falloff": 2.4,
        "reverb_amount": 0.35,
        "occlusion_factor": 0.65,
        "directional": True,
        "speed_multiplier": 1.1,
        "armor_rating": 2,
        "special_audio_cues": ["Pest launcher shot", "Drone hack (electronic interference)", "Hacked drone motor"]
    },
    "Warden": {
        "description": "Medium-heavy footsteps with smart glasses equipment",
        "frequency_range": (280, 1900),
        "volume_db": -13.0,
        "spatial_falloff": 2.0,
        "reverb_amount": 0.45,
        "occlusion_factor": 0.5,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 2,
        "special_audio_cues": ["Glance activation (electronic beep)", "Vision mode switching"]
    },
    "Goyo": {
        "description": "Medium footsteps with Volcan Shield canisters",
        "frequency_range": (300, 2000),
        "volume_db": -14.0,
        "spatial_falloff": 2.1,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.55,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 2,
        "special_audio_cues": ["Shield deployment", "Canister explosion", "Fire spreading (roaring flames)"]
    },
    "Wamai": {
        "description": "Light-medium footsteps with Mag-NET systems",
        "frequency_range": (400, 2200),
        "volume_db": -15.0,
        "spatial_falloff": 2.2,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.6,
        "directional": True,
        "speed_multiplier": 1.05,
        "armor_rating": 2,
        "special_audio_cues": ["Mag-NET throw", "Magnetic attachment (metallic click)", "Projectile capture (magnetic pull)"]
    },
    "Oryx": {
        "description": "Heavy, aggressive footsteps, sprint is extremely loud with dash ability",
        "frequency_range": (150, 1500),
        "volume_db": -10.0,  # Loud normally, -5.0 when dashing
        "spatial_falloff": 1.6,
        "reverb_amount": 0.6,
        "occlusion_factor": 0.25,
        "directional": True,
        "speed_multiplier": 1.3,  # When dashing
        "armor_rating": 2,
        "special_audio_cues": ["Remah Dash charge", "Wall/hatch crash (extremely loud)", "Heavy breathing"]
    },
    "Melusi": {
        "description": "Medium footsteps with Banshee equipment",
        "frequency_range": (350, 2100),
        "volume_db": -15.0,
        "spatial_falloff": 2.1,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.55,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 3,
        "special_audio_cues": ["Banshee deployment", "Sonic wave activation (loud wail)", "Area denial sound"]
    },
    "Aruni": {
        "description": "Distinctive footsteps with prosthetic arm mechanical sounds",
        "frequency_range": (300, 2000),
        "volume_db": -14.0,
        "spatial_falloff": 2.0,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.55,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 2,
        "special_audio_cues": ["Surya Gate deployment", "Laser grid activation (humming)", "Prosthetic punch (mechanical)"]
    },
    "Thunderbird": {
        "description": "Medium footsteps with Kona Station equipment",
        "frequency_range": (350, 2100),
        "volume_db": -14.0,
        "spatial_falloff": 2.1,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.55,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 2,
        "special_audio_cues": ["Station deployment", "Healing activation (medical beeps)", "Station recharge"]
    },
    "Azami": {
        "description": "Light, ninja-like footsteps with Kiba Barrier launcher",
        "frequency_range": (500, 2500),
        "volume_db": -17.0,
        "spatial_falloff": 2.3,
        "reverb_amount": 0.35,
        "occlusion_factor": 0.65,
        "directional": True,
        "speed_multiplier": 1.1,
        "armor_rating": 2,
        "special_audio_cues": ["Kunai throw", "Barrier expanding (foaming sound)", "Surface impact"]
    },
    "Thorn": {
        "description": "Medium footsteps with Razorbloom Shell equipment",
        "frequency_range": (350, 2100),
        "volume_db": -15.0,
        "spatial_falloff": 2.1,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.55,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 2,
        "special_audio_cues": ["Shell deployment", "Proximity detection (beeping)", "Detonation (explosive blast)"]
    },
    "Solis": {
        "description": "Light-medium footsteps with SPEC-IO Electro-Sensor equipment",
        "frequency_range": (450, 2300),
        "volume_db": -16.0,
        "spatial_falloff": 2.2,
        "reverb_amount": 0.38,
        "occlusion_factor": 0.6,
        "directional": True,
        "speed_multiplier": 1.05,
        "armor_rating": 2,
        "special_audio_cues": ["Scanner activation (electronic pulse)", "Electronics detection (pinging)", "Cluster scan"]
    },
    "Fenrir": {
        "description": "Medium footsteps with F-NATT Dread Mine equipment",
        "frequency_range": (350, 2100),
        "volume_db": -15.0,
        "spatial_falloff": 2.1,
        "reverb_amount": 0.4,
        "occlusion_factor": 0.55,
        "directional": True,
        "speed_multiplier": 1.0,
        "armor_rating": 2,
        "special_audio_cues": ["Mine deployment", "Fear effect activation (unsettling sound)", "Vision distortion"]
    }
}


# Enhanced Map Spatial Audio Data
ENHANCED_MAP_AUDIO: Dict[str, Dict] = {
    "Bank": {
        "description": "Urban environment with distant traffic, occasional car horns, bank alarms, and echoing footsteps in marble halls",
        "ambient_frequency_range": (80, 4000),
        "ambient_volume_db": -35.0,
        "reverb_characteristics": {
            "lobby": {"reverb": 0.8, "echo_delay": 0.15, "description": "Large marble hall with high ceiling"},
            "offices": {"reverb": 0.3, "echo_delay": 0.05, "description": "Carpeted rooms with furniture"},
            "vault": {"reverb": 0.6, "echo_delay": 0.12, "description": "Metal surfaces with concrete"},
            "basement": {"reverb": 0.5, "echo_delay": 0.08, "description": "Concrete corridors"}
        },
        "spatial_zones": {
            "exterior": {"occlusion": 0.2, "outdoor_factor": 1.0},
            "interior": {"occlusion": 0.6, "outdoor_factor": 0.0}
        },
        "ambient_sounds": [
            {"name": "city_traffic", "frequency": (100, 800), "volume_db": -40.0, "position": "exterior"},
            {"name": "bank_alarm", "frequency": (1200, 3500), "volume_db": -25.0, "position": "lobby"},
            {"name": "hvac_hum", "frequency": (60, 250), "volume_db": -45.0, "position": "all"}
        ]
    },
    "Clubhouse": {
        "description": "Motorcycle clubhouse with bike engine sounds, metal clanking, basement machinery hum",
        "ambient_frequency_range": (70, 3500),
        "ambient_volume_db": -38.0,
        "reverb_characteristics": {
            "bar": {"reverb": 0.4, "echo_delay": 0.06, "description": "Wooden interior with bottles"},
            "garage": {"reverb": 0.5, "echo_delay": 0.08, "description": "Large concrete room"},
            "basement": {"reverb": 0.6, "echo_delay": 0.1, "description": "Stone walls and metal"},
            "bedroom": {"reverb": 0.25, "echo_delay": 0.04, "description": "Small furnished room"}
        },
        "spatial_zones": {
            "exterior": {"occlusion": 0.15, "outdoor_factor": 1.0},
            "interior": {"occlusion": 0.65, "outdoor_factor": 0.0}
        },
        "ambient_sounds": [
            {"name": "distant_motorcycles", "frequency": (150, 1000), "volume_db": -42.0, "position": "exterior"},
            {"name": "basement_machinery", "frequency": (80, 400), "volume_db": -35.0, "position": "basement"},
            {"name": "metal_creaking", "frequency": (200, 800), "volume_db": -48.0, "position": "all"}
        ]
    },
    "Consulate": {
        "description": "Government building with echoing hallways, office equipment hum, exterior vehicle sounds",
        "ambient_frequency_range": (75, 4200),
        "ambient_volume_db": -36.0,
        "reverb_characteristics": {
            "main_hall": {"reverb": 0.75, "echo_delay": 0.14, "description": "Large open space"},
            "offices": {"reverb": 0.3, "echo_delay": 0.05, "description": "Standard office rooms"},
            "press_room": {"reverb": 0.5, "echo_delay": 0.08, "description": "Conference area"},
            "garage": {"reverb": 0.55, "echo_delay": 0.09, "description": "Underground parking"}
        },
        "spatial_zones": {
            "exterior": {"occlusion": 0.18, "outdoor_factor": 1.0},
            "interior": {"occlusion": 0.62, "outdoor_factor": 0.0}
        },
        "ambient_sounds": [
            {"name": "office_equipment", "frequency": (200, 1500), "volume_db": -42.0, "position": "offices"},
            {"name": "hvac_system", "frequency": (70, 300), "volume_db": -45.0, "position": "all"},
            {"name": "exterior_traffic", "frequency": (120, 900), "volume_db": -40.0, "position": "exterior"}
        ]
    },
    "Oregon": {
        "description": "Rural compound with wind through trees, creaking wood, distant wildlife",
        "ambient_frequency_range": (60, 5000),
        "ambient_volume_db": -40.0,
        "reverb_characteristics": {
            "dorms": {"reverb": 0.35, "echo_delay": 0.055, "description": "Wooden building interior"},
            "meeting_hall": {"reverb": 0.5, "echo_delay": 0.08, "description": "Large wooden room"},
            "basement": {"reverb": 0.45, "echo_delay": 0.07, "description": "Concrete foundation"},
            "tower": {"reverb": 0.3, "echo_delay": 0.05, "description": "Small elevated space"}
        },
        "spatial_zones": {
            "exterior": {"occlusion": 0.1, "outdoor_factor": 1.0},
            "interior": {"occlusion": 0.5, "outdoor_factor": 0.1}
        },
        "ambient_sounds": [
            {"name": "wind_through_trees", "frequency": (80, 2000), "volume_db": -42.0, "position": "exterior"},
            {"name": "wood_creaking", "frequency": (150, 600), "volume_db": -48.0, "position": "dorms"},
            {"name": "distant_birds", "frequency": (1000, 4500), "volume_db": -50.0, "position": "exterior"}
        ]
    },
    "Hereford": {
        "description": "Military training facility with metal echoes, outdoor wind, target range sounds",
        "ambient_frequency_range": (65, 4500),
        "ambient_volume_db": -38.0,
        "reverb_characteristics": {
            "hallways": {"reverb": 0.6, "echo_delay": 0.1, "description": "Concrete military corridors"},
            "garage": {"reverb": 0.55, "echo_delay": 0.09, "description": "Large vehicle bay"},
            "rooms": {"reverb": 0.35, "echo_delay": 0.055, "description": "Basic military rooms"},
            "stairs": {"reverb": 0.7, "echo_delay": 0.12, "description": "Metal staircases"}
        },
        "spatial_zones": {
            "exterior": {"occlusion": 0.15, "outdoor_factor": 1.0},
            "interior": {"occlusion": 0.7, "outdoor_factor": 0.0}
        },
        "ambient_sounds": [
            {"name": "wind", "frequency": (70, 1500), "volume_db": -43.0, "position": "exterior"},
            {"name": "metal_echoes", "frequency": (400, 2000), "volume_db": -46.0, "position": "stairs"},
            {"name": "distant_training", "frequency": (200, 3000), "volume_db": -48.0, "position": "exterior"}
        ]
    },
    "House": {
        "description": "Suburban home with creaking floors, ambient neighborhood sounds, interior echoes",
        "ambient_frequency_range": (70, 4000),
        "ambient_volume_db": -40.0,
        "reverb_characteristics": {
            "garage": {"reverb": 0.5, "echo_delay": 0.08, "description": "Concrete floor, open space"},
            "living_areas": {"reverb": 0.3, "echo_delay": 0.05, "description": "Furnished rooms with carpet"},
            "workshop": {"reverb": 0.45, "echo_delay": 0.07, "description": "Basement workshop"},
            "bedrooms": {"reverb": 0.25, "echo_delay": 0.04, "description": "Small carpeted rooms"}
        },
        "spatial_zones": {
            "exterior": {"occlusion": 0.12, "outdoor_factor": 1.0},
            "interior": {"occlusion": 0.55, "outdoor_factor": 0.15}
        },
        "ambient_sounds": [
            {"name": "suburban_ambience", "frequency": (100, 2500), "volume_db": -45.0, "position": "exterior"},
            {"name": "floor_creaking", "frequency": (200, 800), "volume_db": -50.0, "position": "all"},
            {"name": "pipes_settling", "frequency": (80, 400), "volume_db": -52.0, "position": "workshop"}
        ]
    },
    "Kanal": {
        "description": "Industrial waterfront with boat horns, water lapping, metal structures creaking",
        "ambient_frequency_range": (50, 4000),
        "ambient_volume_db": -35.0,
        "reverb_characteristics": {
            "boat_house": {"reverb": 0.7, "echo_delay": 0.13, "description": "Large space over water"},
            "control_room": {"reverb": 0.4, "echo_delay": 0.06, "description": "Equipment-filled room"},
            "walkways": {"reverb": 0.6, "echo_delay": 0.1, "description": "Metal catwalks"},
            "maps_office": {"reverb": 0.35, "echo_delay": 0.055, "description": "Office space"}
        },
        "spatial_zones": {
            "exterior": {"occlusion": 0.1, "outdoor_factor": 1.0},
            "interior": {"occlusion": 0.6, "outdoor_factor": 0.2}
        },
        "ambient_sounds": [
            {"name": "water_lapping", "frequency": (60, 500), "volume_db": -38.0, "position": "boat_house"},
            {"name": "boat_horns", "frequency": (100, 800), "volume_db": -45.0, "position": "exterior"},
            {"name": "metal_creaking", "frequency": (150, 1000), "volume_db": -42.0, "position": "walkways"},
            {"name": "seagulls", "frequency": (1500, 4000), "volume_db": -48.0, "position": "exterior"}
        ]
    },
    "Chalet": {
        "description": "Mountain lodge with wind howling, wood creaking, fireplace crackling",
        "ambient_frequency_range": (65, 5000),
        "ambient_volume_db": -38.0,
        "reverb_characteristics": {
            "main_hall": {"reverb": 0.55, "echo_delay": 0.09, "description": "Large wooden hall"},
            "bedrooms": {"reverb": 0.3, "echo_delay": 0.05, "description": "Small furnished rooms"},
            "garage": {"reverb": 0.5, "echo_delay": 0.08, "description": "Concrete and wood"},
            "wine_cellar": {"reverb": 0.45, "echo_delay": 0.07, "description": "Stone basement"}
        },
        "spatial_zones": {
            "exterior": {"occlusion": 0.08, "outdoor_factor": 1.0},
            "interior": {"occlusion": 0.5, "outdoor_factor": 0.1}
        },
        "ambient_sounds": [
            {"name": "mountain_wind", "frequency": (70, 2500), "volume_db": -36.0, "position": "exterior"},
            {"name": "fireplace_crackling", "frequency": (100, 1500), "volume_db": -44.0, "position": "main_hall"},
            {"name": "wood_settling", "frequency": (150, 700), "volume_db": -50.0, "position": "all"}
        ]
    }
}


def get_operator_audio_metadata(operator_name: str) -> AudioMetadata:
    """Convert operator data to AudioMetadata object"""
    if operator_name not in ENHANCED_OPERATOR_AUDIO:
        # Return default metadata for unknown operators
        return AudioMetadata(
            name=operator_name,
            description=f"Unknown operator: {operator_name}",
            frequency_range=(300, 2000),
            volume_db=-15.0,
            spatial_falloff=2.0,
            reverb_amount=0.4,
            occlusion_factor=0.5,
            directional=True
        )

    data = ENHANCED_OPERATOR_AUDIO[operator_name]
    return AudioMetadata(
        name=operator_name,
        description=data["description"],
        frequency_range=data["frequency_range"],
        volume_db=data["volume_db"],
        spatial_falloff=data["spatial_falloff"],
        reverb_amount=data["reverb_amount"],
        occlusion_factor=data["occlusion_factor"],
        directional=data["directional"]
    )


def get_map_ambient_metadata(map_name: str, zone: str = "all") -> List[AudioMetadata]:
    """Get ambient sound metadata for a map"""
    if map_name not in ENHANCED_MAP_AUDIO:
        return []

    map_data = ENHANCED_MAP_AUDIO[map_name]
    ambient_list = []

    for ambient in map_data.get("ambient_sounds", []):
        if ambient["position"] == "all" or ambient["position"] == zone or zone == "all":
            metadata = AudioMetadata(
                name=f"{map_name}_{ambient['name']}",
                description=f"Ambient sound: {ambient['name']} on {map_name}",
                frequency_range=ambient["frequency"],
                volume_db=ambient["volume_db"],
                spatial_falloff=1.0,  # Ambient sounds don't fall off as quickly
                reverb_amount=0.2,
                occlusion_factor=0.8,  # Ambient sounds pass through easily
                directional=False  # Ambient sounds are omnidirectional
            )
            ambient_list.append(metadata)

    return ambient_list


def list_operators() -> List[str]:
    """Get list of all operators with enhanced audio data"""
    return sorted(ENHANCED_OPERATOR_AUDIO.keys())


def list_maps() -> List[str]:
    """Get list of all maps with enhanced audio data"""
    return sorted(ENHANCED_MAP_AUDIO.keys())
