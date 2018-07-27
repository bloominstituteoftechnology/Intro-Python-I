

# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items, treasure, light):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
        self.treasure = treasure
        self.light = light
        self.is_light = False
