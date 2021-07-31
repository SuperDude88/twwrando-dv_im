
from collections import namedtuple

class zonePlug:
  def __init__(self,stage_name: str,room_num: int,scls_exit_index: int,spawn_id: int):
    self.stage_name = stage_name
    self.room_num = room_num
    self.scls_exit_index = scls_exit_index
    self.spawn_id = spawn_id

  def update_from_tuple(self,source):
    self.stage_name = source.stage_name
    self.room_num = source.room_num
    self.scls_exit_index = source.scls_exit_index
    self.spawn_id = source.spawn_id

# "stage_name room_num scls_exit_index spawn_id entrance_name island_name warp_out_stage_name warp_out_room_num warp_out_spawn_id"

class entrancePlug(zonePlug):
  def __init__(self,stage_name: str,room_num: int,scls_exit_index: int,spawn_id: int,entrance_name: str,island_name: str,warp_out_stage_name: str,warp_out_room_num: int,warp_out_spawn_id: int):
    super().__init__(stage_name,room_num,scls_exit_index,spawn_id)
    self.entrance_name = entrance_name
    self.island_name = island_name
    self.warp_out_stage_name = warp_out_stage_name
    self.warp_out_room_num = warp_out_room_num
    self.warp_out_spawn_id = warp_out_spawn_id

  def update_from_tuple(self,source):
    super().update_from_tuple(source)
    self.entrance_name = source.entrance_name
    self.island_name = source.island_name
    self.warp_out_stage_name = source.warp_out_stage_name
    self.warp_out_room_num = source.warp_out_room_num
    self.warp_out_spawn_id = source.warp_out_spawn_id

class exitPlug(zonePlug):
  def __init__(self,stage_name: str,room_num: int,scls_exit_index: int,spawn_id: int,zone_name: str,unique_name: str,inner_cave_stage):
    super().__init__(stage_name,room_num,scls_exit_index,spawn_id)
    self.zone_name = zone_name
    self.unique_name = unique_name
    if type(inner_cave_stage) == type(""):
      self.inner_cave_stage = [inner_cave_stage]
      self.boss_stage_name = inner_cave_stage
    elif type(inner_cave_stage) == type([]):
      self.inner_cave_stage = inner_cave_stage
      self.boss_stage_name = inner_cave_stage[0]
    else:
      self.inner_cave_stage =  None
      self.boss_stage_name = None

  def update_from_tuple(self,source):
    super().update_from_tuple(source)
    self.zone_name = source.zone_name
    self.unique_name = source.unique_name
    self.inner_cave_stage = source.inner_cave_stage
    self.boss_stage_name = source.inner_cave_stage


# "stage_name room_num scls_exit_index spawn_id entrance_name island_name warp_out_stage_name warp_out_room_num warp_out_spawn_id"

