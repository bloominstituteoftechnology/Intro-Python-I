# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

items = {
    'katana': Item("Katana", """An extremely sharp single-edged sword"""),

    'spear': Item("Spear", """A wooden spear, useful for fishing"""),

    'broadsword': Item("Broadsword", """A heavy two-handed sword"""),

    'scimitar': Item("Scimitar", """A short curved blade, perfect for self-defense"""),

    'club': Item("Club", """A crudely fashioned club"""),
}

class Room:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        inv = inventory.split(" ")
        self.inventory = [*inv]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"~~ {self.name} ~~\n\n   {self.description}\n\n   Visible items: {self.inventory}"

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def removeItem(self, item):
                self.inventory.remove(item)

    def addItem(self, item):
                self.inventory.append(item)