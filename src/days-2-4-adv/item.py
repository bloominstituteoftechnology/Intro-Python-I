class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup(self, player):
        player.inventory.append(self)
