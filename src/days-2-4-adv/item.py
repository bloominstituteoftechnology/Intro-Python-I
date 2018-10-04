class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.pickedup = False

    def onTake(self, player):
        if not self.pickedup:
            player.score += self.value
