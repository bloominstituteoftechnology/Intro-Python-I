# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = [] if items is None else items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def examine_room(self):
        print(f"\n You examine the room and find: {', '.join(item.name for item in self.items)}")

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        del self.items[self.items.index(item)]

    def __str__(self):
        return str(self.name) + "\n" + str(self.description)