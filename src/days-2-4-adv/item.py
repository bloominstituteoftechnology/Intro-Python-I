class Item:
    def __init__(self, name, description):
        self.name = name

    def on_drop(self):
        print(f"You have dropped {self.name}.")



class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value
        self.is_picked = False

class LightSource(Item):
    def __init__(self, name, description):
        Item.__init__(self, name, description)

    def on_drop(self):
        print(f"It's not wise to drop your source of light!")
        print(f"You have dropped {self.name}.")
