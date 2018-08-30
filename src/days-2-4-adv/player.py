# Write a class to hold player information, e.g. what room they are in
# currently.
from random import *


class Player:
    def __init__(self, name, location, health):
        self.name = name
        self.location = location
        self.inventory = {}
        self.health = health
        self.score = 0

    def take(self, item):
        for key in self.inventory:
            if key == item:
                self.inventory[key] += 1
                return True
        self.inventory[item] = 1

    def drop(self, item):
        for key in self.inventory:
            if key == item:
                if self.inventory[key] > 0:
                    self.inventory[key] -= 1
                    # if inventory is 0, delete
                    if self.inventory[key] == 0:
                        del self.inventory[key]
                    return True
        print("You don't have a {} to drop.\n".format(item))

    def eat(self, item):
        self.health += item.heal
        self.inventory[item.name] -= 1
        if self.inventory[item.name] <= 0:
            del self.inventory[item.name]

    def attack(self, item, player):  # pass in monster object for monster.health
        # if (battle()): # might not be needed because already in battle
        if(random() >= .3):
            player.health -= item.damage
            print("{} dealt {} damage!".format(self.name, item.damage))
        else:
            print("You missed!")

    def getInventory(self):
        return self.inventory

    def getScore(self):
        print(self.score)

    def getStatus(self):
        print(f'Name: \t\t{self.name}')
        print(f'Health: \t{self.health}')
        print(f'Score: \t\t{self.score}')

    def equip(self, item):
        print("You have been equipped! with {}.\n".format(item))
    # def addScore(self, value):
    #     self.score += value
