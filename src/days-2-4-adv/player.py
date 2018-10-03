# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    cannotMove = 'You cannot move in that direction.'
    def __init__(self, roomLocation):
        self.roomLocation = roomLocation