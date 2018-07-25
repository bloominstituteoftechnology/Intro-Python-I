# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name = "", room_description = "", room_items = []):
        self.room_name = room_name
        self.room_description = room_description
        self.room_items = room_items

    def item_found(self, item):  # found by player
        if len(self.room_items) > 0:
            itemIndex = -1
            for index, room_item in enumerate(self.room_items):
                if room_item.item_name == item:
                    itemIndex = index
            if itemIndex > -1:
                taken_item = self.room_items.pop(itemIndex)
                return taken_item
            else:
                return False
        else:
            return False

    def item_dropped(self, item):  # dropped by player
        self.room_items.append(item)

    def print_items(self):
        if len(self.room_items) == 0:
            return "This room seems to have no useable items"
        elif len(self.room_items) == 1:
            return "a {} can been seen".format(self.room_items[0])
        elif len(self.room_items) == 2:
            return "a {} and {} can be seen".format(self.room_items[0], self.room_items[1])
        else:
            return "{} can be seen".format(", ".join(item.item_name for item in self.room_items))

    def __repr__(self):
        return "{} \nRoom Description: {}".format(self.room_name, self.room_description)

    def __str__(self):
        return "{} \nRoom Description: {}".format(self.room_name, self.room_description)
