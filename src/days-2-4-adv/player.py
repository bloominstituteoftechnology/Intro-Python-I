# Write a class to hold player information, e.g. what room they are in currently.
from item import Item

items = {
    'katana': Item("Katana", """An extremely sharp single-edged sword"""),

    'spear': Item("Spear", """A wooden spear, useful for fishing"""),

    'broadsword': Item("Broadsword", """A heavy two-handed sword"""),

    'scimitar': Item("Scimitar", """A short curved blade, perfect for self-defense"""),

    'club': Item("Club", """A crudely fashioned club"""),
}

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []

    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(f"\n\nYou are in: {nextRoom}")
        else:
            print("\n\nYou cannot move in that direction.")

    def look(self, direction=None):
        if direction is None:
            print(f"\n\nYou are in: {self.currentRoom}")
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                print(f"\n\nYou see: {nextRoom}")
            else:
                print("\n\nThere is nothing there.")

    def pickUpItem(self, item):
        if len(self.currentRoom.inventory) > 0:
            if item in self.currentRoom.inventory:
                self.inventory.append(item)
                self.currentRoom.removeItem(item)
                print(f"\n\nYou have picked up the: {item}")
        else:
            print("\n\nThat item is not contained in this room.")

    def dropItem(self, item):
        if len(self.inventory) > 0:
            if item in self.inventory:
                self.inventory.remove(item)
                self.currentRoom.addItem(item)
                print(f"\n\nYou have dropped the: {item}")
        else:
            print("\n\nThat item is not contained in your inventory.")

    def seeInventory(self):
        if len(self.inventory) > 0:
            print("Your inventory includes:\n")
            for item in self.inventory:
                print(f"{items[item].name}:    {items[item].description}")
        else:
            print("There are no items in your inventory.")
        