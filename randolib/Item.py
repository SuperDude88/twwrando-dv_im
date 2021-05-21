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
    self.Checks = list()

  def get_checks(self):
    return self.Checks

  def add_check(self, check):
    self.Checks.append(check)

  def item_set(self):
    self.Owned = True
    for check in self.Checks:
        check.item_received(self.Name)
