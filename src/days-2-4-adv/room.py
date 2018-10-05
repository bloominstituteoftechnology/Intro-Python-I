# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return f"\n\n{self.name}\n\n {self.description}\n\n  {self.getItemsString()}\n"

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

#------------item related methods--------------
    def getItemsString(self):
        return f"The room contains: {', '.join([item.name for item in self.items])}"

    def findItemByName(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
    