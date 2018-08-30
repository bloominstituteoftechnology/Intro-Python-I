class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        pass

class Treasure(Item):
    def __init__(self, name, description, value):
        self.value = value
        self.picked_up = False

    def on_take(self, player):
        if not self.picked_up:
            player.score += self.value
            self.picked_up = True
        
