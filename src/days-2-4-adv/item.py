from player import Player

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"\n{self.name} added to inventory")

    def on_drop(self):
        print(f"\nYou have dropped the {self.name}")

class Treasure(Item):
    def __init__(self, name, description, value):
        self.value = value
        Item.__init__(self, name, description)
    def on_take(self):
        return self.value

class LightSource(Item):
    def __init__(self, name, description):
        Item.__init__(self, name, description)