# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.speed = 10

    def move(self, direction):
        key = direction + "_to"

        # check to see if we can move in the specified direction
        if not hasattr(self.room, key):
            print("You can't go that way!")
            return self.room
        else:
            return getattr(self.room, key)


room = Room("Outside", "outside")
foyer = Room("Foyer")
room.n_to = foyer
foyer.s_to = room

p = Player(room)
print(p.room)
p.room = room.n_to
print(p.room)
