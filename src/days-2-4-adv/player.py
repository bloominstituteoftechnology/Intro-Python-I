from room import Room
from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.
flint = Item('flint', 'used to make fire')
mirror = Item('mirror', 'a small round mirror')
class Player(object):
    def __init__(self, name, room):
        self.name = name
        self.room = room
        # there should be no duplicates in items
        self.items = [flint, mirror]
        self.actions = [
            'search: search room for hidden items',
            'grab: grab found item from room',
            'drop: drop item',
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

    def grab_item(self, name):
        found = False
        item_index = 0
        for i in range(len(self.room.items)):
            if self.room.items[i].name == name:
                found = True
                item_index = i
        if found:
            self.items.append(self.room.items[item_index])
            del self.room.items[item_index]
            print("++++++++++ %s GRABBED! ++++++++++" % name)
        else:
            print("Item %s does not exist here!" % name)
    
    def drop_item(self, name):
        in_inventory = False
        item_index = 0
        for i in range(len(self.items)):
            if self.items[i].name == name:
                in_inventory = True
                item_index = i
        if in_inventory:
            self.room.items.append(self.items[item_index])
            del self.items[item_index]
            self.room.searched = False
            print("++++++++++ %s DROPPED! ++++++++++" % name)
        else:
            print("Item %s not in inventory!")

    def use_item(self, item):
        pass


