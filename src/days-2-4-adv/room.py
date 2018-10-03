# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    def __str__(self):
        return f"\n\n{self.name}\n\n   {self.description}\n\n items in room: {*self.items, sep = ", "}"
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
    def getItemFromRoom(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            return None
    def dropItemInRoom(self, item):
        if item in self.items:
            return None
        else:
            self.items.append(item)
            return item
