from os import system # for system clear on game play
from room import Room
from player import Player
from item import Item
import textwrap # or from textwrap import fill

# Declare all the rooms

room = {
    'outside':  Room("OUTSIDE CAVE ENTRANCE",
                     "North of you, the cave mount beckons", [Item("Lantern", "A Lantern to light your way")] + [Item("Coin", "An old ancient coin")]),

    'foyer':    Room("FOYER", """Dim light filters in from the south. Dusty passages run north and east.""", [Item("Rope", "A bit of old used rope")]),

    'overlook': Room("GRAND OVERLOOK", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [Item("Skull", "A skull from someone scared to death of that steep drop!")]),

    'narrow':   Room("NARROW PASSAGE", """The narrow passage bends here from west to north and south. The smell of gold permeates the air.""", [Item("Cloak", "A tattered, well worn cloak")]),

    'treasure': Room("TREASURE CHAMBER", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south, but you smell something from the North.""", [Item("Shield", "A shield made of sturdy steel")] + [Item("Chest", "An empty chest")]),
    # Rm I added on for fun
    'dungeon': Room("THE DUNGEON", """You've entered the dark, smelly dungeon of doom! Now you are cursed for 10 million years and forever the
caregiver for these smelly pugs. Exit to the east.""", [Item("Satchel", "A satchel made of pig skin to carry your loot")]),
    # Rm I added on for fun
    'pugcave': Room("PUGS CAVE", """Oh No!!! You've awoken the pug beasts... RUN for your lives to the only exit north!""", [Item("Fang", "A smelly pug fang for goodluck")]),
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
room['dungeon'].e_to = room['narrow']
room['narrow'].s_to = room['dungeon']
room['pugcave'].n_to = room['treasure']
room['treasure'].n_to = room['pugcave']

# Add Items (has to wired correctly on room.py as well)
# room['overlook'].contains.append(Item("coins", "Gold coins"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
system("clear") # clears console before you start your game (be sure to add os import system)

player_name = input("Enter a player name: ") # Welcomes player by asking them for their name

player = Player(player_name, room['outside'])

print("\nWelcome, %s!" % (player.playerName)) # Welcomes player by name they entered above

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def dircheck(attr):
    if hasattr(player.room, attr):
        player.room = getattr(player.room, attr)
    else:
        print("\nYou Shall Not Pass\n")

while True:
    print("\n~*~ " + player.room.name + " ~*~")
    print(textwrap.fill(player.room.description, 50))
    print("Items for the taking: " + (",".join([item.name for item in player.room.items]) or "None") + "\n")
    print("To take an item, type 'take [item]'")
    print("To drop an item, type 'drop [item]'")
    print("To check your inventory, type 'i' or 'inventory'" "\n")
    
    cmd = input("\nWhich Direction Would You Like To Go? \n(n, s, e, w or q to quit): ").strip().lower()
    cmds = cmd.split(" ")
    if len(cmds) == 1:
        if cmd == "q" or cmd == "quit":
            break
        elif cmd in ["n", "e", "s", "w"]:
            dircheck(cmd + "_to")
        elif cmd == "i" or cmd == "inventory":
            print("\nInventory:\n" + "\n".join([item.name + " - " + item.description for item in player.inventory]))
        else:
            print("\nSorry, Wrong Command - Try Again") 
    elif len(cmds) == 2:
        verb = cmds[0]
        obj = cmds[1]
        if verb == "get" or verb == "take":
            if obj in [item.name.lower() for item in player.room.items]:
                for i, o in enumerate(player.room.items):
                    if o.name.lower() == obj:
                        player.inventory.append(o)
                        del player.room.items[i]
                        break
            else: 
                print("\nSorry - Item Not Found In This Room")
        elif verb == "drop":
            if obj in [item.name.lower() for item in player.inventory]:
                for i, o in enumerate(player.inventory):
                    if o.name.lower() == obj:
                        player.room.items.append(o)
                        del player.inventory[i]
                        break
            else:
                print("\nSorry - Item Not Found In Your Inventory")
    else:
        print("\nSorry, Wrong Command - Try Again")


# Instructor Solve------------------------------------
# done = False

# while not done:
#     curRoom = player.room

#     prettyDesc = textwrap.fill(curRoom.description)

#     print(f'\n{curRoom.name}\n\n{prettyDesc}')

    # Print room contents
    # if len(curRoom.contents) > 0:
        # print("You also see:")
        # for i in CurRoom.contents:
            #print("  " + i.description)
        # print()

#     command = input("\nCommand> ").strip().lower()

#     command = command.split('  ')

#     if len(command) == 1:

#       if command[0] == 'q' or command[0] == 'quit' or command[0] == 'exit':
#         done = True

#     elif command[0] in ["s", "n", "e", "w"]:
#         dirAttr = command[0] + "_to"

#         if hasattr(curRoom, dirAttr):
#             player.room = getattr(curRoom, dirAttr)

#         else:
#             print("You can't go that way.")

#     elif command[0] in ["i", "inventory"]:
#       print("You're currently carrying:")
#     else:
#         print("I don't understand that!")

#   elif len(command) == 2:

#       verb, obj = command
       
#       if verb in ['get', 'take']:
#           candidates = [item for item in CurRoom.contents if item.name == obj]

#       if len(candidates) == 0:
#           print("You don't see that here.")

#       else:
#           player.contents.append(candidates[0])
#           curRoom.contents.remove(candidates[0])