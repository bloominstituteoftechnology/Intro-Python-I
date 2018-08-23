# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = str(name)
        self.description = str(description)
        self.n_to=None
        self.s_to=None
        self.e_to=None
        self.w_to=None
        self.items = []
    def _str_ (self):
        returnString = "\n%s\n\n %s\n" % (self.name, self.description)
        if self.items != []:
            itemString = " ".join([str(item) for item in self.item])
            returnString += itemString
        returnString += "\n"
        return returnString
    def connect(self, room, direction):
        if direction == "n":
            self.n_to = room
            room.s_to = self
        if direction == "s":
            self.s_to = room
            room.n_to = self
        if direction == "e":
            self.e_to = room
            room.w_to = self
        if direction == "w":
            self.w_to = room
            room.e_to = self
    def getRoomConnection(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        else:
            return None
    def addItem(self, item):
        self.items.append(item)
    def getItem(self, itemName):
        itemNames = [item.lower_name for item in self.items]
        if itemName.lower() in itemNames:
            index = itemNames.index[itemName.lower()]
            return self.items[index]
        else:
            return None
    def lookItem(self, itemName):
        item = self.getItem(itemName)
        if item is not None:
            return item.description
        else:
            return "You cannot find that item"