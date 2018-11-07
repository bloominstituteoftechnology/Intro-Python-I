class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.owner = None
        self.first = True

    def __str__(self):
        return f'{self.name}: {self.desc}'

    def on_take(self, player):
        self.owner = player

    def on_drop(self):
        self.owner = None
        return True


class Treasure(Item):
    def __init__(self, name, desc, value):
        super().__init__(name, desc)
        self.value = value

    def on_take(self, player):
        self.owner = player
        if self.first:
            self.owner.score += self.value
            self.first = False

    def __str__(self):
        return f'*Treasure* {self.name}: {self.desc} Value: {self.value}'


class LightSource(Item):
    def __init__(self, name, desc):
        super().__init__(name, desc)

    def on_drop(self):
        print('Do not drop it!')
        choice = input(
            'Do you still want to drop your lamp? y/n \n')
        if choice == 'y':
            self.owner = None
            return True
        else:
            return False
