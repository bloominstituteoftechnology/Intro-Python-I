# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def get_rooms(self, destination):
        if destination == "n":
           if self.n_to is not None:
                return self.n_to
        elif destination == "e":
            if self.e_to is not None:
                return self.e_to
        elif destination == "s":
            if self.s_to is not None:
                return self.s_to
        elif destination == "w":
            if self.w_to is not None:
                return self.w_to
        else:
            print('You cannot move in that direction')
    def remove_item(self, item):
        chosen = ''
        for items in self.items:
            if items == item:
                chosen = item
        self.items.remove(chosen)
    def add_item(self, item):
        self.items.append(item)
        