from item import Item

class Potion(Item):
    def __init__(self, name, power):
        Item.__init__(self, name)
        self.power = power
        self.picked_up = False
        self.consumed = False
    # on_take method sets the picked_up value to True
    def on_take(self):
        self.picked_up = True

    def on_drop(self): pass

    def on_use(self, target): 
      if not self.consumed:
        print("you consumed a potion")
        target.health += self.power
        self.consumed = True
        self.name = "empty flask"
      else:
        print("this flask is empty you already drank the potion")