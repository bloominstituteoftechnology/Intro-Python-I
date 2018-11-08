from item import Item

class Computer(Item):
    def __init__(self, name, power=10):
        Item.__init__(self, name)
        self.power = power
        self.picked_up = False
        self.switched_on = False

    def on_take(self):
        self.picked_up = True

    def on_drop(self): pass

    def on_use(self, target): 
      if not self.switched_on:
        print("you powered up the " + self.name)
        self.switched_on = True
      else:
        print("the " + self.name + " is already on")