import json

import generate

def main():
  with open("./python/data.json", "r") as file:
    data = json.load(file)

    MOD_ID = data["mod_id"]
    BLOCK_IDS = data["block_ids"]

    generate.run(MOD_ID, BLOCK_IDS)

if __name__ == "__main__":
  main()
