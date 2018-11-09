# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def try_move(self, direction):
        key = direction + '_to'

        if not hasattr(self.current_room, key):
            print("You can't go that way!")
            return self.current_room
        else:
            return getattr(self.current_room, key)

    def find_item(self, item_name):
        for item in self.current_room.items:
            if item.name.lower() == item_name:
                return item
            return none
