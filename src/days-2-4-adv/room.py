from item import LightSource
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, is_light=False, inventory=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.inventory = inventory
        self.is_light = is_light

    def printRoom(self):
        print("Current location: ", self.name)
        print(self.description)
        if len(self.inventory) > 0:
            print('\nOn the ground you see: ')
            for item in self.inventory:
                print(item.name, ': ', item.description)

    def contains(self, item):
        result = False
        for thing in self.inventory:
            if item.name == thing.name:
                result = True
        return result

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item):
        self.inventory.remove(item)

    def hasLightSource(self):
        for item in self.inventory:
            if isinstance(item, LightSource):
                return True

        return False
