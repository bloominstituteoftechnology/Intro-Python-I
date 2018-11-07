from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.health = 100
        self.inventory = []
        self.movement_speed = 10

    def pickup_item(self, item):
            self.inventory.append(item)

    def try_move(self, direction):
            """
            try to move
            """
            key = direction + "_to"

            if not hasattr(self.currentRoom, key):
                print("you can't go that way")
                return self.currentRoom
            else:
                return getattr(self.currentRoom, key)