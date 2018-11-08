# Implement a class to hold room information. This should have name and
# description attributes.

# basic room class based upon the calling convention and data in the adv.py file
class Room:
    def __init__(self, name, description, has_light, items=None, adjacent_rooms=None):
        self.name = name
        self.description = description
        self.has_light = has_light
        self.items = [] if items is None else items
        self.adjacent_rooms = {} if adjacent_rooms is None else adjacent_rooms
    
    # look at the items in the room
    def list_items(self):
        # print using an f string and use a join on a comma to delimit the items and a for loop to loop over the item list
        print(f"\n In this room you see the following: {', '.join(item.name for item in self.items)}")
    # add_item same implementation as in the player class
    def add_item(self, item):
        self.items.append(item)

    # remove_item same implementation as in the player class
    def remove_item(self, item):
        del self.items[self.items.index(item)]

    # check room for specific item
    def check_for_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return True
        return False

    def __str__(self):
        return str(self.name) + "\n" + str(self.description)

