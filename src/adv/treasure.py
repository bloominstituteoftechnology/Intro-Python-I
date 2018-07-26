from item import Item
from printing import prompt

class Treasure(Item):
    def __init__(self, value, *args):
        super().__init__(*args)
        self.value = value

    def on_take(self, player):
        uncollected = self.uncollected
        super().on_take(player)

        if uncollected:
            player.add_score('items', self.value)
            prompt(f"{self.value} points added to {player}'s item score.")
            