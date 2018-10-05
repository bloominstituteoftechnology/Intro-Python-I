
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return self.name
    def on_drop(self):
        print(f"You have dropped {self.name}.")

class Food(Item):
    def __init__(self, name, description, calories):
        Item.__init__(self, name, description)
        self.calories = calories
    def eat(self):
        return self.calories
    def on_drop(self):
        print(f"You have dropped {self.name}.\nIt's not nice to play with your food!")

class Egg(Food):
    def __init__(self):
        self.name = "Egg"
        self.description = "This is an egg."
        self.calories = 50
    def eat(self):
        return 0
    def on_drop(self):
        self.name = "Broken Egg"
        self.description = "This is a broken egg."
        print(f"You have dropped an egg and now it's broken.")




# ---------------------------------------------------------------------------------------------------------

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    def __str__(self):
        return f"\n\n{self.name}\n\n   {self.description}\n\n{self.getItemsString()}\n"
    def printRoomDescription(self, player):
        if player.hasLight():
            print(str(self))
        else:
            print("You cannot see anything.")
    def getItemsString(self):
        return f"The room contains: {', '.join([item.name for item in self.items])}"
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
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None



# -------------------------------------------------------------------------------------------------------------

class Player:
    def __init__(self, name, currentRoom, startingItems=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.items = startingItems
        self.strength = 10
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            nextRoom.printRoomDescription(player)
        else:
            print("You cannot move in that direction.")
    def look(self, direction=None):
        if direction is None:
            self.currentRoom.printRoomDescription(player)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                nextRoom.printRoomDescription(player)
            else:
                print("There is nothing there.")
    def printStatus(self):
        print(f"Your name is {self.name}, your strength is {self.strength}")
    def printInventory(self):
        print("You are carrying:\n")
        for item in self.items:
            print(f"  {item.name} - {item.description}\n")
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
    def hasLight(self):
        return True
    def dropItem(self, itemName):
        itemToDrop = self.findItemByName(" ".join(itemName))
        if itemToDrop is not None:
            self.removeItem(itemToDrop)
            self.currentRoom.addItem(itemToDrop)
            itemToDrop.on_drop()
        else:
            print("You are not holding that item.")



# -------------------------------------------------------------------------------------------

# from room import Room
# from player import Player
# from item import Item, Food, Egg

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
rock1 = Item("Rock", "This is a rock.")
big_rock = Item("Big Rock", "This is a big rock.")
bread = Food("Bread", "This is a loaf of bread.", 100)
egg = Egg()
playerStartingItems = [rock1]
room['outside'].addItem(big_rock)
room['foyer'].addItem(bread)
room['treasure'].addItem(egg)


valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

player = Player(input("What is your name? "), room['outside'], playerStartingItems)

print(player.currentRoom)

while True:
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        elif cmds[0] == "i" or cmds[0] == "inventory":
            player.printInventory()
        elif cmds[0] == "status":
            player.printStatus()
        else:
            print("I did not understand that command.")
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "take" or cmds[0] == "get":
            itemToTake = player.currentRoom.findItemByName(" ".join(cmds[1:]))
            if itemToTake is not None:
                player.addItem(itemToTake)
                player.currentRoom.removeItem(itemToTake)
                print(f"You have picked up {itemToTake.name}")
            else:
                print("You do not see that item.")
        elif cmds[0] == "drop":
            player.dropItem(cmds[1:])
        elif cmds[0] == "eat":
            itemToEat = player.findItemByName(" ".join(cmds[1:]))
            if itemToEat is not None and hasattr(itemToEat, "eat") and itemToEat.eat() > 0:
                strengthGain = int(itemToEat.eat() / 10)
                player.strength += strengthGain
                player.removeItem(itemToEat)
                del itemToEat
                print(f"You have gained {strengthGain} strength!")
            else:
                print("You cannot eat that.")
        else:
            print("I did not understand that command.")
