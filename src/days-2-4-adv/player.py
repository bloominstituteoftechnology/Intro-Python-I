# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.health = 100
        self.inventory = []
        self.movement_speed = 10
        self.rage = 10
        
    def pickup_item(self, item):
        self.inventory.append(item)

    def try_move(self, direction):

        key = direction + "_to"

        # check to see if we can move in the specified direction
        if not hasattr(self.location, key):
            print("You can't go that way!")
            return self.location
        else:
            return getattr(self.location, key)
        
