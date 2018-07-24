# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, currRoom):
        self.currRoom = currRoom

    def setRoom(self, new_room):
        self.currRoom = new_room