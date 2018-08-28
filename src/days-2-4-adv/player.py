# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, room=None):
        self.room = room
        self.name = name
    def __str__(self):
        return self.name
    def getRoom(self):
        return self.room
