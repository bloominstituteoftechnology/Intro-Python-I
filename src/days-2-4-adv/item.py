class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.obtained = False

    def __str__(self):
        return f'{self.name}: {self.description}'

    def on_take(self, player):
        self.obtained = True
        return f'You pick up the {self.name}'

    def on_drop(self):
        return f'You drop the {self.name}'

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def on_take(self, player):
        if self.obtained == False:
            player.add_score(self.value)
        return super().on_take(player)

    def on_drop(self):
        return super().on_drop()

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_take(self, player):
        return super().on_take(player)

    def on_drop(self):
        print("It's not wise to drop your source of light!")
        return super().on_drop()
