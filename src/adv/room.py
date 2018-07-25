# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room(Item):
    def __init__(self, name, description, item_name, item_description):
        Item.__init__(self, item_name, item_description)
        self.name = name
        self.description = description
