# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, startLocation, items):
        self.name = name
        self.location = startLocation
        self.items = items
    def changeLocation(self, newLocation):
        self.location = newLocation
    def __repr__(self):
        return "Current Location: {}".format(self.location)
    def __str__(self):
        return "Current Location: {}".format(self.location)

    def getItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)