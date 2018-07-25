# Write a class to hold player information, e.g. what room they are in
# currently.
#
# Add capability to add `Item`s to the player's inventory. The inventory can
# also be a `list` of items "in" the player, similar to how `Item`s can be in a
# `Room`.

from room import Room

class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []
    
    def toInventory(self, item):
        inventory.append(item)