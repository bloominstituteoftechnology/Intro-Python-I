class Item:
    def __init__(self, name, description=''):
        self.name = name
        self.description = description
        self.acquired = False

    def __repr__(self):
        return f'{self.name}'

    def on_take(self, player):
        self.acquired = True

    def on_drop(self):
        return f'You have dropped {self.name}'

class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value

    def __repr__(self):
        return f'\n{self.name} : {self.description}'

    def on_take(self, player):
        if self.acquired == False:
            player.add_score(self.value)
            super().on_take(player)
        
    def on_drop(self):
        super().on_drop()

class LightSource(Item):
    def __init__(self, name, description=''):
        Item.__init__(self, name, description)
        self.name = name
    
    def __repr__(self):
        return f'{self.name}'

    def on_drop(self):
        print (f'\nIt\'s not wise to drop your source of light!')
            
        