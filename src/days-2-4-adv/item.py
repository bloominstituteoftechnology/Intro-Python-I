class Item:
    def __init__(self, name, description=''):
        self.name = name
        self.description = description
    def __repr__(self):
        return f'{self.name}'

class Treasure:
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value
    def __repr__(self):
        return f'{self.name} : {self.description}\n\n Estimated Value: {self.value}'