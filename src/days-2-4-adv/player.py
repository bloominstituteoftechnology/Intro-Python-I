# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(object):
    def __init__(self, room):
        self.currentRoom = room
