from room import Room
from item import Item, Treasure, LightSource, LockedItem
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(object):
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.score = 0
        # there should be no duplicates in items
        self.items = {
            'flint': Item('flint', 'used to make fire'),
            'mirror': Item('mirror', 'a small round mirror')
        }
        self.actions = [
            'search: search room for hidden items',
            'grab: grab found item from room',
            'drop: drop item',
            'use: attempt to use item in current room',
            'light: light item',
            'items: display items carried by player',
            'open: open unlocked item, chest, door, etc'
        ]

    def display_items(self):
        pass

    def display_actions(self):
        for action in self.actions:
            print("* " + action)

    def search(self):
        pass
    
    def grab(self):
        pass

    def drop(self):
        pass
    
    def use(self):
        pass
    
    def light(self):
        pass

    def open(self):
        pass


