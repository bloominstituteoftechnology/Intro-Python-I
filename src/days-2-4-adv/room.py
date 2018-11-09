
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, room_items, is_light = False):
        self.name = name
        self.description = description
        self.room_items = room_items
        self.is_light = is_light


