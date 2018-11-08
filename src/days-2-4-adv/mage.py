from player import Player


class Mage(Player):
    def __init__(self):
        # super(self)
        self.mana = 100
        self.hp = 90
        self.armor = 40

    def arcane_blast(self, target):
        if self.mana >= 10:
            target.armor -= 15
        else:
            print("Not enough mana")
