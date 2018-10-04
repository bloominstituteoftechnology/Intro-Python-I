# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
    def __str__(self):
        return f"\n{self.name}\n\n  {self.description}\n\n {self.getItemsString()}\n"
    def getItemsString(self):
        if len(self.items) > 0:
            return f"The room contains: {', '.join([item.name for item in self.items])}"
        else:
            return "This room does not contain items."
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        elif direction == "e":
            return self.e_to
        else:
            return None
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None 