import os
import textwrap
from time import sleep
from room import Room
from player import Player
from item import Item 
# Declare all the rooms
# Need to extend room array with item array
# array.extend()

room = {
    # outside: {name: "Outside cave entrance", description: "North of you, the cave mouth beckons", n_to: {POINTS TO FOYER}}
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons"),
    'foyer':    Room("Foyer","Dim light filters in from the south. Dusty passages run north and east."),
    'overlook': Room("Grand Overlook","A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),
    'narrow':   Room("Narrow Passage","The narrow passage bends here from west to north. The smell of gold permeates the air."),
    'bathroom': Room("Pit stop", "Remember to wash your hands!", "You may continue from west to north"),
    'treasure': Room("Treasure Chamber","You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
    # Add my own room
    
}



# item = {
#     1: Item("Sword").extend(room),
#     print(item[])
#     # 2: 
#     # 3: 
# }
#debugging

# trying to come up with the wording to implement the printing of the item here:
# if "item" in Room['']:
#     print("You see a/an ") + Room[]["item"])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['narrow'].e_to = room['bathroom']
room['bathroom'].w_to = room['treasure']
room['bathroom'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
room['foyer'].contents.append(Item("lamp", "Lamp"))
room['foyer'].contents.append(Item("sword", "A Sword with emeralds in the handle"))
# Main
# DEBUGGING
# print(room['outside'].s_to)
# Make a new player object that is currently in the 'outside' room.
player = Player('Jackee', room['outside'])
direction = None
# Write a loop that:
# while(True):
#     #print current room name
#     #debug 
    
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(
#         '\n You are currently here:','\n'.join(wrap(player.location.name, width=10)),
#         '\n Description:', '\n'.join(wrap(player.location.description, width=50))) 
#     direction = input('\nWhich way would you like to go?\n(N, E, S, W) or (Q to quit) pick one:').lower()
#     player.move_to(direction)
# curRoom = player.room

    # Print out room description
done = False

while not done:
    curRoom = player.room

    # Print out room description

    # prettyDesc = textwrap.fill(curRoom.description)

    # print('\n{curRoom.name}\n\n{prettyDesc}')

    # Print room contents

    if len(curRoom.contents) > 0:
        print("\nYou also see:")
        for i in curRoom.contents:
            print("   " + i.description)

    # Prompt

    command = input("\nCommand> ").strip().lower()

    command = command.split(' ')

    # Single word commands

    if len(command) == 1:

        if command[0] == 'q' or command[0] == 'quit' or command[0] == 'exit':
            done = True

        elif command[0] in ["s", "n", "e", "w"]:
            dirAttr = command[0] + "_to"

            if hasattr(curRoom, dirAttr):
                player.room = getattr(curRoom, dirAttr)

            else:
                print("You can't go that way.")

        elif command[0] in ["i", "inventory"]:
            if len(player.contents) > 0:
                print("\nYou're currently carrying:")
                for i in player.contents:
                    print("   " + i.description)
            else:
                print("\nYou're not carrying anything.")

        else:
            print("I don't understand that!")

    elif len(command) == 2:

        verb, obj = command

        if verb in ['get', 'take']:
            candidates = [item for item in curRoom.contents if item.name == obj]
 
            if len(candidates) == 0:
                print("You don't see that here.")

            else:
                player.contents.append(candidates[0])
                curRoom.contents.remove(candidates[0])
                if candidates not in player.contentsHistory:
                    print("Grats on points, Bro!")
                    player.score += 1
           

        elif verb == 'drop':
            candidates = [item for item in player.contents if item.name == obj]

            if len(candidates) == 0:
                print("You're not carrying that.")

            else:
                player.contents.remove(candidates[0])
                curRoom.contents.append(candidates[0])

        else:
            print("I don't understand that!")

    else:
        print("I don't understand that!")

# * A *.pyc file is created for imported modules, and they are placed in the same directory containing the .py file. 
# However... no .pyc file is created for the main script for your program. In other words... 
# if you call "python myscript.py" on the command line, there will be no .pyc file for myscript.py.
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
