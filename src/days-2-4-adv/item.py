#Implements a class to hold item information. Will have name and
#description attributes

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return '{}: {}'.format(self.name, self.description)
    def on_take(self):
        print(f'\x1b[1;27;42m -You have obtained {self.name}!- \x1b[0m')
        return 0
    def on_drop(self):
        print(f'\x1b[1;27;42m -You dropped {self.name}!- \x1b[0m')

class Treasure(Item):
    def __init__(self, name, description, value, notTakenBefore=True):
        super().__init__(name, description)
        self.value = value
        self.notTakenBefore = notTakenBefore
    def __str__(self):
        return '(Treasure!) {}: {}, Value: {}\n'.format(self.name, self.description, self.value)
    def on_take(self):
        if self.notTakenBefore:
            print(f'\x1b[1;27;42m -Treasure obtained! You took {self.name}! {self.value} points to Gryffindor!- \x1b[0m')
            self.notTakenBefore = False
            return self.value
        else:
            print(f'\x1b[1;27;42m -Slimy fingered, ornery knave, lazy bum! You dropped your {self.name} and tried to pick it up again. No points for you!- \x1b[0m')
            return 0

class LightSource(Item):
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return '(Light Source) {}: {}\n'.format(self.name, self.description)
    def on_drop(self):
        print(f"\x1b[1;27;42m It's not wise to drop your source of light! \x1b[0m")
