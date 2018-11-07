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
        self.previous_room = room
        self.direction = 'north'
        self.inventory = []

    # Return a formatted value of the Player class
    def __str__(self):
        return f"Name: {self.name}, Room: {self.room}"

    def show_inventory(self):
        if len(self.inventory) < 1:
            print("No items in inventory")
            return

        for d in self.inventory:
            for key in d:
                print("{}: {}".format(key, d[key]))

    # Move the player north
    def move_north(self):
        # Set direction
        self.direction = 'north'

        # Set new room, else, set previous room to current room so
        # we don't have an infinite loop of the same room
        if self.room.n_to:
            self.previous_room = self.room
            self.room = self.room.n_to
        else:
            self.previous_room = self.room

    # Move the player south
    def move_south(self):
        self.direction = 'south'
        if self.room.s_to:
            self.previous_room = self.room
            self.room = self.room.s_to
        else:
            self.previous_room = self.room

    # Move the player east
    def move_east(self):
        self.direction = 'east'
        if self.room.e_to:
            self.room = self.room.e_to
        else:
            self.previous_room = self.room

    # Move the player west
    def move_west(self):
        self.direction = 'west'
        if self.room.w_to:
            self.room = self.room.w_to
        else:
            self.previous_room = self.room
