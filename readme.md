# ![](pack.png) Any Dimension Mod 2 Data Pack Expansion

![Preview Screenshot](images/preview.jpg)

- `Mod:` Luxore
- `Expansion Author:` luxmiyu

## Developer Guide

This repo uses blocks from [Luxore](https://github.com/luxmiyu/luxore)
as an example data pack expansion for [Any Dimension Mod 2](https://github.com/luxmiyu/adm2).
The data pack would be called `Any Dimension Mod 2 - Luxore` in this case.

Follow these instructions you'd like to create your own data pack expansion for Any Dimension Mod 2.

- Open `pack.mcmeta` and edit the fields.
  - Make sure to choose a compatible `"pack_format"` for the Minecraft version you're targetting.
    See [Pack Format](https://minecraft.wiki/w/Pack_format) for more information.
  - Give it an appropriate `"description"`.
- Open `python/data.json` and edit the fields.
  -  `mod_id`: The mod you intend to create dimensions for.
  -  `block_ids`: The blocks you want to create dimensions for, without their mod id.
- Run `python/start.bat`. You must have Python installed on your machine.

The python scripts will take care of generating all of the important json files for the data pack.

## Debug Wand

Any Dimension Mod 2 includes many wands to use in Creative Mode for demonstration purposes,
you can use the Debug Wand to help you find suitable blocks!

![Any Dimensional Debug Wand](images/debug_wand.png)

When used on a block, the wand will identify the mod that block belongs to, and then print out
to the console the list of "full cube" blocks from that mod. Use while sneaking to print out
the entire list of blocks from that mod.

## As a Mod (for any Mod Loader)

You can convert this data pack into a proper mod by simply including the `data/` folder into
the `resources/` folder of your mod project. This requires some minimum modding knowledge, check your mod loader's instructions on how to get started!

If you use Fabric, please add this entry into your `fabric.mod.json` file to display Any Dimension Mod 2 as
a parent in [ModMenu](https://github.com/TerraformersMC/ModMenu), as well as add it as a dependency.

```js
"depends": {
  // ...
  "adm2": "*"
},
"suggests": {
  "modmenu": "*",
  "immersive_portals": "*"
},
"custom": {
  "modmenu": {
    "parent": "adm2"
  }
}
```

You can view [Any Dimension Mod 2 - Luxore](https://github.com/luxmiyu/adm2-luxore)
as an example of how it could be done!
