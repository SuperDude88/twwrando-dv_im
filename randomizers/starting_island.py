
import tweaks
from class_creator.class_ms import YamlOrderedDictLoader

import os
from paths import DATA_PATH
import yaml
from collections import OrderedDict

def randomize_starting_island(self):
  possible_starting_islands = list(range(1, 49+1))

  limited_movement = 0
  limiting_items = [ "Wind Waker", "Ballad of Gales", "Boat's Sail", "Wind's Requiem" ]
  for item in limiting_items:
    if item not in self.starting_items:
      limited_movement += 1

  # Don't allow Forsaken Fortress to be the starting island.
  # It wouldn't really cause problems, but it would be weird because you normally need bombs to get in, and you would need to use Ballad of Gales to get out.

  limit_possible_island = [
    [1],
    [2,4,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,45,46,48,49],
    [47],
    [3,6],
    [5]
  ]

  for limit_list in limit_possible_island[0:limited_movement+1]:
    for island_index in limit_list:
      possible_starting_islands.remove(island_index)

  while True:
    starting_island_room_index = self.rng.choice(possible_starting_islands)
    if(self.banned_island_locales[starting_island_room_index-1]):
      break
    else:
      continue

  if not self.dry_run:
    tweaks.set_new_game_starting_room_index(self, starting_island_room_index)
    tweaks.change_ship_starting_island(self, starting_island_room_index)

  self.starting_island_index = starting_island_room_index
  #print(str(starting_island_room_index))
  return starting_island_room_index

def get_starting_island(self,starting_island_room_index):
  if True:
    bad_index = OrderedDict()
    bad_index[9] = "Child Isle"

  with open(os.path.join(DATA_PATH, "island_data.txt")) as f:
    island_data = yaml.load(f, YamlOrderedDictLoader)

  starting_island_name = island_data[starting_island_room_index]["Long Name"]
  neighbor_index = (island_data[starting_island_room_index]["Neighbors"]).split(", ")
  island_macro = "Can Travel to {}".format(starting_island_name)
  req_string = "Nothing"
  self.set_macro(island_macro, req_string)
  req_string = "| ({} & Can Sail)".format(island_macro)
  req_data = self.parse_logic_expression(req_string)

  for neighbor in neighbor_index:
    if neighbor in bad_index:
      neighbor_name = bad_index[int(neighbor)]
    else:
      neighbor_name = island_data[int(neighbor)]["Long Name"]
    island_macro = "Can Travel to {}".format(neighbor_name)

    req_new = self.macros[island_macro]
    for data in req_data:
      req_new.append(data)
    self.macros[island_macro] = req_new
  #print(str(starting_island_room_index))
