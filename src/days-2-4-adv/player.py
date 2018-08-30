# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, startRoom, inventory=[]):
        self.name = name
        self.location = startRoom
        self.inventory = inventory

    def getInventory(self):
        if (len(self.inventory) == 0):
            return None
        else:
            return ([i.name for i in self.inventory])

    def getItem(self, item):
        self.inventory.append(item)
        item.on_take()
    
    def dropItem(self, index):
        del self.inventory[index]