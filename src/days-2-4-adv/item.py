class Item:
    def __init__(self, name, description):
        self.name = name
    def takeItem(self, player):
        player.items.append(self)
        player.currentRoom.items.remove(self)
    def dropItem(self, player):
        player.items.remove(self)
        player.currentRoom.items.append(self)
        
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

class LightSource(Item):
    def __init__(self, name, description,):
        Item.__init__(self, name, description)
    def takeItem(self, player):
        player.items.append(self)
        player.currentRoom.items.remove(self)
    def dropItem(self, player):
        player.items.remove(self)
        player.currentRoom.items.append(self)
        print("It's not wise to drop your source of light")

