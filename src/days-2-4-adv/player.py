from items import Item, Treasure, Torch
# Write a class to hold player information, e.g. what room they are in
# currently.

items = {
    'blade': Item("Blade", """A mighty blade of grass"""),
    'shield': Item("Shield", """A shield of slaying, because the best defense is a good offense"""),
    'sand': Item("Sand", """Pocket sand, shi shaw!"""),
    'coin': Treasure("Coin", """A golden coin worth 1 money""", 1),
    'jewel': Treasure("Jewel", """A shiny trinket worth 10 monies""", 10),
    'torch': Torch("Torch", """A bright fire on a stick that lights the way""")
}

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []
        self.netWorth = 0
#THIS CREATES THE PLAYER CLASS THAT
#DEFINES THE ATTRIBUTES OF PLAYER
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            if "torch" in self.inventory or "torch" in self.currentRoom.inventory or self.currentRoom.is_lit == True:
                print(f"\n\nnow entering {nextRoom}")
            else:
                print("n\nit's pitch black dark in here")
        else:
            print("\n\ncannot move in that direction")

    def look(self, direction=None):
        if direction is None:
            if "torch" in self.inventory or "torch" in self.currentRoom.inventory or self.currentRoom.is_lit == True:
                print(f"\n\ncurrently in {self.currentRoom}")
            else:
                print("\n\nit's too dark to see in here")
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                if "torch" in self.inventory or "torch" in nextRoom.inventory or nextRoom.is_lit == True:
                    print(f"\n\nin that direction is {nextRoom}")
                else:
                    print("\n\nit's too dark to see in that direction")    
            else:
                print("\n\nnothing in that direction")

    def takeItem(self, item):
        if "torch" in self.inventory or "torch" in self.currentRoom.inventory or self.currentRoom.is_lit == True:
            if len(self.currentRoom.inventory) > 0 and item in self.currentRoom.inventory:
                self.inventory.append(item)
                self.currentRoom.removeItem(item)
                print(f"\n\n===You picked up the {item}===")
                if item == "coin" or item == "jewel":
                    if items[item].taken == False:
                        items[item].pickingUp()
                        self.netWorth += items[item].value
                        print(f"\n\n Your net worth increases by {items[item].value}")
            else:
                print("\n\nitem not in room")
        else:
            print("\n\ncannot see in dark")

    def dropItem(self, item):
        if len(self.inventory) > 0 and item in self.inventory:
            if item == "torch":
                items[item].warning()
            self.inventory.remove(item)
            self.currentRoom.addItem(item)
            print(f"\n\nyou have dropped the {item}")
        else:
            print("\n\nyou dont have that item")

    def viewInventory(self):
        if len(self.inventory) > 0:
            print("\n===YOUR INVENTORY:\n")
            for item in self.inventory:
                print(f"{items[item].name}:\n{items[item].description}\n")
        else:
            print("you have no inventory")

    def viewNetWorth(self):
        print(f"\n\n===YOUR NETWORTH: {self.netWorth}===")