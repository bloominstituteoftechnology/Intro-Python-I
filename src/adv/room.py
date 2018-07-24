# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomName, summary):
        self.roomName = roomName
        self.summary = summary
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None


    def printRoom(self):
        return f"The {self.roomName} is {self.summary}"


# test = Room("Kitchen", "is for cooking food")

# print(test.printRoom())