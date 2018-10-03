class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.owner = None
        self.first = True

    def __str__(self):
        return f'{self.name}: {self.desc}'

    def on_take(self, player):
        self.owner = player


class Treasure(Item):
    def __init__(self, name, desc, value):
        super().__init__(name, desc)
        self.value = value

    def on_take(self, player):
        self.owner = player
        if self.first:
            self.owner.score += self.value
            self.first = False

    def on_drop(self):
        self.owner = None
