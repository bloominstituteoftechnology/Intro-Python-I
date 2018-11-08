class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take_item(self, player):
        #pass
        player.inventory.append(self)

class Treasure(Item):
    def __init__(self, name, description, value):
        self.value = 100
        self.picked_up = False
        super().__init__(name, description)
    def take_item(self, player):
         super().take_item(player)
         if not self.picked_up:
             player.score += self.value
             print(f'Your score increases by {self.value}!')
             self.picekd_up = True

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.light_source = True
        
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
