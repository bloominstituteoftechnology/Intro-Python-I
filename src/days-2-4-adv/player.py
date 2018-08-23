# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.startingRoom = startingRoom
    def moveRooms(self, direction):
        nextRoom = self.currentRoom.getRoomConnection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom    