from player import Player

class Warrior(Player):
    def __init__(self):
        self.main_weapon = "Sword"
        self.second_weapon = "Shield"
        self.aggro_level = 10
        self.rage = 0
        
        print(self.main_weapon)
