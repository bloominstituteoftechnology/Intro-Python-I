class Item:
    def __init__(self, name, description, attributes = {}):
        self.name = name
        self.description = description
        self.attributes = attributes

class Potion (Item):
    def __init__(self, name, description, attributes):
        super().__init__(name + ' potion', description, attributes)
        
    def use_item(self, player):
        for key in self.attributes:
            player[key] += self.attributes[key]
        


redPotion = Potion('red', 'This potion heals 4 health points', {
    "hp": 4
})
