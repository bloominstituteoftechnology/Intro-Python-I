class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f"Picked up {self.name}")
        return 0
    def on_drop(self):
        print(f"Dropped {self.name}")

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)

        self.value = value
        self.pickedUp = False
    def on_take(self):
        if self.pickedUp == False:
            self.pickedUp = True
            return self.value
        else:
            return 0

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    def on_drop(self):
        print("It's not wise to drop your source of light!")

