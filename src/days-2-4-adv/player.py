# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.speed = 10

    def move(self, direction):
        d = direction + "_to"
        self.room = self.room[d]