DUNGEON_ENTRANCES = [
  entrancePlug("Adanmae", 0, 2, 2, "Path to Valoo on Dragon Roost Island", "Dragon Roost Island", "sea", 13, 211),
  entrancePlug("sea", 41, 6, 6, "Tree Corpse near Forest Haven", "Forest Haven", "Omori", 0, 215),
  entrancePlug("sea", 26, 0, 2, "Foyer to Tower of the Gods", "Tower of the Gods", "sea", 26, 1),
  entrancePlug("Edaichi", 0, 0, 1, "Shrine to Laruto on Headstone Island", "Headstone Island", "sea", 45, 229),
  entrancePlug("Ekaze", 0, 0, 1, "Shrine to Fado on Gale Isle", "Gale Isle", "sea", 4, 232),
]
PUZZLE_CAVE_ENTRANCES = [
  # Note: For Fire Mountain and Ice Ring Isle, the spawn ID specified is on the sea with KoRL instead of being at the cave entrance, since the player would get burnt/frozen if they were put at the entrance while the island is still active.
  entrancePlug("sea", 20, 0, 0, "Crater on Fire Mountain", "Fire Mountain", "sea", 20, 0),
  entrancePlug("sea", 40, 0, 0, "Palsa on Ice Ring Isle", "Ice Ring Isle", "sea", 40, 0),
  entrancePlug("Abesso", 0, 0, 1, "Hearth on Private Oasis", "Private Oasis", "Abesso", 0, 1),
  entrancePlug("sea", 29, 0, 5, "Frozen-Over Pit on Needle Rock Isle", "Needle Rock Isle", "sea", 29, 5),
  entrancePlug("sea", 47, 1, 5, "Hole in Angular Isles", "Angular Isles", "sea", 47, 5),
  entrancePlug("sea", 35, 0, 1, "Drop Behind Bars on Bird's Peak Rock", "Bird's Peak Rock", "sea", 35, 1),
  entrancePlug("sea", 36, 0, 1, "Geo on Diamond Steppe Island", "Diamond Steppe Island", "sea", 36, 1),
  entrancePlug("sea", 42, 0, 2, "Inlet on Cliff Plateau Isles", "Cliff Plateau Isles", "sea", 42, 2)
]
MIXED_CAVE_ENTRANCES = [
  entrancePlug("sea", 48, 0, 5, "Firth on Boating Course", "Boating Course", "sea", 48, 5),
  entrancePlug("sea", 12, 0, 1, "Cave Opening in Shell on Pawprint Isle", "Pawprint Isle", "sea", 12, 1),
  entrancePlug("sea", 34, 0, 1, "Crater on Bomb Island", "Bomb Island", "sea", 34, 1)
]
COMBAT_CAVE_ENTRANCES = [
  entrancePlug("sea", 44, 8, 10, "Covered Opening on Outset Island", "Outset Island", "sea", 44, 10),
  entrancePlug("sea", 13, 2, 5, "Buried Pit on Dragon Roost Island", "Dragon Roost Island", "sea", 13, 5),
  entrancePlug("sea", 31, 0, 1, "Sheltered Hole on Stone Watcher Island", "Stone Watcher Island", "sea", 31, 1),
  entrancePlug("sea", 7, 0, 1, "Geo on Overlook Island", "Overlook Island", "sea", 7, 1),
  entrancePlug("sea", 12, 1, 5, "Side Isle Inlet on Pawprint Isle", "Pawprint Isle", "sea", 12, 5),
  entrancePlug("sea", 16, 0, 1, "Drop on Rock Spire Isle", "Rock Spire Isle", "sea", 16, 1),
  entrancePlug("sea", 38, 0, 5, "Protected Entry on Shark Island", "Shark Island", "sea", 38, 5),
  entrancePlug("sea", 43, 0, 5, "Firth on Horseshoe Island", "Horseshoe Island", "sea", 43, 5),
  entrancePlug("sea", 2, 0, 1, "Cave Opening on Star Island", "Star Island", "sea", 2, 1)
]

FAIRY_ENTRANCES = [
  entrancePlug("sea", 3, 0, 1, "Northern Fairy Conch", "Northern Fairy Island", "sea", 3, 1),
  entrancePlug("sea", 19, 0, 1, "Eastern Fairy Conch", "Eastern Fairy Island", "sea", 19, 1),
  entrancePlug("sea", 15, 0, 1, "Western Fairy Conch", "Western Fairy Island", "sea", 15, 1),
  entrancePlug("A_mori", 0, 0, 2, "Hole in the Forest of Fairies", "Outset Island", "A_mori", 0, 2),
  entrancePlug("sea", 28, 0, 1, "Thorned Fairy Conch", "Thorned Fairy Island", "sea", 28, 1),
  entrancePlug("sea", 39, 0, 1, "Southern Fairy Conch", "Southern Fairy Island", "sea", 39, 1),
]

SECRET_CAVE_ENTRANCES = PUZZLE_CAVE_ENTRANCES + MIXED_CAVE_ENTRANCES + COMBAT_CAVE_ENTRANCES + FAIRY_ENTRANCES


# "stage_name room_num scls_exit_index spawn_id zone_name unique_name boss_stage_name"

