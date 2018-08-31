# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, startLocation):
        self.name = name
        self.location = startLocation
        self.items = []
    def change_location(self, newLocation):
        self.location = newLocation
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)