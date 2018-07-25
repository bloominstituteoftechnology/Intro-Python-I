# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player(Item):
    def __init__(self, room_location, name_item = None, description_item = None):
        Item.__init__(self, name_item, description_item)
        self.room_location = room_location