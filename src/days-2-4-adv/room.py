# Implement a class to hold room information. This should have name and
# description attributes.
class Room(object):
    def __init__(self, name, description,items=None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def getRoominDirection(self, direction):
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
    def getItems(self):
        return ', '.join([i.name for i in self.items]) 