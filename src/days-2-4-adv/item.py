class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description  
class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.lightsource = True        
class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.treasure = True
        self.collected = False
class Weapon(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.attack = value
        self.equippable = True