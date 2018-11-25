# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.current_room = room #starting/current room of the player
        self.health = 100
        self.inventory = []
    
    def try_move(self, direction):
        key = direction + "_to"
        if not hasattr(self.current_room, key):
            print("You can't go that way!")
            return self.current_room
        else:
            return getattr(self.current_room, key)
    
    def take_item(self, item):
        self.inventory.append(item)
    
    
        
