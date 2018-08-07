from room import Room
from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.
flint = Item('flint and steel', 'used to make fire')
mirror = Item('mirror', 'a small round mirror')
class Player(object):
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = [flint, mirror]
        self.actions = [
            'search: search room for hidden items',
            'grab: grab found item from room',
            'use: attempt to use item in current room',
            'light: light torch',
            'items: display items carried by player'
        ]

    def display_items(self):
        if len(self.items) > 0:
            for i in self.items:
                print('\t' + '* ' + i.name + '----' + i.description)
        else:
            print("**********Player has no items!**********")

    def display_actions(self):
        for action in self.actions:
            print("* " + action)


