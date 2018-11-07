# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory
        #health

    def printStatus(self):
        print()
        print('****')
        print(self.name.capitalize())
        #health
        self.location.printRoom()

    def getInv(self):
        print("\nInventory: ")
        for item in self.inventory:
            print('    ', item.name, ': ', item.description)

    def addItem(self, item):
        self.inventory.append(item)
        self.location.removeItem(item)

    def dropItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.location.addItem(item)
        else:
            print('That item is not in your inventory')
