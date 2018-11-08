# TODO: Refactor weapon to own subclass of Item
class Item:
    def __init__(self, name, description, attack=0, defence=0, hp=0, vitality=0, intelligence=0, dexterity=0, wisdom=0, mp=0):
        self.name = name
        self.description = description
        self.attack = attack
        self.hp = hp
        self.mp = mp
        self.defence = defence
        self.vit = vitality
        self.int = intelligence
        self.dex = dexterity
        self.wis = wisdom

    # Return a formatted value of the Item class
    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

    def on_take(self, value):
        print(f'{self.name} has been picked up')


# TODO: Add more attributes
class Weapon(Item):
    def __init__(self, name, description, attack=0, defence=0, hp=0, vitality=0, intelligence=0, dexterity=0, wisdom=0, mp=0):
        super().__init__(name, description, attack, defence, hp, vitality, intelligence, dexterity, wisdom, mp)


# TODO: Add more attributes
class Shield(Weapon):
    def __init__(self, name, description, attack=0, defence=0, hp=0, vitality=0, intelligence=0, dexterity=0, wisdom=0, mp=0):
        super().__init__(name, description, attack, defence, hp, vitality, intelligence, dexterity, wisdom, mp)


# TODO: Add more attributes
class Armour(Shield):
    def __init__(self, name, description, attack=0, defence=0, hp=0, vitality=0, intelligence=0, dexterity=0, wisdom=0, mp=0):
        super().__init__(name, description, attack, defence, hp, vitality, intelligence, dexterity, wisdom, mp)


class Treasure(Item):
    def __init__(self, name, description, score=0, attack=0):
        super().__init__(name, description, attack)
        self.score = score
        self.taken = False

    def on_take(self):
        if self.taken is False:
            self.taken = True
            return self.score
        else:
            return 0
