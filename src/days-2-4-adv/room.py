# Implement a class to hold room information. This should have name and
# description attributes.

class Room(object):
    def __init__(self, name, description, *paths):
        self.name = name
        self.description = description
        self.paths = paths
        self.items = {}

    def connect(self, room, direction):
        if direction == 'N':
            self.north = room
        elif direction == 'E':
            self.east = room
        elif direction == 'S':
            self.south = room
        elif direction == 'W':
            self.west = room
        elif direction == 'U':
            self.up = room
        elif direction == 'D':
            self.down = room

    def addItem(self, name, description):
        self.items[name] = description
