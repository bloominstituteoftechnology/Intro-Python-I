class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        pass

    def on_drop(self, player):
        pass

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.picked_up = False

    def on_take(self, player):
        if not self.picked_up:
            player.score += self.value
            self.picked_up = True

class LightSource(Item):
    def __init__(self, name, description): 
        super().__init__(name, description)      
