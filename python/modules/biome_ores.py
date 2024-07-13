import json

def get_biome(ids):
  features = []

  for id in ids:
    features.append([f"adm2:{id}"])

  biome_object = {
    "temperature": 1,
    "downfall": 0.5,
    "has_precipitation": False,
    "temperature_modifier": "none",
    "creature_spawn_probability": 0,
    "effects": {
      "sky_color": 13421772,
      "fog_color": 13421772,
      "water_color": 13421772,
      "water_fog_color": 13421772
    },
    "spawners": {},
    "spawn_costs": {},
    "carvers": {
      "air": [
        "adm2:caves",
        "adm2:canyons"
      ],
      "liquid": []
    },
    "features": features
  }

  return biome_object

def target_object(blockId, oreId):
  target_object = {
    "target": {
      "predicate_type": "minecraft:block_match",
      "block": f"{blockId}"
    },
    "state": {
      "Name": f"{oreId}"
    }
  }

  return target_object

def get_placed_feature(blockIds, oreId, size, count):
  targets = []

  for blockId in blockIds:
    targets.append(target_object(blockId, oreId))

  ore_object = {
    "feature": {
      "type": "minecraft:ore",
      "config": {
        "size": size,
        "discard_chance_on_air_exposure": 0,
        "targets": targets
      }
    },
    "placement": [
      {
        "type": "minecraft:count",
        "count": count
      },
      {
        "type": "minecraft:in_square"
      },
      {
        "type": "minecraft:height_range",
        "height": {
          "type": "minecraft:uniform",
          "min_inclusive": {
            "above_bottom": 0
          },
          "max_inclusive": {
            "below_top": 0
          }
        }
      },
      {
        "type": "minecraft:biome"
      }
    ]
  }

  return ore_object

def run(mod_id, block_ids):
  featureBlockIds = [f"{mod_id}:{block_id}" for block_id in block_ids]
  featureOres = [
    ("minecraft:tnt", 32, 6, f"{mod_id}_tnt"),
    ("minecraft:pearlescent_froglight", 12, 4, f"{mod_id}_pearlescent_froglight"),
    ("minecraft:sand", 20, 2, f"{mod_id}_sand"),
    ("minecraft:gravel", 20, 2, f"{mod_id}_gravel"),
    ("adm2:any_dimensional_sand", 8, 4, f"{mod_id}_adm2_any_dimensional_sand"),
    ("adm2:any_dimensional_coal_ore", 8, 4, f"{mod_id}_adm2_any_dimensional_coal_ore"),
    ("adm2:any_dimensional_copper_ore", 8, 4, f"{mod_id}_adm2_any_dimensional_copper_ore"),
    ("adm2:any_dimensional_diamond_ore", 8, 4, f"{mod_id}_adm2_any_dimensional_diamond_ore"),
    ("adm2:any_dimensional_emerald_ore", 8, 4, f"{mod_id}_adm2_any_dimensional_emerald_ore"),
    ("adm2:any_dimensional_gold_ore", 8, 4, f"{mod_id}_adm2_any_dimensional_gold_ore"),
    ("adm2:any_dimensional_iron_ore", 8, 4, f"{mod_id}_adm2_any_dimensional_iron_ore"),
    ("adm2:any_dimensional_lapis_ore", 8, 4, f"{mod_id}_adm2_any_dimensional_lapis_ore"),
    ("adm2:any_dimensional_quartz_ore", 8, 4, f"{mod_id}_adm2_any_dimensional_quartz_ore"),
    ("adm2:any_dimensional_redstone_ore", 8, 4, f"{mod_id}_adm2_any_dimensional_redstone_ore"),
  ]
  featureNames = [ore[3] for ore in featureOres]
  featureNames.append("iceberg")

  biome_object = get_biome(featureNames)
  with open(f"data/adm2/worldgen/biome/common_{mod_id}.json", "w") as file:
    json.dump(biome_object, file, indent=2)
    print(f"Generated data/adm2/worldgen/biome/common_{mod_id}.json")

  for featureOre in featureOres:
    oreId = featureOre[0]
    size = featureOre[1]
    count = featureOre[2]
    name = featureOre[3]

    placed_feature = get_placed_feature(featureBlockIds, oreId, size, count)

    with open(f"data/adm2/worldgen/placed_feature/{name}.json", "w") as file:
      json.dump(placed_feature, file, indent=2)
      print(f"Generated data/adm2/worldgen/placed_feature/{name}.json")
