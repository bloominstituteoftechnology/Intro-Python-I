# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, playerName, currentRoom):
        self.playerName = playerName
        self.currentRoom = currentRoom
        self.inventory = inventory

    def __str__(self):
        return '{} is in the {}.'.format(self.playerName, self.currentRoom)
