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
    def __init__(self, name, description, itemType, weight, heal):
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
        if (self.value):
            print("You've picked up the {} and now have {} more points.".format(
                self.name, self.value))
        else:
            print("You've picked up the {}, but you already got the points.".format(self.name))
        self.value = 0


class LightSource(Items):
    def __init__(self, name, description, itemType, weight, energy):
        Items.__init__(self, name, description, itemType, weight)
        self.energy = energy


class Weapon(Items):
    def __init__(self, name, description, itemType, weight, damage):
        Items.__init__(self, name, description, itemType, weight)
        self.damage = damage
