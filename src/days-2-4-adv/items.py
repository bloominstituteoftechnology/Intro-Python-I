import random


class Items:
    def __init__(self, name, description, itemType, weight):
        self.name = name
        self.description = description
        self.itemType = itemType
        self.weight = weight

    def on_take(self, player):
        print("You've picked up the {}".format(self.name))


class Food(Items):
    def __init__(self, name, description, itemType, heal, weight):
        Items.__init__(self, name, description, itemType, weight)
        self.heal = heal  # random.randint(health[0], health[1])
        self.currentHeal = self.heal

# class Weapon(Items):


class Treasure(Items):
    def __init__(self, name, description, itemType, weight, value):
        Items.__init__(self, name, description, itemType, weight)
        self.value = value

    def on_take(self, player):
        # self.on_take = False
        player.score += self.value
        self.value = 0
        # print('does this run/work')
        # return player.score


class LightSource(Items):
    def __init__(self, name, description, itemType, weight, energy):
        Items.__init__(self, name, description, itemType, weight)
        self.energy = energy


class Weapon(Items):
    def __init__(self, name, description, itemType, weight, damage):
        Items.__init__(self, name, description, itemType, weight)
        self.damage = damage
