# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """Holds information about a player"""
    def __init__(self, startLocation, startItems=[]):
        self.location = startLocation
        self.items = startItems
    def changeLocation(self, newLocation):
        self.location = newLocation
    # def __str__(self):
    #     return("Current Location: {}".format(self.location))
    # def __repr__(self):
    #     return("Current Location: {}".format(self.location))
    def dropItem(self, item):
        item.on_drop()
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item