"""
Reference Object for items

Item Properties
Item.Name      : str
Item.Owned     : bool
Item.Checks    : ItemLocation list


Functions

get_checks() -> ItemLocation list
add_check(ItemLocation:check) -> void
item_set() -> void
"""


class Item:
  def __init__(self, str:Name):
    self.Name = Name
    self.Owned = False
    self.locations = list()

  def get_locations(self):
    return self.locations

  def add_check(self, check):
    self.locations.append(check)

  def item_set(self):
    self.Owned = True
    for location in self.locations:
        location.item_received(self.Name)
