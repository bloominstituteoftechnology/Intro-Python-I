# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    def getRoomInDirection(self, direction):
        if direction == 'north':
            return self.n_to
        elif direction == 'east':
            return self.e_to
        elif direction == 'south':
            return self.s_to
        elif direction == 'west':
            return self.w_to
        else:
            return None