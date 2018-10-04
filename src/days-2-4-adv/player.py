# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []
        self.score = 0
        self.hasLight = False
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            if self.hasLight == True or self.currentRoom.hasLight == True:
                print(nextRoom)
            else:
                print(f"\n\n{self.currentRoom.name}\n\n   {self.currentRoom.description}\n\n   It's pitch black!\n")
        else:
            print("You cannot move in that direction.")
    def look(self, direction=None):
        if direction is None:
            print(self.currentRoom)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                print(nextRoom)
            else:
                print("There is nothing there.")
    def takeItem(self, item):
        if self.hasLight == False or self.currentRoom.hasLight == False:
            print("Good luck finding that in the dark!")
        else:
            self.inventory.append(item)
            self.score += item.on_take()
            if isinstance(item, LightSource):
                self.hasLight = True
    def dropItem(self, item):
        for i in self.inventory:
            if i.name == item:
                if isinstance(i, LightSource):
                    i.on_drop()
                    self.hasLight = False
                self.inventory.remove(i)
                return i
    def checkInventory(self):
        print("   Inventory:")
        for i in self.inventory:
            print(f"   {i.name}: {i.description}")
    def checkScore(self):
        print(f"Score: {self.score}")
    def addScore(self, value):
        self.score += value