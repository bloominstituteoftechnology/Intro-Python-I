from player import Player

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}"

    def item_taken(self):
        print(f"{self.name} has been added to your inventory!")

    def item_dropped(self):
        print(f"{self.name} has been dropped!")
