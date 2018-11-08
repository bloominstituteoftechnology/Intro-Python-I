class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take_item(self, player):
        pass

class Potion(Item):
    def __init__(self, name, description, health):
        self.health = health
        self.picked_up = False
        super().__init__(name, description)

    def take_item(self, player):
        super().take_item(player)

    def consume(self, player):
        #super().take_item
        if not self.picked_up:
            player.health += self.health
            print(f"Your get {self.health} health!")
            self.picked_up = True
