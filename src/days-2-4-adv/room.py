# Implement a class to hold room information. This should have name and
# description attributes.



class Room:
    def __init__(self, title, description, items):
        self.items = items
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def add_item(self, item):
        self.items.append(item)
    def drop_item(self, item):
        for itim in self.items:
            if itim == item:
                self.items.remove(itim)
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
    '''def connectRooms(self, destinationRoom, direction):
        if direction == "n":
            self.n_to = destinationRoom
            destinationRoom.s_to = self
        elif direction == "s":
            self.n_to = destinationRoom
            destinationRoom.n_to = self
        elif direction == "e":
            self.n_to = destinationRoom
            destinationRoom.w_to = self
        elif direction == "w":
            self.n_to = destinationRoom
            destinationRoom.e_to = self
        else:
            print("Invalid direction")'''







