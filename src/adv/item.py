from printing import prompt

class Item:
    def __init__(self, name, adjectives, description):
        self.name = name
        self.adjectives = adjectives  
        self.description = description
        self.uncollected = True

    def on_take(self, player):
        self.uncollected = False
        prompt(f"{player.name} collects the {self.name} from the {player.room.name}")

    def __str__(self):
        adjectives = ", ".join(self.adjectives)
        return f"a {adjectives} {self.name}"