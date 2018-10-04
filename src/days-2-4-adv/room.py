# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, inventory, naturalLight):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.naturalLight = naturalLight
        self.is_light = naturalLight
    def printName(self):
        print(self.name)
    def printDesc(self):
        print(self.description)
    def printInv(self):
        if len(self.inventory) > 0:
            print("The room contains:")
            for item in self.inventory:
                print(item.name, ":", item.description)
        else:
            print('There is nothing of interest here.')