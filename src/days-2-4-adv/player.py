# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, startRoom, items):
        self.startRoom = startRoom
        self.name = name
        self.items = items
