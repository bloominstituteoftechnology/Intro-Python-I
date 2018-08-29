# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, startLocation):
        self.name = name
        self.location = startLocation
    def changeLocation(self, newLocation):
        self.location = newLocation
    def __repr__(self):
        return "Current Location: {}".format(self.location)
    def __str__(self):
        return "Current Location: {}".format(self.location)