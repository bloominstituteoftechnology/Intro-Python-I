# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player

class Room:
    def __init__(self, name, description,items):
        self.name = name
        # self.inventory=inventory
        self.description = description
        self.items = items
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f"\n\n{self.name}\n\n   {self.description}\n"
    def printRoomDescription(self, player):
        if player.hasLight():
            print(str(self))
        else:
            print("You cannot see anything.")
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

    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
