class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)


#alternate solution code from Beej
    # def __str__(self):
    #     return self.name
    
    # def __repr__(self):
    #     return self.name