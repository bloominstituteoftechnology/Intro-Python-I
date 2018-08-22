# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    n_to=None
    s_to=None
    e_to=None
    w_to=None
    def __init__(self, name="DEFAULT NAME", description="DEFAULT DESCRIPTION"):
        self.name = name
        self.description = description
    def connect(self, room, direction):
        if direction == 'n':
            self.n_to = room
            room.s_to = self
        elif direction == 's':
            self.s_to = room
            room.n_to = self
        elif direction == 'e':
            self.e_to = room
            room.w_to = self
        elif direction == 'w':
            self.w_to = room
            room.e_to = self
    def __str__(self):
        return "%s:\n%s" % (self.name, self.description)

