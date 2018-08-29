# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """Holds information about a player"""
    def __init__(self, startLocation):
        self.location = startLocation
    def changeLocation(self, newLocation):
        self.location = newLocation
    def __str__(self):
        return("Current Location: {}".format(self.location))
    def __repr__(self):
        return "Current Location: {}".format(self.location)