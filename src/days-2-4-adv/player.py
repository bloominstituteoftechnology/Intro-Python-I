# Write a class to hold player information, e.g. what room they are in
# currently.
from game_map import Map
from item import Item
from item import Lightsource

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
            if (action[0] == "take" and i.name == action[1]):
                item = True
                self.inventory.append(action[1])
                location.remove_item(i)
                if hasattr(i, "picked_up"):
                    self.score += i.value
                print(f"You now have a {action[1]}")
        for i in self.inventory:
            if (action[0] == "drop" and i == action[1]):
                item = True
                self.inventory.remove(action[1])
                location.add_item(i)
                if (i == "torch"):
                    print("Sad to see a lightsource go.")
                else:
                    print(f"You have dropped a {action[1]}")
        
        if(item == False):
            print("No item was found")

    def search(self, location):
        for i in location.items:
            print(i.name)
        