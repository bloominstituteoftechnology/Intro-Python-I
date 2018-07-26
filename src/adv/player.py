# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player(Item):
    def __init__(self, room_location, weapon_inventory = [], weapon_choice = None):
        self.weapon_inventory = weapon_inventory
        self.weapon_choice = weapon_choice
        self.room_location = room_location