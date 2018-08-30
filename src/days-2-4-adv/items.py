import random


class Items:
    def __init__(self, name, description, itemType):
        self.name = name
        self.description = description
        self.itemType = itemType

    def on_take(self):
        print("You've picked up the {}".format(self.name))


class Food(Items):
    def __init__(self, name, description, itemType, heal):
        Items.__init__(self, name, description, itemType)
        self.heal = heal # random.randint(health[0], health[1])
        self.currentHeal = self.heal
        
# class Weapon(Items):

class Treasure(Items):
    def __init__(self, name, description, itemType, value):
        Items.__init__(self, name, description, itemType)
        self.value = value
    
    def on_take(self, player):
        # self.on_take = False
        player.score += self.value
        # print('does this run/work')
        # return player.score


class LightSource(Items):
    def __init__(self, name, description, energy):
        Items.__init__(self, name, description)
        self.energy = energy
