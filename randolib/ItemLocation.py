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

class ItemLocation:

  def __init__(self, str:LocationName, str:LocationLocale, str:Path,
               str:LogicString):

    self.LocationName = LocationName
    self.LocationLocale = LocationLocale
    self.Item = ""
    self.Path = Path
    self.Sphere = -1
    #self.__LocationLogic = ItemLogic(LogicString)

  def set_check_item(self, str:item_name, int:sphere) -> void:
    self.Item = item_name
    self.Sphere = sphere

  def get_accessibilty(self) -> bool:
    return self.__LocationLogic.accessible()

  def required_progression(self):
    return self.__LocationLogic.get_all_items()

  def item_received(self, str:item_name) -> void:
    if self.get_accessibilty():
      return
    else:
      self.__LocationLogic.add_item(item_name)
