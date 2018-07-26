class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Treasure(Item):
    def __init__(self, name, description, value=1, taken=False):
        self.name = name
        self.description = description
        self.value = value
        self.taken = taken

    def on_take(self, player):
        if self.taken == False:
            player.score += self.value
            self.taken = True
