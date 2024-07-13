import json

def get_noise_settings(mod_id, block_id, leaves = False):
  noise_settings = {
    "sea_level": 50,
    "disable_mob_generation": False,
    "aquifers_enabled": True,
    "ore_veins_enabled": True,
    "legacy_random_source": False,
    "default_block": {
      "Name": f"{mod_id}:{block_id}",
    },
    "default_fluid": {
      "Name": "minecraft:water",
      "Properties": {
        "level": "0"
      }
    },
    "noise": {
      "min_y": 0,
      "height": 384,
      "size_horizontal": 1,
      "size_vertical": 2
    },
    "noise_router": {
      "barrier": 0,
      "fluid_level_floodedness": 0,
      "fluid_level_spread": 0,
      "lava": 0,
      "temperature": 0,
      "vegetation": 0,
      "continents": 0,
      "erosion": 0,
      "depth": 0,
      "ridges": 0,
      "initial_density_without_jaggedness": 0,
      "final_density": {
        "type": "minecraft:interpolated",
        "argument": "minecraft:nether/base_3d_noise"
      },
      "vein_toggle": 0,
      "vein_ridged": 0,
      "vein_gap": 0
    },
    "spawn_target": [],
    "surface_rule": {
      "type": "minecraft:sequence",
      "sequence": []
    }
  }

  if leaves:
    noise_settings["default_block"]["Properties"] = {
      "persistent": "true"
    }

  return noise_settings

def run(mod_id, block_ids):
  for block_id in block_ids:
    leaves = f"{block_id}".endswith("_leaves")

    noise_settings = get_noise_settings(mod_id, block_id, leaves)

    dimensionId = f"{mod_id}__{block_id}"
    file_path = f"data/adm2/worldgen/noise_settings/{dimensionId}.json"

    with open(file_path, "w") as file:
      json.dump(noise_settings, file, indent=2)
      print(f"Generated {file_path}")
