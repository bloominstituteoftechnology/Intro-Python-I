# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room


class Player:
    def __init__(self, room):
        self.room = room

    def move(self, direction):
        key = direction + "_to"



        # check to see if we can move in the specified direction
        if not hasattr(self.room, key):
            print("You can't go that way!")
            return self.room
        else:
            return getattr(self.room, key)

    def __str__(self):
        return f"{self.room}"



