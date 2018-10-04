class Item:
    def __init__(self, name, description=''):
        self.name = name
        self.description = description
        self.acquired = False

    def __repr__(self):
        return f'{self.name}'

    def on_take(self, player):
        self.acquired = True
        # print (f'You have acquired {self.name}')

class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value

    def __repr__(self):
        return f'\n{self.name} : {self.description}\n\n Estimated Value: {self.value}'

    def on_take(self, player):
        if self.acquired == False:
            player.add_score(self.value)
        return super().on_take(player)
            
        