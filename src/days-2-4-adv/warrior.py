from player import Player

class Warrior(Player):
    def __init__(self):
        self.main_weapon = 'sword'
        self.second_weapon = 'shield'

    def enrage(self):
        if self.rage >= 5:
            self.health += 20
            self.movement_speed += 5
        else:
            print('nto enough rage')
