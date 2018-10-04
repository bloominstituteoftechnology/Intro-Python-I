# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description 
        self.n_to = None # North to
        self.s_to = None # South to
        self.e_to = None # East to
        self.w_to = None # West to
        self.items = []
    def __str__(self):
        return f'\n{self.name}\n    {self.description}\n'
    def getRoomInDirection(self, direction):
        if direction == 'n':
            return self.n_to
        if direction == 's':
            return self.s_to
        if direction == 'e':
            return self.e_to
        if direction == 'w':
            return self.w_to
        else:
            return None