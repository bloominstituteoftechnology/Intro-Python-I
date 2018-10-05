from player import Player
from room import Room

class Item:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    def __str__(self):
        return self.name
    def on_drop(self):
        print(f"You have dropped {self.name}.")
    def room_items(self):
        if len(self.items) is not 0:
            print('\nThis room contains: ')
            for i, item in enumerate(self.items):
                print(str(i) + ' -> ' + item.name + ': ' + item.description)

class Treasure(Item):
    def __init__(self, name, description, value, beenScored):
        Item.__init__(self, name, description)
        self.value = value
        self.beenScored = False
    def takeItem(self, player):
        player.items.append(self)
        player.currentRoom.items.remove(self)
        if self.beenScored is False:
            player.score += self.value
            self.beenScored = True
    def dropItem(self, player):
        player.items.remove(self)
        player.currentRoom.items.append(self)

class LightSource(Item):
    def __init__(self, name, description,):
        Item.__init__(self, name, description)
    def takeItem(self, player):
        player.items.append(self)
        player.currentRoom.items.remove(self)
    def dropItem(self, player):
        player.items.remove(self)
        player.currentRoom.items.append(self)


