"""
Location should be the parent class of any randomizable location,
this includes entrances, items, and enemies. This is simply to adhere
to proper OOP principles.
"""
from logic import Logic as Logic
class Location:

  def __init__(self, str: name, str: logic):
      self.name = name
      self.logic = logic(logic)
