from os import system

from room import Room
from player import Player
from item import Item, Treasure

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

# Create Items Dictionary

Items = {
    "Sword" : Item('Sword', 'Shiny'),
    "Bronze Coin" : Treasure('Bronze Coin', 'Bronze', '5'),
    "Silver Coin" : Treasure('Silve Coin', 'Silver', '10'),
    "Gold Coin" : Treasure('Gold Coin', 'Gold', '20')
}

# Adding Items to a Room

room['outside'].addItem(Items['Sword'])
room['foyer'].addItem(Items['Bronze Coin'])
room['narrow'].addItem(Items['Silver Coin'])
room['overlook'].addItem(Items['Gold Coin'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

system("clear")
name = input("Enter your name:\n")
player = Player(name, room['outside'])

# Game Features:
    # 1. Display current room, room description, room items

    # 2. Takes an input as an instruction

    # 3. Travels through rooms using cardinal directions (North, East, South, West)

    # 4. Quits the game (Quit)

    # 5. Take items from the room or drop items from the inventory (Take Item(Name) | Drop Item(Name))

    # 6. Checks the inventory (Inventory)

    # 7. Display end game message

    # 8. Checks the score (Score)

system("clear")
while (player.room != 'exit'):

    # - Display current room, room description, room items

    print(player.name + " is at the\n" + player.room.name + ": " + player.room.description + "\n")
    print("The item(s) in the " + player.room.name + ": " + str(player.room.items) + "\n")

    # - Takes an input as an instruction

    instruction = input("Enter: North | East | South | West | Take Item(Name) | Drop Item(Name) | Inventory | Score | Quit:\n")

    # - Travels through rooms using cardinal directions (North, East, South, West)

    direction = {
        "North": player.room.n_to,
        "East": player.room.e_to,
        "South": player.room.s_to,
        "West": player.room.w_to
    }

    # Single Word Commands

    system("clear")
    if (len(instruction.split()) == 1):
        new_room = direction.get(instruction, None)

    # - Quits the game (Quit)

        if (instruction == "Quit"):
            break
        elif (new_room):
            if (player.room.name == "Treasure Chamber"):
                break
            player.room = new_room

    # - Checks the inventory (Inventory)

        elif (instruction == "Inventory"):
            print("In your inventory:", player.inventory)
            print("")
    
    # - Checks the score (Score)

        elif (instruction == "Score"):
            print(player.name + "'s Current Score: " + str(player.score) + "\n")
        elif (instruction in ["North", "East", "South", "West"]):
            print("Nowhere to go\n")
        else:
            print("Invalid Command. Enter: North | East | South | West | Take Item(Name) | Drop Item(Name) | Inventory | Score | Quit:\n")

    # Two Word Commands
    
    # - Take items from the room or drop items from the inventory (Take Item(Name) | Drop Item(Name))

    else:
        verb, target = [x for x in instruction.split()]
        if (verb == "Take"):
            if (player.room.searchItems(target)):
                player.toInventory(Items[target])
                player.room.removeItem(target)
                print(player.name + " takes the " + target + "\n")
            else: 
                print(target + " is not available\n")
        if (verb == "Drop"):
            if (player.searchInventory(target)):
                player.room.addItem(Items[target])
                player.removeItem(target)
                print(player.name + " drops the " + target + "\n")
            else:
                print(target + " is not in your inventory\n")

# - Display end game message

system("clear")
if (len(player.inventory) == 0):
    print("You left the cave empty handed!\n")
else:
    print("Congratulations, you managed to leave the cave with:", player.inventory)
    print("")