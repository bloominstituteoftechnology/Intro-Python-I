# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(object):
    def __init__(self, name, startRoom):
        self.name = name
        self.location = startRoom
        self.items = {}

    def roomDescription(self):
        return('you stand in the {}, {}'.format(self.location.name, self.location.description))

    def move(self, direction):
        if direction in self.location.paths:
            if direction == 'N':
                self.location = self.location.north
            elif direction == 'E':
                self.location = self.location.east
            elif direction == 'S':
                self.location = self.location.south
            elif direction == 'W':
                self.location = self.location.west
            elif direction == 'U':
                self.location = self.location.up
            elif direction == 'D':
                self.location = self.location.down
        else:
            return 'false'

    def pickup(self, key):
        self.items[key] = self.location.items[key] 
