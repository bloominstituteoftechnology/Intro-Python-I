class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(self.name, 'picked up!')

    def on_drop(self):
        print(self.name, 'has been dropped.')

class Treasure(Item):
    def __init__(self, value, name, description):
        super().__init__(name, description)
        self.value = value

    def on_take(self):
        points = self.value
        self.value = 0
        print(self.name, 'picked up!')
        return points

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.isLightSource = True

    def on_drop(self):
        print('It\'s not wise to drop your light source!')
