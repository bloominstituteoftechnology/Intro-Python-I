from printing import prompt

class Item:
    def __init__(self, name, adjectives, description):
        self.name = name
        self.adjectives = adjectives  
        self.description = description
        self.uncollected = True

    def on_take(self, player):
        self.uncollected = False
        prompt(f"{player} collects the {self} from the {player.room}")
        return True

    def on_drop(self, player):
        prompt(f"{player} drops the {self} in the {player.room}")
        return True

    def __str__(self):
        adjectives = ", ".join(self.adjectives)
        return f"{adjectives} {self.name}"
