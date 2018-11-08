class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        # Called when player takes an item
        pass

    def __str__(self):
        # Convert to string
        return self.description