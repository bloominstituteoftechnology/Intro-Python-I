import random


class Items:
    def __init__(self, name, description, itemType):
        self.name = name
        self.description = description
        self.itemType = itemType


class Food(Items):
    def __init__(self, name, description, itemType, health):
        super().__init__(self, name, description, itemType)
        self.health = random.randint(health[0], health[1])
        self.currentHealth = self.health

    def eat(self, item):
        pass


class Treasure(Items):
    def __init__(self, name, description, value):
        super().__init__(self, name, description)
        self.value = value


class LightSource(Items):
    def __init__(self, name, description, energy):
        super().__init__(self, name, description)
        self.energy = energy
