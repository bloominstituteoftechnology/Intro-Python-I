# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom, startingItems=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.items = startingItems

    def look(self, direction):
        nextRoom = None
        if direction == "n":
            if self.currentRoom.n_to is not None:
                nextRoom = self.currentRoom.n_to
        elif direction == "s":
            if self.currentRoom.s_to is not None:
                nextRoom = self.currentRoom.s_to
        elif direction == "e":
            if self.currentRoom.e_to is not None:
                nextRoom = self.currentRoom.e_to
        elif direction == "w":
            if self.currentRoom.w_to is not None:
                nextRoom = self.currentRoom.w_to
        if nextRoom is not None:
            print(nextRoom)
        else:
            print("There is nothing there.")

    def printInventory(self):
        print("You are carrying:\n")
        for item in self.items:
            print(f" {item.name}\n")