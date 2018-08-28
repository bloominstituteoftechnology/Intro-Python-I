# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, spells, health, room):
        self.name = name
        self.spells = spells
        self.health = health
        self.room = room