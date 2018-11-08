# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.health = 100
        self.inventory = []
        self.movement_speed = 10

    def pickup_item(self, item):
        self.inventory.append(item)

    def try_move(self, direction):

        # Try to move in a direction or print error message
        d = direction + "_to"

        #check to see if we can move in a specified direction
        if not hasattr(self.currentRoom, d):
            print("You can't go that way")
            return self.currentRoom
        else:
            self.currentRoom = self.currentRoom[d]
