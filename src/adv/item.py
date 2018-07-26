class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def takes(self, player):
        pass


class Treasure(Item):
    def __init__(self, name, description, value):
        self.value = value
        self.owned = False
        super().__init__(name, description)

    def on_take(self, player):
        super().takes(player)

        if not self.owned:
            player.score += self.value
            print(f"You get {self.value} points!")
            self.picked_up = True
