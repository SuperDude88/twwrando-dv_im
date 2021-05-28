"""
Entrance Handler. Properties include
Entrance.Name         : str
Entrance.Hint         : str
Entrance.Path         : str
Entrance.LocaleName   : str
Entrance.Locations    : ItemLocation List

The constructor requires all but the 'Locations' property to be provided.

"""
from Location import Location as Location
class Entrance(Location):

  def __init__(self, str: name, str:hint, str:path, str:LocaleName, str:logicString):
      self.Hint = hint
      self.Path = path
      self.LocaleName = LocaleName
      self.Locations = list()
      Location.__init__(self, name, logicString)

  def location_open(self) -> bool:
      return self.logic.accessible
