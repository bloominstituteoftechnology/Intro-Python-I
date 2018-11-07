from player import Player


class Warrior(Player):
    def __init__(self):
        self.main_weapon = "Barbed sword"
        self.hp = 140
        self.rage = 0
        self.armor = 100

    def thrash(self, target):
        target.health -= (20 + (100 / target.armor * 5))

    def eye_for_an_eye(self, target):
        if self.hp > 20:
            target.hp -= 20
            self.hp -= 20
        else:
            print("You'll kill yourself!")
