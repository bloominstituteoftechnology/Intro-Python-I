class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return "Name: %s | Description: %s" %(self.name, self.description)
    def on_take(self, player):
        pass
class Treasure(Item):
    def __init__(self, name, description, score):
        self.score = score
        self.had = False
        super().__init__(name, description)
    def on_take(self, player):
        super().on_take(player)
        if not self.had:
            player.score += self.score
            print("SCORED")
            self.had = True
