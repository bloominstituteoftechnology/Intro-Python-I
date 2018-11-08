# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.MaxHp = hp
        self.maxMp = mp

    def attack(self, other):
        pass