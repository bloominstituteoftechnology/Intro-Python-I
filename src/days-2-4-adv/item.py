from player import Player

 class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
     def take_item(self):
        print(f"{self.name} has been added to your inventory!")
