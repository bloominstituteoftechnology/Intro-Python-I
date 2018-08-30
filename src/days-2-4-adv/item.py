class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f"{self.name} Added to inventory!")
    def on_drop(self):
        print(f"{self.name} Removed from inventory!")

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    def on_drop(self):
        print(f"It's not wise to drop your source of light!")

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

itemList = {
    'sword': Item("Sword", "The sword hums with a strange power"),
    'hat': Item("Hat", "The most uninteresting hat you've ever laid eyes upon"),
    'shield': Item("Shield", "Something cowards use to block attacks"),
    'torch': LightSource("Torch", "This torch burns bright"),
    'coin': Treasure("Coin", "Merchants accept this!", 1),
    'ruby': Treasure("Ruby", "Lovely red shine! Merchants will pay a hefty sum for this!", 20),
    'diamond': Treasure("Diamond", "Shine bright like a diamond! Very Expensive!", 35),
    'chest': Item("Treasure Chest", "This chest contains the grand gift of knowledge"),
    'armor': Item("Armor", "Protects you from bad people"),
    'telescope': Item("Telescope", "With this you can be a pirate"),
    'lamp': LightSource("Lamp", "It's like a torch, but better!")
}
