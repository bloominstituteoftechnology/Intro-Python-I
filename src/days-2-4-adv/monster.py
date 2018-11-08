class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name                
        self.health = health
        self.attack_power = attack
        self.defense = defense
        self.killed = False
    def attack(self, target):
        target.health -= self.attack_power