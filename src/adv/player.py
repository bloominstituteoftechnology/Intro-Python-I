# Write a class to hold player information, e.g. what room they are in
# currently.
#
# Add capability to add `Item`s to the player's inventory. The inventory can
# also be a `list` of items "in" the player, similar to how `Item`s can be in a
# `Room`.

class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []
        self.score = 0
    
    def toInventory(self, item):
        self.inventory.append(item)
    
    def searchInventory(self, item_name):
        for item in self.inventory:
            if item_name == item.name:
                return item
            else:
                return None
    
    def removeItem(self, item_name):
        for item in self.inventory:
            if (item.name == item_name):
                self.inventory.remove(item)
            else:
                return None