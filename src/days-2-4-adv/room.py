# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        if items is not None:
            self.items.append(items)

        if len(self.items) != 0:
            room_items_list = [item.name for item in self.items]

    def __str__(self):
        # description_list = [item.description for item in self.items]
        # if description_list is not None:
        return "{name}\n\n {description}\n\n".format(name = self.name, description=self.description)
        # else:
        #     return f"\n\n{self.name}\n\n {self.description}\n\n you see no items in this room."

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def getItemFromRoom(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            return None

    def dropItemInRoom(self, item):
        if item in self.items:
            return None
        else:
            self.items.append(item)
            return item
