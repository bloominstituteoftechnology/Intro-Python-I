class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def onTake(self, player):
        player.items.append(self)
        player.room.items.remove(self)
        print(f'You have grabbed {self.name}')

    def onDrop(self, player):
        player.items.remove(self)
        player.room.items.append(self)
        print(f'You have dropped {self.name}')


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.pickedup = False

    def onTake(self, player):
        super().onTake(player)
        if not self.pickedup:
            player.score += self.value

    def onDrop(self, player):
        super().onDrop(player)
        if not self.pickedup:
            self.pickedup = True


class LightSource(Item):
    def __init__(self):
        super().__init__("Lamp", "Lights up the world")
