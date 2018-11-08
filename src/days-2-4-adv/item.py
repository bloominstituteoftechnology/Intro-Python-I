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

    def on_take(self):
        print(f'{self.name} has been picked up')

    def on_drop(self):
        print(f'{self.name} has been dropped')


# TODO: Add more attributes
class Weapon(Item):
    def __init__(self, name, description, attack=0, defence=0, hp=0, vitality=0, intelligence=0, dexterity=0, wisdom=0, mp=0):
        super().__init__(name, description, attack, defence, hp, vitality, intelligence, dexterity, wisdom, mp)


# TODO: Add more attributes
class Shield(Item):
    def __init__(self, name, description, attack=0, defence=0, hp=0, vitality=0, intelligence=0, dexterity=0, wisdom=0, mp=0):
        super().__init__(name, description, attack, defence, hp, vitality, intelligence, dexterity, wisdom, mp)


# TODO: Add more attributes
class Armour(Item):
    def __init__(self, name, description, attack=0, defence=0, hp=0, vitality=0, intelligence=0, dexterity=0, wisdom=0, mp=0):
        super().__init__(name, description, attack, defence, hp, vitality, intelligence, dexterity, wisdom, mp)


class Treasure(Item):
    def __init__(self, name, description, gold):
        super().__init__(name, description)
        self.gold = gold
        self.taken = False

    def on_take(self):
        self.taken = True

    def is_taken(self):
        if self.taken:
            return True
        else:
            return False


class Lightsource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print('It\'s not wise to drop your source of light!')
