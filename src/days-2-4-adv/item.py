class Item:
    """Item base class."""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        """Called every time the player takes an item."""
        pass

    def __str__(self):
        """Convert to string."""
        return self.description

class Treasure(Item):
    """A treasure that adds to your score the first time you pick it up."""
    def __init__(self, name, description, value):
        self.value = value
        self.picked_up = False
        super().__init__(name, description)

    def on_take(self, player):
        super().on_take(player)

        if not self.picked_up:
            player.score += self.value
            print(f"You get {self.value} points!")
            self.picked_up = True

class LightSource(Item):
    """An item that casts light."""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.lightsource = True