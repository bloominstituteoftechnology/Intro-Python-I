# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, is_light, items =[]):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.items = items
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None

    def __str__(self):
        return '{}\n{}'.format(self.name, self.description)

    def getRoomDirection(self, direction):
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
