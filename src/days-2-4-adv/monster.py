import random
class Monster:
  def __init__(self, name, hp, low_attack, high_attack):
    self.name = name
    self.hp = hp
    self.low_attack = low_attack
    self.high_attack = high_attack
  def __str__(self):
    return str(f"{self.name}")
  def attack(self):
    return random.randrange(self.low_attack, self.high_attack, 1)