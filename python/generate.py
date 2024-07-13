#
#  generate.py
#
#  This python script generates the JSON files for the following folders:
#  - data/adm2/dimension/
#  - data/adm2/worldgen/noise_settings/
#  - data/adm2/custom_portal_generation/
#  - data/adm2/worldgen/placed_feature/
#  - data/adm2/worldgen/biome/
#
#  The run() function is intended to be called from "python/main.py".
#

import json
import os

from modules import biome_ores, noise_settings, dimensions, immersive_portals

def empty_directories():
  directories = [
    "data/adm2/worldgen/biome/",
    "data/adm2/worldgen/placed_feature/",
    "data/adm2/custom_portal_generation/",
    "data/adm2/worldgen/noise_settings/",
    "data/adm2/dimension/",
  ]

  delete_count = 0

  for directory in directories:
    for file in os.listdir(directory):
      os.remove(f"{directory}{file}")
      delete_count += 1

  print(f"Deleted {delete_count} files.")

def run(mod_id, block_ids):
  empty_directories()

  biome_ores.run(mod_id, block_ids)
  noise_settings.run(mod_id, block_ids)
  dimensions.run(mod_id, block_ids)
  immersive_portals.run(mod_id, block_ids)
