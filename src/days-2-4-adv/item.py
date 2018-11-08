class Item:
    def __init__(self, name, description, attack=0, is_weapon=False):
        self.name = name
        self.description = description
        self.is_weapon = is_weapon
        self.attack = attack

    # Return a formatted value of the Item class
    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"
