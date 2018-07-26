# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room(Item):
    def __init__(self, room_name, room_story, name_item, description_item):
        Item.__init__(self, name_item, description_item)
        self.room_name = room_name
        self.room_story = room_story