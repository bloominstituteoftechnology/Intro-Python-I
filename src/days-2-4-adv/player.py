# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, health, mana, startingLocation):
        self.health = 100
        self.mana = 100
        self.location = "outside"