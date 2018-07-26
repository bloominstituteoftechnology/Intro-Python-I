# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player
from item import Item


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return "You are currently " + self.name + '\n\n' + self.description + '\n'

    def pickup(self, player, item):
        try:
            self.items.remove(item)
            player.addItem(item)
            return "Picked up " + item.name + '\n'
        except:
            return "There is no " + item.name + '\n'

    def drop(self, player, item):
        try:
            player.removeItem(item)
            self.items.append(item)
            return "Dropped " + item.name + '\n'
        except:
            return "You're not carrying " + item.name + '\n'

    def viewItems(self):
        return self.items
