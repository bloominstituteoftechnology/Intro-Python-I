class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.pickedUp = False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def inspect(self):
        return self.name + ': ' + self.description

    def onTake(self, player):
        pass


class Treasure(Item):
    def __init__(self, name, description, points):
        super().__init__(name, description)
        self.points = points

    def onTake(self, player):
        if self.pickedUp == False:
            self.pickedUp = True
            player.score += self.points


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
