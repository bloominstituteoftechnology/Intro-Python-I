class Item:
    def __init__(self, name):
        self.name = name    

    def on_take(self):
        pass

class Treasure(Item):
    def __init__(self, name, value):
        self.value = value
        super().__init__(name)

    def on_take(self):
        return self.value

class LightSource(Item):
    def __init__(self, lamp):
        self.lamp = lamp
        super().__init__()

    def on_drop(self):
        return "It's not wise to drop you light source"

# test = Treasure("Sword", "500 physical damage and 200 magicka", 500)

# print(test.on_take())
