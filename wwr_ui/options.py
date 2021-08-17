
from collections import OrderedDict

MAXIMUM_ADDITIONAL_STARTING_ITEMS = 47

OPTIONS = OrderedDict([
  (
    "progression_dungeons",
    "This controls whether dungeons can contain progress items.<br><u>If this is not checked, dungeons will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_puzzle_secret_caves",
    "This controls whether puzzle-focused secret caves can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_mixed_secret_caves",
    "This controls whether secret caves that use both puzzle and combat elements can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_combat_secret_caves",
    "This controls whether combat-focused secret caves can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_tingle_chests",
    "This controls whether checks in strange dungeons locations can contain progress items [and some must be bombed to make them appear]. (2[2] in DRC, 6[2] in FW, 1[1] in TOTG, 3[1] in ET, and 4[1] in WT)<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_great_fairies",
    "This controls whether the items given by Great Fairies can be progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_island_puzzles",
    "This controls whether various island puzzles can contain progress items (e.g. chests hidden in unusual places).<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_long_combat_trials",
    "This controls whether various long combat checks can contain progress items (e.g. Savage Labyrinth, Orca 500-hits, etc.).<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_short_sidequests",
    "This controls whether sidequests that can be completed quickly can reward progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only reward optional items you don't need to beat the game."
  ),
  (
    "progression_long_sidequests",
    "This controls whether long sidequests (e.g. Lenzo's assistant, withered trees, goron trading) can reward progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only reward optional items you don't need to beat the game."
  ),
  (
    "progression_spoils_trading",
    "This controls whether the items you get by trading in spoils to NPCs can be progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only reward optional items you don't need to beat the game."
  ),
  (
    "progression_platforms_rafts",
    "This controls whether lookout platforms and rafts can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_short_minigames",
    "This controls whether most minigames can reward progress items (cheaper auctions, mail sorting, etc.).<br><u>If this is not checked, minigames will still be randomized</u>, but will only reward optional items you don't need to beat the game."
  ),
  (
    "progression_long_minigames",
    "This controls whether most minigames can reward progress items (Orca 500-hits, bird-man contest, etc.).<br><u>If this is not checked, minigames will still be randomized</u>, but will only reward optional items you don't need to beat the game."
  ),
  (
    "progression_expensive_purchases",
    "This controls whether items that cost a lot of rupees can be progress items (Rock Spire shop, auctions, Tingle's letter, trading quest).<br><u>If this is not checked, they will still be randomized</u>, but will only be optional items you don't need to beat the game."
  ),
  (
    "progression_big_octos_gunboats",
    "This controls whether the items dropped by Big Octos and Gunboats can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_submarines",
    "This controls whether submarines can contain progress items.<br><u>If this is not checked, submarines will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_free_gifts",
    "This controls whether gifts freely given by NPCs can be progress items (Tott, Salvage Corp, imprisoned Tingle).<br><u>If this is not checked, they will still be randomized</u>, but will only be optional items you don't need to beat the game."
  ),
  (
    "progression_eye_reef_chests",
    "This controls whether the chests that appear after clearing out the eye reefs can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_triforce_charts",
    "This controls whether the sunken treasure chests marked on Triforce Charts can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_treasure_charts",
    "This controls whether the sunken treasure chests marked on Treasure Charts can contain progress items.<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "progression_misc",
    "Miscellaneous locations that don't fit into any of the above categories (outdoors chests, wind shrine, Cyclos, etc).<br><u>If this is not checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),


  (
    "keymode",
    "Sets where dungeon keys can appear in the game."
  ),
  (
    "randomize_entrances",
    "Shuffles around which dungeon entrances/secret cave entrances take you into which dungeons/secret caves.\n(No effect on Forsaken Fortress or Ganon's Tower.)"
  ),
  (
    "randomize_charts",
    "Randomizes which sector is drawn on each Triforce/Treasure Chart."
  ),
  (
    "randomize_starting_island",
    "Randomizes which island you start the game on."
  ),


  (
    "locale_drc",
    "Disables all item locations in Dragon Roost Cavern.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_deep_drc",
    "Disables all item locations deep inside Dragon Roost Cavern.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_fw",
    "Disables all item locations in Forbidden Woods.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_deep_fw",
    "Disables all item locations deep inside Forbidden Woods.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_totg",
    "Disables all item locations in or around Tower of the Gods.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_deep_totg",
    "Disables all item locations deep inside Tower of the Gods.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_ff",
    "Disables all item locations in or around Forsaken Fortress.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_et",
    "Disables all item locations in Earth Temple.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_deep_et",
    "Disables all item locations deep inside Earth Temple.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_wt",
    "Disables all item locations in Wind Temple.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_deep_wt",
    "Disables all item locations deep inside Wind Temple.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),

  (
    "locale_star",
    "Disables all item locations in or around Star Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_northern_fairy",
    "Disables all item locations in or around Northern Fairy Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_gale",
    "Disables all item locations in or around Gale Isle.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_crescent",
    "Disables all item locations in or around Crescent Moon Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_seven_star",
    "Disables all item locations in or around Seven-Star Isles.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_overlook",
    "Disables all item locations in or around Overlook Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_four_eye",
    "Disables all item locations in or around Four-Eye Reef.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_mother_child",
    "Disables all item locations in or around Mother and Child Isles.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_spectacle",
    "Disables all item locations in or around Spectacle Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_windfall",
    "Disables all item locations in or around Windfall Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_pawprint",
    "Disables all item locations in or around Pawprint Isle.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_dragon_roost_island",
    "Disables all item locations in or around Dragon Roost Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_flight_control",
    "Disables all item locations in or around Flight Control Platform.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_western_fairy",
    "Disables all item locations in or around Western Fairy Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_rock_spire",
    "Disables all item locations in or around Rock Spire Isle.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_tingle",
    "Disables all item locations in or around Tingle Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_northern_triangle",
    "Disables all item locations in or around Northern Triangle Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_eastern_fairy",
    "Disables all item locations in or around Eastern Fairy Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_fire_mountain",
    "Disables all item locations in or around Fire Mountain.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_star_belt",
    "Disables all item locations in or around Star Belt Archipelago.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_three_eye",
    "Disables all item locations in or around Three-Eye Reef.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_greatfish",
    "Disables all item locations in or around Greatfish Isle.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_cyclops",
    "Disables all item locations in or around Cyclops Reef.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_six_eye",
    "Disables all item locations in or around Six-Eye Reef.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_eastern_triangle",
    "Disables all item locations in or around Eastern Triangle Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_thorned_fairy",
    "Disables all item locations in or around Thorned Fairy Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_needle_rock",
    "Disables all item locations in or around Needle Rock Isle.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_islet",
    "Disables all item locations in or around Islet of Steel.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_stone_watcher",
    "Disables all item locations in or around Stone Watcher Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_southern_triangle",
    "Disables all item locations in or around Southern Triangle Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_private_oasis",
    "Disables all item locations in or around Private Oasis.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_bomb",
    "Disables all item locations in or around Bomb Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_birds_peak",
    "Disables all item locations in or around Bird's Peak Rock.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_diamond_steppe",
    "Disables all item locations in or around Diamond Steppe Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_five_eye",
    "Disables all item locations in or around Five-Eye Reef.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_shark",
    "Disables all item locations in or around Shark Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_southern_fairy",
    "Disables all item locations in or around Southern Fairy Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_ice_ring",
    "Disables all item locations in or around Ice Ring Isle.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_forest_haven",
    "Disables all item locations in or around Forest Haven.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_cliff_plateau",
    "Disables all item locations in or around Cliff Plateau Isles.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_horseshoe",
    "Disables all item locations in or around Horseshoe Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_outset",
    "Disables all item locations in or around Outset Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_headstone",
    "Disables all item locations in or around Headstone Island.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),

  (
    "locale_two_eye",
    "Disables all item locations in or around Two-Eye Reef.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_angular",
    "Disables all item locations in or around Angular Isle.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_boating_course",
    "Disables all item locations in or around Boating Course.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_five_star",
    "Disables all item locations in or around Five-Star Isles.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),


  (
    "locale_great_sea",
    "Disables all item locations without a single map location.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_under_great_sea",
    "Disables all item locations in Hyrule Castle or the Gerudo Desert.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_battlesquid",
    "Disables all item locations associated with Battlesquids/Sploosh Kaboom.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_savage",
    "Disables all item locations in Savage Labyrinth.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_mail",
    "Disables all item locations in the mailbox.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_picto",
    "Disables all item locations that require Picto Box usage.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),
  (
    "locale_dvim",
    "Disables all item locations added in dv_im.<br><u>If this is checked, they will still be randomized</u>, but will only contain optional items you don't need to beat the game."
  ),


  (
    "swift_sail",
    "Sailing speed is doubled and the direction of the wind is always at your back as long as the sail is out."
  ),
  (
    "instant_text_boxes",
    "Text appears instantly.<br>Also, the B button is changed to instantly skip through text as long as you hold it down."
  ),
  (
    "reveal_full_sea_chart",
    "Start the game with the sea chart fully drawn out."
  ),
  (
    "num_starting_triforce_shards",
    "Change the number of Triforce Shards you start the game with.<br>The higher you set this, the fewer you will need to find placed randomly."
  ),
  (
    "add_shortcut_warps_between_dungeons",
    "Adds new warp pots that act as shortcuts connecting dungeons to each other directly. (DRC, FW, TotG, and separately FF, ET, WT.)\nEach pot must be unlocked before it can be used, so you cannot use them to access dungeons you wouldn't already have access to."
  ),

  (
    "sword_mode",
    "Controls whether you start with the Hero's Sword, without a sword, or if there is no sword in the entire game.\nSwordless and No Starting Sword are challenge modes, not recommended for your first run.\nFF's Phantom Ganon is vulnerable to Skull Hammer in Swordless mode only."
  ),
  (
    "skip_rematch_bosses",
    "Removes the door in Ganon's Tower that only unlocks when you defeat the rematch versions of Gohma, Kalle Demos, Jalhalla, and Molgera."
  ),
  (
    "invert_camera_x_axis",
    "Inverts the horizontal axis of camera movement.",
  ),
  (
    "race_mode",
    "For Dungeon Modes other than Default, random dungeon bosses will drop required items (e.g. Triforce Shards). In Race Mode, nothing in the other dungeons will ever be required.\nYou can see which islands have the required dungeons on them by which islands have blue quest markers on the sea chart.",
  ),
  (
    "num_dungeon_race_mode",
    "Effects the number of dungeons the player will have to complete if Race Mode is enabled."
  ),
  (
    "compass_map_pool_with_keys",
    "If enabled, the unhad dungeon maps and compasses will be included in items to find for dungeon completion like a small or big key.\nOtherwise, it will be placed like any other unique non-progressive items."
  ),

  (
    "generate_spoiler_log",
    "Generates a text file listing included seed details. (This being checked also changes where items are placed in this seed.)<br/><u>Highly recommended even if use is not intended</u>, in case of self-locking."
  ),
  (
    "progression_check_spoiler_log",
    "Generates a playthrough as part of the spoiler log.<br/><u>Highly recommended even if use is not intended</u>, in case of self-locking."
  ),
  (
    "all_check_spoiler_log",
    "Generates a list of all check locations as part of the spoiler log.<br/><u>Highly recommended even if use is not intended</u>, in case of self-locking."
  ),
  (
    "entrance_spoiler_log",
    "Generates a list of entrance locations as part of the spoiler log.<br/><u>Highly recommended even if use is not intended</u>, in case of self-locking."
  ),
  (
    "chart_spoiler_log",
    "Generates a list of chart locations as part of the spoiler log.<br/><u>Highly recommended even if use is not intended</u>, in case of self-locking."
  ),


  (
    "logic_mod",
    "Changes logic to reflect skill level by introducing tricks.\nFor further details, look in './logic_types/About Logic Types.txt'."
  ),
  (
    "convenience_option",
    "Adds extra items to the pool.\nConvenience includes Quiver, Hurricane Spin, etc. Plentiful adds an extra of each progressive item."
  ),


  (
    "randomize_music",
    "Shuffles around all the music in the game. This affects background music, combat music, fanfares, etc.<br>At this time, this may cause issues that could serverely impact player enjoyment.",
  ),
  (
    "disable_tingle_chests_with_tingle_bombs",
    "This prevents the Tingle Tuner's bombs from revealing Tingle Chests, meaning the only way to access these chests is to find the normal bombs item.\n(The randomizer makes normal bombs work on Tingle Chests regardless of this option.)",
  ),
  (
    "randomize_enemy_palettes",
    "Gives all the enemies in the game random colors.",
  ),
  (
    "remove_title_and_ending_videos",
    "Removes the two prerendered videos that play if you wait on the title screen and after you beat the game. (Decreases randomized ISO's filesize by about 600MB.)\nIf you keep these videos in, they won't reflect your custom player model or colors.",
  ),
  (
    "can_chain_charts",
    "Allow Treasure Charts to appear in Sunken Treasure.\nThis may produce chains of Treasure Charts."
  ),


  (
    "custom_player_model",
    "Replaces Link's model with a custom player model.\nThese are loaded from the /models folder."
  ),
  (
    "player_in_casual_clothes",
    "Enable this if you want to wear your casual clothes instead of the Hero's Clothes."
  ),
  (
    "disable_custom_player_voice",
    "If the chosen custom model comes with custom voice files, you can check this option to turn them off and simply use Link's normal voice instead."
  ),
  (
    "disable_custom_player_items",
    "If the chosen custom model comes with custom item models, you can check this option to turn them off and simply use Link's normal item models instead."
  ),
  (
    "disable_custom_boat",
    "If the chosen custom model comes with a custom boat model, you can check this option to turn it off and simply use the regular King of Red Lions."
  ),
  (
    "sail_color",
    "Selects sail to use in game."
  ),
  (
    "custom_bck_entry",
    "Selects animation deviation. May effect gameplay."
  ),
  (
    "custom_color_preset",
    "This allows you to select from preset color combinations chosen by the author of the selected player model."
  ),
  (
    "randomized_gear",
    "Inventory items that will be randomized."
  ),
  (
    "starting_gear",
    "Items that will be in Link's inventory at the start of a new game."
  ),
  (
    "additional_starting_min",
    "The minimum random items that will be in Link's inventory at the start of a new game."
  ),
  (
    "additional_starting_max",
    "The maximum random items that will be in Link's inventory at the start of a new game."
  ),
  (
    "starting_pohs",
    "Amount of extra pieces of heart that you start with."
  ),
  (
    "starting_hcs",
    "Amount of extra heart containers that you start with."
  ),
  (
    "starting_bh",
    "Amount of base hearts the player has.\nThis will effect full completion by reducing the total heart count."
  ),
  (
    "no_heart_in_pool",
    "Additional health pieces and containers do not appear in item pool."
  ),
  (
    "remove_music",
    "Mutes all ingame music."
  ),
  (
    "randomize_enemies",
    "Randomizes the placement of non-boss enemies."
  ),
  (
    "silver_membership_points",
    "Sets the number of points you need to get Beedle's silver membership."
  ),
  (
    "gold_membership_points",
    "Sets the number of points you need to get Beedle's gold membership."
  ),
  (
    "randomize_membership_points",
    "Randomizes the placement of non-boss enemies."
  ),
])

NON_PERMALINK_OPTIONS = [
  "invert_camera_x_axis",
  "custom_player_model",
  "player_in_casual_clothes",
  "disable_custom_player_voice",
  "disable_custom_player_items",
  "disable_custom_boat",
  "sail_color",
  "custom_color_preset",
  "remove_title_and_ending_videos",
  # Note: Options that affect music must be included in the permalink because music duration affects gameplay in some cases, like not being allowed to close the item get textbox until the item get jingle has finished playing.
  # Note: randomize_enemy_palettes has special logic to be in the permalink when enemy rando is on, but otherwise just have an unused placeholder in the permalink.
]

HIDDEN_OPTIONS = [
  "disable_tingle_chests_with_tingle_bombs",
  "randomize_enemies",
  "custom_bck_entry",
]

POTENTIALLY_UNBEATABLE_OPTIONS = [
  "randomize_enemies",
]
