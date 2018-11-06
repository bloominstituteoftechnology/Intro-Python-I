# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.direction = 'north'

    def __str__(self):
        return f"Name: {self.name}, Room: {self.room}"

    def move_north(self):
        self.direction = 'north'
        if self.room.n_to:
            self.room = self.room.n_to

    def move_south(self):
        self.direction = 'south'
        if self.room.s_to:
            self.room = self.room.s_to

    def move_east(self):
        self.direction = 'east'
        if self.room.e_to:
            self.room = self.room.e_to

    def move_west(self):
        self.direction = 'west'
        if self.room.w_to:
            self.room = self.room.w_to

