class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return "Name: %s | Description: %s" %(self.name, self.description)
    def on_take(self, player):
        pass
    def on_drop(self, player):
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
        else: print("NO SCORE")
class LightSource(Item):
    def __init__(self, name, description):
         super().__init__(name, description)
         self.see = True
    def on_drop(self, player):
        super().on_drop(player)
        if self.see:
            print("If you drop this you won't be able to see")
            self.see = False:
            break
        else: print("Alright then")
