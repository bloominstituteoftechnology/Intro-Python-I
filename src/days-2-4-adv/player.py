# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    cannotMove = 'You cannot move in that direction.'
    nothingThere = 'There is nothing to see.'
    def __init__(self, name, roomLocation):
        self.name = name
        self.roomLocation = roomLocation
        self.items = []
    def travel(self, direction):
        nextRoom = self.roomLocation.getRoomInDirection(direction)
        if nextRoom is not None:
            self.roomLocation = nextRoom
            print(f'\n{nextRoom}\n')
        else:
            print(f'\n{self.cannotMove}\n')
    def look(self, direction):
        nextRoom = self.roomLocation.getRoomInDirection(direction)
        if nextRoom is not None:
            print(f'\n{nextRoom}\n\nYou are still in {self.roomLocation}\n')
        else:
            print(f'\n{self.nothingThere}\n\nYou are still in:{self.roomLocation}\n')
