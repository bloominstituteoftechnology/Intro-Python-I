class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

itemList = {
    'sword': Item("Sword", "The sword hums with a strange power"),
    'hat': Item("Hat", "The most uninteresting hat you've ever laid eyes upon"),
    'shield': Item("Shield", "Something cowards use to block attacks"),
    'torch': Item("Torch", "This torch burns bright"),
    'coin': Item("Coin", "Merchants accept this!"),
    'chest': Item("Treasure Chest", "This chest contains the grand gift of knowledge"),
    'armor': Item("Armor", "Protects you from bad people"),
    'telescope': Item("Telescope", "With this you can be a pirate")
}