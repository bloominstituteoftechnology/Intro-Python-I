from item import LightSource
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory
        self.score = 0
        #health

    def printStatus(self):
        print()
        print('*****************************************')
        print(self.name.capitalize())
        print('Score: ', self.score)
        #health

    def getInv(self):
        print("\nInventory: ")
        for item in self.inventory:
            print('    ', item.name, ': ', item.description)

    def addItem(self, item):
        self.inventory.append(item)
        result = item.on_take()
        if type(result) == type(3):
            self.score = self.score + result
        self.location.removeItem(item)

    def dropItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.location.addItem(item)
            item.on_drop()
        else:
            print('That item is not in your inventory')

    def hasLightSource(self):
        for item in self.inventory:
            if isinstance(item, LightSource):
                return True

        return False
