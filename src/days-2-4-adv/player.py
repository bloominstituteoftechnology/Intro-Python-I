# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.health = 100
        self.inventory = []
        self.movement_speed = 10
        self.rage = 10
        self.score = 0

    def pickup_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def try_move(self, direction):
        key = direction + "_to"
        if not hasattr(self.location, key):
            return self.location
        else:
            return getattr(self.location, key)

    def check_items(self, direction):
        print(f'items include: {self.inventory}')

    def has_item(self, item_name):
        for my_item in self.inventory:
            if my_item.name == item_name:
                return True
        return False