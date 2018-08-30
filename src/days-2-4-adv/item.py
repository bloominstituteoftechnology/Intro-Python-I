class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Treasure(Item):
    def __init__(self, name, description, value):
        self.value = value
        Item.__init__(self, name, description)