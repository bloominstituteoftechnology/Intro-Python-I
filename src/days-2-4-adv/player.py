# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, currentRoom):
        self.current_room = currentRoom
        self.inventory = []
        self.movement_speed = 10

    def pickup_item(self, item):
        self.inventory.append(item)

    def putdown_item(self, item):
        self.inventory.remove(item)

    def try_move(self, direction):
        key = direction + "_to"

        if not hasattr(self.current_room, key):
            print("You can't go that way!")
            return self.current_room
        else:
            return getattr(self.current_room, key)
