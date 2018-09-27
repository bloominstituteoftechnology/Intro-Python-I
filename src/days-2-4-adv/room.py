# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, title, description, light):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []
        self.is_light = light
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
    def connectRooms(self, destinationRoom, direction):
        if direction == "n":
            self.n_to = destinationRoom
            destinationRoom.s_to = self
        elif direction == "s":
            self.s_to = destinationRoom
            destinationRoom.n_to = self
        elif direction == "e":
            self.e_to = destinationRoom
            destinationRoom.w_to = self
        elif direction == "w":
            self.w_to = destinationRoom
            destinationRoom.e_to = self
        else:
            print("Invalid Direction") 
    
    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
    
    def findItemByName(self, item):
        if len(self.items) > 0:
            for i in self.items:
                if i.name == item:
                    return i

    def listOfItems(self):
        return ", ".join([item.name for item in self.items])

    def lightUpRoom(self):
        self.is_light = True
    
    def darkenRoom(self):
        self.is_light = False

    def hasLight(self, light):
        if len(self.items) > 0:
            for i in self.items:
                if isinstance(i, light):
                    return True
        else:
            return False
