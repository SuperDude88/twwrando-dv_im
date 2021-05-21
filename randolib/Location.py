"""
Location Handler. Properties include
Location.ID           : int
Location.ShortName    : str
Location.LongName     : str
Location.Abbreviation : str
Location.Hint         : str
Location.Stage        : str
Location.LocaleName   : str
Location.Neighbors    : Location List
Location.Checks       : ItemLocation List

The constructor requires all but the 'Checks' property to be provided.

Functions
location_open() -> bool
add_neighbor(Location:neighbor) -> void
get_all_neighbors() -> Location List
"""

class Location:

  def __init__(self, int:ID, str:ShortName, str:LongName, str:Abbreviation,
    str:Hint, str:Stage, str:LocaleName):

    self.ID = ID
    self.ShortName = ShortName
    self.LongName = LongName
    self.Abbreviation = Abbreviation
    self.Hint = Hint
    self.Stage = Stage
    self.LocaleName = LocaleName
    self.Neighbors = list()

  def location_open(self) -> bool:
      return True

  def add_neighbor(self, Location:neighbor) -> void:
    if neighbor not in self.Neighbors:
          self.Neighbors.append(neighbor)

  def get_all_neighbors(self):
    return self.Neighbors
