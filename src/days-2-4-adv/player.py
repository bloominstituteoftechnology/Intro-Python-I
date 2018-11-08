# Write a class to hold player information, e.g. what room they are in
# currently.
from game_map import Map
from item import Item

class Player:
    def __init__(self,current_room):
        self.current_room = current_room
        self.health = 100
        self.inventory = []
        self.movement_speed = 10
        self.score = 0

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

    def actions(self, action, location):
        item = False
        for i in location.items:
            if (i.name == action[1]):
                item = True
                if action[0] == "take":
                    self.inventory.append(action[1])
                    location.remove_item(i)
                    print(f"You now have a {action[1]}")
            elif action[0] == "drop":
                self.inventory.remove(action[1])
                location.add_item(Item(action[1], i.name))
                print(f"You have dropped a {action[1]}")
        
        if(item == False):
            print("No item was found")
        