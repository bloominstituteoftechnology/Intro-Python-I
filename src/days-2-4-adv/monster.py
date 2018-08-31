from random import randint


class Monster():
    def _init__(self, name, hp):
        self.name = name
        self.hp = hp

    def on_attack(self, player):
        player.health -= randint(0, 9)
