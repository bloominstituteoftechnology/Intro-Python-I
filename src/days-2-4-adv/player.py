from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room):
        self.current_room = current_room
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

            if not hasattr(self.current_room, key):
                print("you can't go that way")
                return self.current_room
            else:
                return getattr(self.current_room, key)