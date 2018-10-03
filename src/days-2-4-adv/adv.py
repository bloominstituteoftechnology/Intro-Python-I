from room import Room
from player import Player
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

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

#
# Main
#

# p = Player(input("What is your name? "))

choice_dictionary = {"n": "North", "s": "South", "e": "East", "w": "West", "u": "Up", "d": "Down"}

# Make a new player object that is currently in the 'outside' room.

p = Player('Minnie', room["outside"])

# clearTerminal = os.system("clear")




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

def current(location):
    for key in room:
        if key == location:
            print("Current Location: " + room[key].name)
            print(room[key].description)


    
    

while True:
    currentLocation = p.location
    currentPlayer = p.name
    print(f"\n\n\n\n\nYou are currently in the great " + p.location.name)
    print("\n" + currentPlayer +"\n    Enter 'N' to go North \n    Enter 'Q' to Quit \n")
    cmd = input("-> ")
    if cmd == "q":
        os.system("clear")
        break
    elif cmd.upper() == 'N':
        if hasattr(p.location, 'n_to'):
            p.location = currentLocation.n_to
        else:
            os.system("clear")
            print(f"\n\n\nYou ran into a wall GAME OVER\n\n\n")
            break
            # print(f"\n You are currently in the grand " + p.location.name)
    # elif cmd == "n":
    #     print(f"You are currently " + currentLocation.name)
    #     currentLocation = currentLocation.n_to
    #     print(f"You are currently " + currentLocation.name)
    # elif cmd == "s"
    # elif cmd == "e"
    # elif cmd == "w"
    # elif cmd == "u"
    # elif cmd == "d"
    else:
        print("Movement Not Allowed")
    

