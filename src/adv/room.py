# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomName, summary, items, treasureScored, index):
        self.roomName = roomName
        self.summary = summary
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = items
        self.treasureScored = treasureScored
        self.index = index


    def printRoom(self):
        return f"The {self.roomName} is {self.summary}"

    def printItems(self):
        return f"The room has these items: {self.items}"

# test = Room("Kitchen", "is for cooking food", ["Sword", "Staff", "Knife"])

# print(test.printRoom())
# print(test.printItems())
