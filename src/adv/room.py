# Implement a class to hold room information. This should have name and
# description attributes.

# Add capability to add items to rooms.

# The `Room` class should be extended with a `list` that holds the `Item`
# that are currently in that room.

# Add an attribute to `Room` called `is_light` that is 
# `True` if the `Room` is naturally illuminated, or `False` if a 
# `LightSource` is required to see what is in the room.

class Room():
    def __init__(self, name, description, is_Light):
        self.name = name
        self.description = description
        self.is_Light = is_Light
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def searchItems(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None
    
    def removeItem(self, item_name):
        for item in self.items:
            if (item.name == item_name):
                self.items.remove(item)
        return None