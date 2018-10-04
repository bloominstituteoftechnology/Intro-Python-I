# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items, is_light):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.is_light = is_light
    def __str__(self):
        return f"\n    [{self.name}] \n\n    {self.description}\n"
    def getRoomInDirection(self, direction):
        if direction == "N":
            return self.n_to
        elif direction == "E":
            return self.e_to
        elif direction == "S":
            return self.s_to
        elif direction == "W":
            return self.w_to
        else:
            return None

