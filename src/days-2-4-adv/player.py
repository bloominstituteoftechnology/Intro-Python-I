# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player(Room):
    def __init__(self, location, description, items):
        self.items = items
        Room.__init__(self, location, description)
    def __str__(self):
        return self.location + '' + self.items
        
