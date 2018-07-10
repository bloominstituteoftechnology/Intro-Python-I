# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
        "w_to": "shed",
    },

    "shed": {
        "name": "Shed",
        "description": """The shed is completely empty, besides some cobwebs in the corner 
and a rope ladder on the floor.""",
        "e_to": "outside",
        "contents": ["ladder"],
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. A light flickers in
the distance, but there is no way across the chasm. The only way is down...""",
        "s_to": "foyer",
        "d_to": "",
    },

    "chasmFloor": {
        "name": "Chasm Floor",
        "description": """It's much too dark to see anything down here. 
All you can see is a faint light coming from up above.""",
        "u_to": "overlook",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w_to": "foyer",
        "n_to": "treasure",
        "contents": ["sparrow"],
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
    },

}

""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
    },
"""

# Write a class to hold player information, e.g. what room they are in currently
class Player:
    def __init__(self, inRoom, inventory):
        self.inRoom = inRoom
        self.inventory = inventory

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(rooms["outside"], [])

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
import textwrap

def listInventory(array):
    print("You have ", end='')
    if len(array) == 0:
            print('nothing.')
    for item in array:
        if len(array) == 1:
            print(f'a {item}.')
        elif item == array[len(array)-1]:
            print(f'and a {item}.')
        else:
            print(f'a {item}, ', end='')

print("\n\n")
print(f'{player1.inRoom["name"]}: \n{player1.inRoom["description"]}')

quit = False
while quit == False:
    command = input("\n>")
    #quit
    if command == 'q':
        print("Farewell adventurer.")
        quit = True
    
    #travel
    elif command == 'n' or command == 's' or command == 'e' or command == 'w' or command == 'd' or command == 'u':
        if command + "_to" in player1.inRoom:
            if player1.inRoom[command + "_to"]:
                nextRoom = player1.inRoom[command + "_to"]
                player1.inRoom = rooms[nextRoom]
                print(f'{player1.inRoom["name"]}: \n{player1.inRoom["description"]}')
            else:
                print("You can not go that way right now.")
        else:
            print("You can not go that way.")

    #take items
    elif command == 'take ladder':
        if "ladder" in player1.inRoom.contents:
            player1.inventory.append("ladder")
            player1.inRoom.contents.remove("ladder")
        else:
            print('There is no ladder in this room')

    #use items
    elif command == 'use ladder':
        if 'ladder' in player1.inventory:
            if player1.inRoom == "overlook":
                


    #inventory
    elif command == 'i' or command == 'inventory':
        listInventory(player1.inventory)
    
    #look
    elif command == 'look' or command == 'l':
        print(f'{player1.inRoom["name"]}: \n{player1.inRoom["description"]}')
    
    #unsupported
    else:
        print("That's not a verb I recognise.")
