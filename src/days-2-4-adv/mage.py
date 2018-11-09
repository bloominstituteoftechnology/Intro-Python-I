import random
from player import Player

class Mage:
    def __init__(self):
        self.mana = 100
        self.intelligence = 150

    def frostbolt(self, target):
        if self.mana >= 20:
            target.health -= random.randrange(30, 61)
            target.movement_speed = 2
        else:
            print('not enough mana')