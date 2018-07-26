class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self): # creates string representation of obj
        return self.name 

    def __repr__(self): # dispays the object 
        return self.name

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
