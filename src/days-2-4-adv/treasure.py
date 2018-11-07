from item import Item

class Treasure(Item):
    def __init__(self, name, value):
        Item.__init__(self, name)
        self.value = value
        self.picked_up = False
    # on_take method sets the picked_up value to True
    def on_take(self):
        self.picked_up = True

    def on_drop(self): pass