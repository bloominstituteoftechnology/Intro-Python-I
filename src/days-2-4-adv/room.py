# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        current_items = ', '.join(item.name for item in self.items)
        return f'\n\n{self.name}\n\n {self.description}\n\n You find the following items within... {current_items}'
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