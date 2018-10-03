# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
        self.score = 0
    def move(self, direction):
        if direction == "n":
            if self.currentRoom.n_to is not None:
                self.currentRoom = self.currentRoom.n_to
            else:
                print("Where do you think you're going?")
        elif direction == "e":
            if self.currentRoom.e_to is not None:
                self.currentRoom = self.currentRoom.e_to
            else:
                print("Where do you think you're going?")
        elif direction == "s":
            if self.currentRoom.s_to is not None:
                self.currentRoom = self.currentRoom.s_to
            else:
                print("Where do you think you're going?")
        elif direction == "w":
            if self.currentRoom.w_to is not None:
                self.currentRoom = self.currentRoom.w_to
            else:
                print("Where do you think you're going?")
