class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
