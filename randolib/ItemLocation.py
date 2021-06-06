"""
The Check itself. It can reference it's own Location/Locale (To know if it's
banned) it's own logic, and then the item it has.

ItemLocation Properties

ItemLocation.LocationName     : str
ItemLocation.LocationLocale   : Location
ItemLocation.Item             : str
ItemLocation.Path             : str
ItemLocation.Sphere           : int
ItemLocation.__LocationLogic  : Logic

Functions

set_check_item(str:item_name, int:sphere) -> void
get_accessiblity() -> bool
required_progression() -> str list
item_received(str:item_name) -> void
"""
from Location import Location as Location

class ItemLocation(Location):

  def __init__(self, str:LocationName, str:LocationLocale, str:Path,
               str:LogicString):
    self.LocationLocale = LocationLocale
    self.Item = ""
    self.Path = Path
    self.Sphere = -1
    Location.__init__(self,LocationName,LogicString)

  def set_check_item(self, str:item_name, int:sphere) -> void:
    self.Item = item_name
    self.Sphere = sphere

  def get_accessibilty(self) -> bool:
    return self.logic.accessible

  def required_progression(self):
    return self.logic.get_item_list()

  def item_received(self, str:item_name, int:sphere) -> void:
    self.Sphere = Sphere
    if not self.logic.accessible:
      return
    else:
      self.logic.add_item(item_name)
