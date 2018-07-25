# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []

    def change_location(self, new_location):
        self.location = new_location

    def drop(self, item):  # player drops this
        if len(self.inventory) > 0:
            itemIndex = -1
            for index, inv_item in enumerate(self.inventory):
                if inv_item.item_name == item:
                    itemIndex = index
            if itemIndex > -1:
                droppedItem = self.inventory.pop(itemIndex)
                return droppedItem
            else:
                return False
        else:
            return False
    
    def pick_up(self, item):  # player picks this up
        self.inventory.append(item)

    def print_inv(self):
        if len(self.inventory) == 0:
            return "Empty"
        else:
            return ", ".join(item.item_name for item in self.inventory)

    def __repr__(self):
        return "Current Location: {}".format(self.location)
    
    def __str__(self):
        return "Current Location: {}".format(self.location)