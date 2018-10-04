# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    cannotMove = 'You cannot move in that direction.'
    def __init__(self, name, roomLocation):
        self.name = name
        self.roomLocation = roomLocation
    def travel(self, direction):
        nextRoom = None
        if direction == 'n':
            if self.roomLocation.n_to is not None:
                nextRoom = self.roomLocation.n_to
        elif direction == 's':
            if self.roomLocation.s_to is not None:
                nextRoom = self.roomLocation.s_to
        elif direction == 'e':
            if self.roomLocation.e_to is not None:
                nextRoom = self.roomLocation.e_to
        elif direction == 'w':
            if self.roomLocation.w_to is not None:
                nextRoom = self.roomLocation.w_to
        if nextRoom is not None:
            self.roomLocation = nextRoom
            print(nextRoom)
        else:
            print(self.cannotMove)