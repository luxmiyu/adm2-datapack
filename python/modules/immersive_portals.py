import json

def immersive_portal_from_dimensions(dimension_ids = [], exclude = [], add_vanilla = True):
  from_dimensions = [
    "minecraft:overworld",
    "minecraft:the_nether",
    "minecraft:the_end"
  ] if add_vanilla else []

  for dimension_id in dimension_ids:
    if dimension_id not in exclude:
      from_dimensions.append(f"adm2:{dimension_id}")

  return from_dimensions

def get_to(dimension_id, block_id, dimension_ids = [], add_vanilla = True):
  immersive_portal = {
    "schema_version": "imm_ptl:v1",
    "from": immersive_portal_from_dimensions(dimension_ids, [dimension_id], add_vanilla),
    "to": f"adm2:{dimension_id}",
    "form": {
      "type": "imm_ptl:classical",
      "from_frame_block": f"{block_id}",
      "area_block": "minecraft:air",
      "to_frame_block": f"{block_id}",
      "generate_frame_if_not_found": True
    },
    "trigger": {
      "type": "imm_ptl:use_item",
      "item": "adm2:any_dimensional_portal_wand"
    }
  }

  return immersive_portal

def get_from(dimension_id, block_id):
  immersive_portal = {
    "schema_version": "imm_ptl:v1",
    "from": [
      f"adm2:{dimension_id}"
    ],
    "to": "minecraft:overworld",
    "form": {
      "type": "imm_ptl:classical",
      "from_frame_block": f"{block_id}",
      "area_block": "minecraft:air",
      "to_frame_block": f"{block_id}",
      "generate_frame_if_not_found": True
    },
    "trigger": {
      "type": "imm_ptl:use_item",
      "item": "adm2:any_dimensional_portal_wand"
    }
  }

  return immersive_portal

def run(mod_id, block_ids):
  with open("./python/modules/base.json", "r") as file:
    base_dimensions = json.load(file)
    mod_dimension_ids = [f"{mod_id}__{block_id}" for block_id in block_ids]

    dimension_ids = base_dimensions + mod_dimension_ids

    # create portals to mod dimensions
    for block_id in block_ids:
      from_object = get_from(f"{mod_id}__{block_id}", f"{mod_id}:{block_id}")
      to_object = get_to(f"{mod_id}__{block_id}", f"{mod_id}:{block_id}", dimension_ids)

      from_file_path = f"data/adm2/custom_portal_generation/{mod_id}__{block_id}_from.json"
      to_file_path = f"data/adm2/custom_portal_generation/{mod_id}__{block_id}_to.json"

      with open(from_file_path, "w") as file:
        json.dump(from_object, file, indent=2)
        print(f"Generated {from_file_path}")

      with open(to_file_path, "w") as file:
        json.dump(to_object, file, indent=2)
        print(f"Generated {to_file_path}")

    # create portals from base dimensions to mod dimensions
    for base_dimension in base_dimensions:
      base_block_namespace = base_dimension.split("__")[0]
      base_block_path = base_dimension.split("__")[1]
      base_block_id = f"{base_block_namespace}:{base_block_path}"

      to_object = get_to(base_dimension, base_block_id, mod_dimension_ids, False)
      to_file_path = f"data/adm2/custom_portal_generation/{base_dimension}_to_from_{mod_id}.json"

      with open(to_file_path, "w") as file:
        json.dump(to_object, file, indent=2)
        print(f"Generated {to_file_path}")
