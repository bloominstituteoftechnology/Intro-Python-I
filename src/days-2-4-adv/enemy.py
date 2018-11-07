import random
from item import Item

class Enemy:
    def __init__(self, room, name, items=None, health=100):
        self.room = room
        self.name = name
        self.items = [] if items is None else items
        self.gold = 20
        self.health = health
        self.attack = 3
        self.alive = True

    def take_damage(self, dmg):
      if self.alive:
        print("the " + self.name + " took " + str(dmg) + " damage")
        self.health -= (dmg + random.randrange(1, 20))
        if self.health <= 0:
          print("the " + self.name + " died from the battle")
          self.alive = False