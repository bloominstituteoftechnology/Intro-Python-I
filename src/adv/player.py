# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, startRoom):
        self.curRoom = startRoom
        self.items = []

    def addItem(self, item):
         self.items.append(item)

    def removeItem(self, name):

        item = self.findItem(name)
        self.items.remove(item)

    def findItem(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def pickUpItem(self, name):
        item = self.curRoom.findItem(name)
        if item is None:
            print("Item not found")
        else:
            self.addItem(item)
            self.curRoom.removeItem(item.name)

    def useItem(self, name):
        item = self.findItem(name)
        if item is None:
            print("Item not found")
        else:
            self.removeItem(item.name)
            self.curRoom.addItem(item)

    def printInventory(self):

        if len(self.items) > 0:
            print("Inventory:\n")
            for item in self.items:
                print("name: ", item.name, "description: ", item.description)
        else:
            print("You have no items in inventory")