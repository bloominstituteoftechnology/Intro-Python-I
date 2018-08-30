# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player():
    def __init__(self, room):
        self.room = room
        self.items = []
        self.score = 0

    def getScore(self):
        print("You currently have {} points, pick up more items to earn more points.".format(
            self.score))
