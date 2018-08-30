# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, startLocation, items, score):
        self.name = name
        self.location = startLocation
        self.items = items
        self.score = score
    def changeLocation(self, newLocation):
        self.location = newLocation
    def __repr__(self):
        return "Current Location: {}".format(self.location)
    def __str__(self):
        return "Current Location: {}".format(self.location)

    def getItem(self, item):
        self.items.append(item)
        add_to_score = item.on_take()
        self.score = add_to_score

    def dropItem(self, item):
        item.on_drop(item)
        self.items.remove(item)

    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item