class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.lightSource = True