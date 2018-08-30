class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.is_light = True
    def __str__(self):
        return f"\n  {self.title}\n    {self.description}\n\n{self.items}"
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
            print('Invalid direction')
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
            print('Invalid direction')
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def checkLigh(self):
        if self.is_light:
            pass
        else:
            print('It\'s pitch black!')
    
    