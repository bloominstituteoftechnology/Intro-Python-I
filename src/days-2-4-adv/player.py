# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, startLocation):
        self.inventory = None
        self.weapon = None
        self.health  = 100
        self.name = name

        self.location = startLocation
        print("\nHello {}".format(self.name),
              "You are: {}".format(self.location))

    def change_location(self, new_location):
        self.location = new_location
        print("\nMoved to: {}".format(self.location))

    def __repr__(self):
        return "Current Location: {}".format(self.location)

    def __str__(self):
        return "Current Location: {}".format(self.location)
