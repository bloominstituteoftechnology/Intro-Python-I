# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return f"\n\n{self.name}\n\n   {self.description}\n"

    # deal with items in rooms
    def addItem(self, items):
        self.items.append(item)

    # def direction(self, direction):
    #     if direction == "n":
    #         return self.n_to
    #     elif direction == "s":
    #         return self.s_to
    #     elif direction == "e":
    #         return self.e_to
    #     elif direction == "w":
    #         return self.w_to
    #     else:
    #         return "None"

    # def connectRooms(self, newRoom, direction):
    #     if direction == "n":
    #         self.n_to = newRoom
    #         newRoom.s_to = self
    #     elif direction == "s":
    #         self.s_to = newRoom
    #         newRoom.s_to = self
    #     elif direction == "e":
    #         self.e_to = newRoom
    #         newRoom.e_to = self
    #     elif direction == "w":
    #         self.w_to = newRoom
    #         newRoom.w_to = self
    #     else:
    #         print("Sorry, you can't move in that direction, please enter n, s, e, w")
