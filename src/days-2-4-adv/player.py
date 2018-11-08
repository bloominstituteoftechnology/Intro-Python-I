# Write a class to hold player information, e.g. what room they are in
# currently.
from game_map import Map

class Player:
    def __init__(self,current_room):
        self.current_room = current_room
        self.health = 100
        self.inventory = []
        self.movement_speed = 10

    def pickup_item(self, item):
        self.inventory.append(item)

    def move(self, direction):
        d = direction + "_to"
        
        if not hasattr(self.current_room,d):
            print("\nThere is no path that way!")
            return self.current_room
        elif direction == "m":
            map.game_map(self.current_room)
        else:
            return getattr(self.current_room, d)

    def actions(self, action):
        actions = action.split()
        if actions[0] == "take":
            self.inventory.append(actions[1])
        elif actions[0] == "drop":
            self.inventory.remove()

    