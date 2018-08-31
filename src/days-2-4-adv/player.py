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
    # def dropItem(self, currentItem):
    #     currentItem.on_drop()
    def addItem(self, currentItem):
        self.items.append(currentItem.name)
    def removeItem(self, currentItem):
        self.items.remove(currentItem)
    def findItemByName(self, currentItem):
        for item in self.items:
            if currentItem == item.lower():
                return item