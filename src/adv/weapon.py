from item import Item

class Weapon(Item):
    def __init__(self, damage, *args):
        super().__init__(*args)
        self.damage = damage

    def __str__(self):
        return self.name