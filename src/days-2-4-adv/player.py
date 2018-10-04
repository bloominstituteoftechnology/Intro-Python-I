# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []

    def __repr__(self):
        return f"Current Room: {self.currentRoom}"

    def travel(self, newRoom):
        self.currentRoom = newRoom

    def __repr__(self):
        return "Current Location: {}".format(self.currentRoom)

    # deal with items by player

    def findItemByName(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def getInventoryString(self):
        return "' ".join({item.name for item in self.items})