DUNGEON_EXITS = [
  exitPlug("M_NewD2", 0, 0, 0, "Dragon Roost Cavern", "Dragon Roost Cavern", "M_DragB"),
  exitPlug("kindan", 0, 0, 0, "Forbidden Woods", "Forbidden Woods", "kinBOSS"),
  exitPlug("Siren", 0, 1, 0, "Tower of the Gods", "Tower of the Gods", "SirenB"),
  exitPlug("M_Dai", 0, 0, 0, "Earth Temple", "Earth Temple", "M_DaiB"),
  exitPlug("kaze", 15, 0, 15, "Wind Temple", "Wind Temple", "kazeB"),
]
PUZZLE_CAVE_EXITS = [
  exitPlug("MiniKaz", 0, 0, 0, "Fire Mountain", "Fire Mountain Secret Cave", None),
  exitPlug("MiniHyo", 0, 0, 0, "Ice Ring Isle", "Ice Ring Isle Secret Cave", None),
  exitPlug("TF_04", 0, 0, 0, "Private Oasis", "Cabana Labyrinth", None),
  exitPlug("SubD42", 0, 0, 0, "Needle Rock Isle", "Needle Rock Isle Torches Cave", None),
  exitPlug("SubD43", 0, 0, 0, "Angular Isles", "Angular Isles Light Puzzle Cave", None),
  exitPlug("TF_03", 0, 0, 0, "Bird's Peak Rock", "Bird's Peak Rock Secret Cave", None),
  exitPlug("WarpD", 0, 0, 0, "Diamond Steppe Island", "Diamond Steppe Island Warp Maze Cave", None),
  exitPlug("Cave03", 0, 0, 0, "Cliff Plateau Isles", "Cliff Plateau Isles Floating Plants Cave", None)
]
MIXED_CAVE_EXITS = [
  exitPlug("SubD71", 0, 0, 0, "Boating Course", "Boating Course Diamond Switches Cave", None),
  exitPlug("TyuTyu", 0, 0, 0, "Pawprint Isle", "Pawprint Isle Chuchu Cave", None),
  exitPlug("Cave01", 0, 0, 0, "Bomb Island", "Bomb Island Magtail Cave", None)
]
COMBAT_CAVE_EXITS = [
  exitPlug("Cave09", 0, 1, 0, "Outset Island", "Savage Labyrinth", None),
  exitPlug("TF_06", 0, 0, 0, "Dragon Roost Island", "Dragon Roost Island Mysterious Cave", None),
  exitPlug("TF_01", 0, 0, 0, "Stone Watcher Island", "Stone Watcher Island Combat Trial", None),
  exitPlug("TF_02", 0, 0, 0, "Overlook Island", "Overlook Island Combat Trial", None),
  exitPlug("Cave07", 0, 0, 0, "Pawprint Isle", "Pawprint Isle Wizzrobe Cave", None),
  exitPlug("Cave04", 0, 0, 0, "Rock Spire Isle", "Rock Spire Isle Keese Cave", None),
  exitPlug("ITest63", 0, 0, 0, "Shark Island", "Shark Island Enemy Hell Cave", None),
  exitPlug("Cave05", 0, 0, 0, "Horseshoe Island", "Horseshoe Island Mothula Cave", None),
  exitPlug("Cave02", 0, 0, 0, "Star Island", "Star Island Combat Cave", None)
]

FAIRY_EXITS = [
  exitPlug("Fairy01", 0, 0, 0, "Northern Fairy Island", "Northern Fairy Fountain", None),
  exitPlug("Fairy02", 0, 0, 0, "Eastern Fairy Island", "Eastern Fairy Fountain", None),
  exitPlug("Fairy03", 0, 0, 0, "Western Fairy Island", "Western Fairy Fountain", None),
  exitPlug("Fairy04", 0, 0, 0, "Outset Island", "Forest of Fairies Fountain", None),
  exitPlug("Fairy05", 0, 0, 0, "Thorned Fairy Island", "Thorned Fairy Fountain", None),
  exitPlug("Fairy06", 0, 0, 0, "Southern Fairy Island", "Southern Fairy Fountain", None),
]

SECRET_CAVE_EXITS = PUZZLE_CAVE_EXITS + MIXED_CAVE_EXITS + COMBAT_CAVE_EXITS + FAIRY_EXITS

DUNGEON_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS = [
  "Path to Valoo on Dragon Roost Island",
]
SECRET_CAVE_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS = [
  "Cave Opening in Shell on Pawprint Isle",
  "Inlet on Cliff Plateau Isles",
]
FAIRY_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS = [
  "Northern Fairy Conch"
]

DUNGEON_EXIT_NAMES_WITH_NO_REQUIREMENTS = [
  "Dragon Roost Cavern",
  "Forbidden Woods",
  "Tower of the Gods"
]
PUZZLE_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS = [
  "Ice Ring Isle Secret Cave",
  "Diamond Steppe Island Warp Maze Cave"
]
MIXED_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS = [
  "Pawprint Isle Chuchu Cave"
]
COMBAT_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS = [
  "Rock Spire Isle Keese Cave"
]
SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS = PUZZLE_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS + MIXED_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS + COMBAT_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS
FAIRY_EXIT_NAMES_WITH_NO_REQUIREMENTS = [
  "Northern Fairy Fountain"
  "Eastern Fairy Fountain",
  "Western Fairy Fountain",
  "Forest of Fairies Fountain",
  "Thorned Fairy Fountain",
  "Southern Fairy Fountain"
]
