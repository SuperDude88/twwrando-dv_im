"""
Dungeon Handler. Properties include
Dungeon.Name         : str
Dungeon.Hint         : str
Dungeon.Path         : str
Dungeon.LocaleName   : str
Dungeon.Locations    : ItemLocation List

The constructor requires all but the 'Locations' property to be provided.

"""
from Location import Location as Location
class Dungeon(Location):

  def __init__(self, str: name, str:hint, str:path, str:LocaleName, str:logicString):
      self.Hint = hint
      self.Path = path
      self.LocaleName = LocaleName
      self.Locations = list()
      Location.__init__(self, name, logicString)

  def location_open(self) -> bool:
      return self.logic.accessible
