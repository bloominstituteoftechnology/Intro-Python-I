from player import Player


class Warrior(Player):
    def __init__(self):
        self.main_weapon = "Barbed sword"
        self.health = 140
        self.rage = 0

    def thrash(self, target):
        target.health -= 20
