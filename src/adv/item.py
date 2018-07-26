class Item:
    def __init__(self, name, adjectives, description):
        self.name = name
        self.adjectives = adjectives  
        self.description = description

    def __str__(self):
        adjectives = ", ".join(self.adjectives)
        return f"a {adjectives} {self.name}"