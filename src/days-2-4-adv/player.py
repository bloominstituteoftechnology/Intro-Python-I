# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, startRoom):
        self.currentRoom = startRoom
    def moveTo(self, room):
        self.currrentRoom = room