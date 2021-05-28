"""
Island Handler. Properties include
Island.ID           : int
Island.ShortName    : str
Island.LongName     : str
Island.Abbreviation : str
Island.Hint         : str
Island.Stage        : str
Island.LocaleName   : str
Island.Neighbors    : Island List
Island.Locations    : ItemLocation List


The constructor requires all but the 'Checks' property to be provided.

Functions
location_open() -> bool
add_neighbor(Island:neighbor) -> void
get_all_neighbors() -> Island List
"""
from Location import Location as Location
class Island(Location):

  def __init__(self, int:ID, str:ShortName, str:LongName, str:Abbreviation,
    str:Hint, str:Stage, str:LocaleName, str:logicString):

    self.ID = ID
    self.ShortName = ShortName
    self.LongName = LongName
    self.Abbreviation = Abbreviation
    self.Hint = Hint
    self.Stage = Stage
    self.LocaleName = LocaleName
    self.Neighbors = list()
    self.Locations = list()
    Location.__init__(self,LongName, logicString)

  def location_open(self) -> bool:
      return self.logic.accesible

  def add_neighbor(self, Location:neighbor) -> void:
    if neighbor not in self.Neighbors:
          self.Neighbors.append(neighbor)

  def get_all_neighbors(self):
    return self.Neighbors
