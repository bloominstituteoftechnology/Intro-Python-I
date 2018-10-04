# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
 
items = {
    'Jar of Fairies': Item("Jar of Fairies","""Each fairy is used to guide you North, South, East and West"""),
     'Magic Roomba': Item("Magic Roomba","""Removes the dust so you can see better"""),
     'A golden septor': Item("A golden septor", """to protect you from danger"""),
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

