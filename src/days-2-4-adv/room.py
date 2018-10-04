# Implement a class to hold room information. This should have name and
# description attributes.
from item import LightSource

class Room:
    def __init__(self, name, description, items, hasLight):
        self.name = name
        self.description = description
        self.items = items
        self.hasLight = hasLight
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
            return f"\n\n{self.name}\n\n   {self.description}\n\n   This room contains:\n\n{self.checkItems()}\n" 
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
    def checkItems(self):
        items = ""
        for i in self.items:
            items += f"   {i.name}: {i.description}\n"
        return items
    def removeItem(self, item):
        for i in self.items:
            if i.name == item:
                if isinstance(i, LightSource):
                    self.hasLight = False
                self.items.remove(i)
                return i
    def addItem(self, item):
        self.items.append(item)
        if isinstance(item, LightSource):
            self.hasLight = True
