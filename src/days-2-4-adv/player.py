# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
#THIS CREATES THE PLAYER CLASS THAT
#DEFINES THE ATTRIBUTES OF PLAYER
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(f"\n\nnow entering {nextRoom}")
        else:
            print("\n\ncannot move in that direction")

    def look(self, direction=None):
        if direction is None:
            print(f"\n\ncurrently in {self.currentRoom}")
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                # print(f"\n\nin '{cmds[1]}' direction is {nextRoom}")
                print(f"\n\nin that direction is {nextRoom}")
            else:
                print("\n\nnothing in that direction")

    