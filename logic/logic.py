"""
This is the new logic handler, it will be a component of any sub-class to 'Location.py'
Should help with some stuff.
"""

class Logic:

    def __init__(self, str:logicString):
        self.originalString = logicString
        self.logicStruct = self._conToLogStruct(self.originalString)
        self.accessible = False
        self.itemList = list()

    def _con_log_struct(self, str:logicString):
        pass

    def add_item(self, str:ItemName):
        pass

    def get_item_list(self):
        return self.itemList
