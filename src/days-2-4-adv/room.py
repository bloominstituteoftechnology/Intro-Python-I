# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.is_light = False
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
    def addItem(self,item):
        self.items.append(item)
    def removeItem(self,item):
        self.items.remove(item)
    def findItemByName(self,name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item