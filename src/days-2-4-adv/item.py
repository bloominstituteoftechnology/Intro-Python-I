class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self, player, room):
        player.inventory.append(self)
        room.inventory.remove(self)
        print("You have taken the %s." % self.name)
    def on_drop(self, player, room):
        player.inventory.remove(self)
        room.inventory.append(self)
        print("You have dropped the %s." % self.name)

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.takenAlready = False
    def on_take(self, player, room):
        self.takenAlready = True
        player.inventory.append(self)
        room.inventory.remove(self)
        print("You have taken the %s." % self.name)

class Lightsource(Item):
    def __init__ (self, name, description):
        super().__init__(name, description)
        