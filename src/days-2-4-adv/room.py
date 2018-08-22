# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    n_to = "No Path"
    s_to = "No Path"
    w_to = "No Path"
    e_to = "No Path"
    items = []
    def __init__(self, name, description):
        self.name = str(name)
        self.description = str(description)
    def __str__(self):
        itemString = " ".join([str(item) for item in self.items])
        returnString = "\n%s\n\n %s\n\n  " % (self.name, self.description)
        if self.items != []:
            returnString += itemString
        returnString += "\n"
        return returnString
    def connect(self, room, direction):
        if direction == "n":
            self.n_to = room
            room.s_to = self
        elif direction == "s":
            self.s_to = room
            room.n_to = self
        elif direction == "e":
            self.e_to = room
            room.w_to = self
        elif direction == "w":
            self.w_to = room
            room.e_to = self
    def roomConnection(self, direction):
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
    def addItem(self, item):
        self.items.append(item)
    def getItem(self, itemName):
        itemNames = [str(item) for item in self.items]
        if itemName in itemNames:
            index = itemNames.index(itemName)
            return self.items[index]
    def lookItem(self, itemName):
        item = self.getItem(itemName)
        if item is not None:
            return item.description
        else:
            return ""