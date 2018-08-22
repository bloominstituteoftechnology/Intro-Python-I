# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, startRoom):
        self.name = name
        self.curRoom = startRoom
    def mRooms(self, direction):
        nextRoom = self.curRoom.roomConnection(direction)
        if nextRoom is not None:
            self.curRoom = nextRoom
