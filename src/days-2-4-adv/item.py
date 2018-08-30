class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description 
    def getDescription(self):
        return self.description
    def getName(self):
        return self.name
    
class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__int__(self, name, description)

class LightSource(Item):
    def __init__(self, name, description):
        Item.__int__(self, name, description)
