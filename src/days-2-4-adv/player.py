# Write a class to hold player information, e.g. what room they are in
# currently.

"""Return a player object

Player holds player name, room and direction information and movement
methods.
"""


class Player:
    # Initialize the properties of the class
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.direction = 'north'

    # Return a formatted value of the Player class
    def __str__(self):
        return f"Name: {self.name}, Room: {self.room}"

    # Move the player north
    def move_north(self):
        self.direction = 'north'
        if self.room.n_to:
            self.room = self.room.n_to

    # Move the player south
    def move_south(self):
        self.direction = 'south'
        if self.room.s_to:
            self.room = self.room.s_to

    # Move the player east
    def move_east(self):
        self.direction = 'east'
        if self.room.e_to:
            self.room = self.room.e_to

    # Move the player west
    def move_west(self):
        self.direction = 'west'
        if self.room.w_to:
            self.room = self.room.w_to
