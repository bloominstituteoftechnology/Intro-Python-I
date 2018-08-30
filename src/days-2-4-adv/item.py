class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f'{self.name}'
    def __str__(self):
        return f'{self.name}'
    def getDescription(self):
        return self.description
    def on_drop(self):
        print(f'\nYou have dropped {self.name}')
    

class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value
        self.oneTime = True
    def on_take(self, player):
        if self.oneTime:
            player.score += self.value
            print(f'You got {self.name} and scored: {self.value}')
            self.oneTime = False
        else:
            print(f'You got a score for {self.name} before')
        
    
class LightSource(Item):
    def __init__(self, name, description):
        Item.__init__(self, name, description)
        self.name = name

    def on_drop(self):
        print "It's not wise to drop your source of light!"