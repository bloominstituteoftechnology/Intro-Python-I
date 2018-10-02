# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory
    def printName(self):
        print(self.name)
    def printDesc(self):
        print(self.description)
    def printInv(self):
        if len(self.inventory) > 0:
            print("The room contains: ", self.inventory)
        else:
            print('There is nothing of interest here.')