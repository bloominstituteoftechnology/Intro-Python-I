class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


class Treasure(Item):
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value

