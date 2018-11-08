# player class
from item import Item # might centralize all this in to 1 file at some point
from lightsource import LightSource

# created a simple constructor to take in a room to match the calling convention in my adv.py
class Player:
    def __init__(self, room, items=None, health=100):
        self.room = room
        self.items = [] if items is None else items
        self.gold = 0
        self.health = health
        self.attack = 0

    # class methods

    # get method to pick up an item [ making use of append() method ]
    def get(self, item):
        self.items.append(item)

    # drop method to drop an item [ making use of the del keyword and suing the index() method ]
    def drop(self, item):
        del self.items[self.items.index(item)]

    # check the players gold
    def check_gold(self):
        if self.gold == 0:
            print("\nYou are skinter than a poor mans poor bits!")
        else:
            print(f"\nYou have: {self.gold} gold.")

    # check the players items list for a specific item
    def check_for_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return True
        return False

    # ehcek for the light
    def check_for_light(self):
        for item in self.items:
            if type(item) == LightSource:
                return True
        return False

    # list out the items in the players inventory [items] list
    def inventory(self):
        print(f"\nYou have the following items: {', '.join(item.name for item in self.items)}")

    def __str__(self):
        return str(self.location.name)  + "\n" + str(self.location.description)