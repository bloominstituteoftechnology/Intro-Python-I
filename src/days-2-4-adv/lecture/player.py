class Player:
    def __init__(self, name, startLocation, startingItems=[]):
        self.name = name
        self.location = startLocation
        self.items = startingItems
    def change_location(self, new_location):
        self.location = new_location
    def __repr__(self):
        return "Current Location: {}".format(self.location)
    def __str__(self):
        return "Current Location: {}".format(self.location)
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, name):
        self.items.remove(item)
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower:
                return item
            return None
    def getInventoryString(self):
        return ', '.join([item.name for item in self.items])