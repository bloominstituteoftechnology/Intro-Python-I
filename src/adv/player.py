# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, playerName, startRoom):
        self.startRoom = startRoom
        self.playerName = playerName