#Implements a class to hold item information. Will have name and
#description attributes

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return '{}: {}'.format(self.name, self.description)

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def __str__(self):
        return '(Treasure!) {}: {}, Value: {}\n'.format(self.name, self.description, self.value)
