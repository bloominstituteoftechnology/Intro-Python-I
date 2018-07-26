from os import system
from room import Room
from player import Player
from item import Item
import textwrap
from textwrap import fill

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['sword']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['shield']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['coin']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['note'])
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

player = Player(input("Enter your name: "), room['outside'], [])

system("clear")

play = input("Hello, " + str(player.name) + "! I hope you're ready to go look for some treaure!\n\nHere's how you play:\n\nIf you want to move just type 'n' to go north, 's' for south, 'e' for east, and 'w' for west.\nTo pick up an item, type 'take (item name)'.\nTo drop an item, type 'drop (item name)'.\nTo check your inventory, type 'i'.\nIf you want to quit, type 'q'.\nAre you ready to play? (Yes/No)\n>>> ")

notPlaying = False
if play == 'No' or play == 'no' or play == 'n' or play == 'N' or play == 'NO':
    
    notPlaying = True
    print("\nOk, see you later!\n")
    system("clear")

elif play == 'Yes' or play == 'yes' or play == 'y' or play == 'Y':

    system("clear")
    print("Awesome, let's find that treasure!...\n")
    

    done = False
    while not done:

        curRoom = player.room
        roomDesc = textwrap.fill(curRoom.description)
        foundItem = curRoom.item

        print("{}\n{}\n\n{}\n".format(curRoom.name, roomDesc, foundItem))

        command = input("What do you want to do?\n>>> ").strip().lower().split()
        system("clear")

        if len(command) == 1:

            if command[0] == 'q' or command[0] == 'quit' or command[0] == 'exit':
                
                done = True
                print("\nQuitter!\n")

            elif command[0] == 'i':

                if len(player.inventory) == 0:
                   
                    print("You're inventory is empty.")

                else:
                   
                    print("This is what is in your inventory:\n" + player.inventory)
            
            elif command[0] in ["s", "n", "e", "w"]:

                dirAttr = command[0] + "_to"

                if hasattr(curRoom, dirAttr):

                    player.room = getattr(curRoom, dirAttr)

                else:

                    print("That way is blocked")
            
            else:

                print("Why don't you try that again...")

        elif len(command) == 2:

            if command[0] == 'take':

                curRoom.item.remove(command[1])
                player.inventory.append(command[1])

                print("Congrats, you picked up the item! Check your inventory to see your items.")
            
            elif command[0] == 'drop':

                player.inventory.remove(command[1])
                curRoom.item.append(command[1])

                print("You dropped an item.")

            else:
                
                print("There are no items to do this...keep moving.")
            
