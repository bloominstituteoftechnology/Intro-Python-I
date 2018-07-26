# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, playerName, currentRoom):
        self.playerName = playerName
        self.current_room = currentRoom
        self.inventory = []

    def __str__(self):
        return '{} is in the {}.'.format(self.playerName, self.current_room)
