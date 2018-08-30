# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def getLoots(self):
        if len(self.items)==0:
            return None
        return [i.name for i in self.items]

    def getRoomInDirection(self, direction):
        if direction=='n':
            return self.n_to
        elif direction=='s':
            return self.s_to
        elif direction=='w':
            return self.w_to
        elif direction=='e':
            return self.e_to
        else:
            return None
    
    def removeItem(self, index):
        del self.items[index]

    def receiveItem(self, item):
        self.items.append(item)