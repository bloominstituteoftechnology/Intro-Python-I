# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return f"\n\n{self.name}\n\n{self.description}\n\n{self.getItemsInString()}\n"
    def getItemsInString(self):
        return f"Items in the room: {','.join([str(item) for item in self.items])}"
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
    # adds an item to the end of the list
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def getItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None