import json

def get_dimension(mod_id, dimension_id):
  dimension = {
    "type": "adm2:common",
    "generator": {
      "type": "minecraft:noise",
      "settings": f"adm2:{dimension_id}",
      "biome_source": {
        "type": "minecraft:fixed",
        "biome": f"adm2:common_{mod_id}"
      }
    }
  }

  return dimension

def run(mod_id, block_ids):
  for block_id in block_ids:
    dimension_id = f"{mod_id}__{block_id}"
    dimension = get_dimension(mod_id, dimension_id)
    file_path = f"data/adm2/dimension/{dimension_id}.json"

    with open(file_path, "w") as file:
      json.dump(dimension, file, indent=2)
      print(f"Generated {file_path}")
