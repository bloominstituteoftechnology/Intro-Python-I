# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, startRoom, inventory=[]):
        self.name = name
        self.location = startRoom
        self.inventory = inventory

    def getInventory(self):
        return ', '.join([i.name for i in self.inventory])
