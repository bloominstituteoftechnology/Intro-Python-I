from textwrap import wrap
from time import sleep

# Create Item class, arguments are name and description
class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.bound = None
    
    def on_take(self, player):
        pass

    def info(self):
        info_message = self.name + ':\t' + self.description
        return '\n'.join(wrap(info_message, width=50)) + '\n' + '-' * 50
        
class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def on_take(self, player):
        player.score = player.score + self.value

    def on_drop(self, player):
        player.score = player.score - self.value





