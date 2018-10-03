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

playername = input("Enter Your Name: ")


p = Player(playername, room["outside"])

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
    CRED = '\033[91m'
    CBLACK = '\033[0;30m'
    CGREEN = '\033[0;32m'
    CBLUE = '\033[0;34m'
    currentPlayer = p.name
    currentLocation = p.location
    print(f"\nYou are currently in the great " + p.location.name + "\n\n" + p.location.description)
    

    if hasattr(p.location, "S_to"):
        print("\n\n    'S' to" + str(p.location.s_to))
        if hasattr(p.location, "e_to"):
            print("    'E' to" + str(p.location.e_to))
            if hasattr(p.location, "n_to"):
                print("    'N' to" + str(p.location.n_to))
                if hasattr(p.location, "w_to"):
                    print("    'W' to" + str(p.location.w_to))
    elif hasattr(p.location, "w_to"):
        print("\n\n    'W' to" + str(p.location.w_to))
        if hasattr(p.location, "n_to"):
            print("    'N' to" + str(p.location.n_to))
            if hasattr(p.location, "e_to"):
                print("    'E' to" + str(p.location.e_to))
                if hasattr(p.location, "s_to"):
                    print("    'S' to" + str(p.location.s_to))
    elif hasattr(p.location, "e_to"):
        print("\n\n    'E' to" + str(p.location.e_to))
        if hasattr(p.location, "s_to"):
            print("    'S' to" + str(p.location.s_to))
            if hasattr(p.location, "w_to"):
                print("    'W' to" + str(p.location.w_to))
                if hasattr(p.location, "n_to"):
                    print("    'N' to" + str(p.location.n_to))
    elif hasattr(p.location, "n_to"):
        print("\n\n    'N' to" + str(p.location.n_to))
        if hasattr(p.location, "e_to"):
            print("    'E' to" + str(p.location.e_to))
            if hasattr(p.location, "s_to"):
                print("    'S' to" + str(p.location.s_to))
                if hasattr(p.location, "w_to"):
                    print("    'W' to" + str(p.location.w_to))
    else:

        if hasattr(p.location, "S_to"):
            print("\n\n    'S' to" + str(p.location.s_to))
            if hasattr(p.location, "e_to"):
                print("    'E' to" + str(p.location.e_to))
                if hasattr(p.location, "n_to"):
                    print("    'N' to" + str(p.location.n_to))
                    if hasattr(p.location, "w_to"):
                        print("    'W' to" + str(p.location.w_to))
        elif hasattr(p.location, "w_to"):
            print("\n\n    'W' to" + str(p.location.w_to))
            if hasattr(p.location, "n_to"):
                print("    'N' to" + str(p.location.n_to))
                if hasattr(p.location, "e_to"):
                    print("    'E' to" + str(p.location.e_to))
                    if hasattr(p.location, "s_to"):
                        print("    'S' to" + str(p.location.s_to))
        elif hasattr(p.location, "e_to"):
            print("\n\n    'E' to" + str(p.location.e_to))
            if hasattr(p.location, "s_to"):
                print("    'S' to" + str(p.location.s_to))
                if hasattr(p.location, "w_to"):
                    print("    'W' to" + str(p.location.w_to))
                    if hasattr(p.location, "n_to"):
                        print("    'N' to" + str(p.location.n_to))
        elif hasattr(p.location, "n_to"):
            print("\n\n    'N' to" + str(p.location.n_to))
            if hasattr(p.location, "e_to"):
                print("    'E' to" + str(p.location.e_to))
                if hasattr(p.location, "s_to"):
                    print("    'S' to" + str(p.location.s_to))
                    if hasattr(p.location, "w_to"):
                        print("    'W' to" + str(p.location.w_to)) 

    print("\n\n")
    cmd = input("-> ")
    if cmd == "q":
        os.system("clear")
        break
    elif cmd.upper() == 'N':
        os.system("clear")
        print(currentPlayer + ",")

        # if p.location == room['treasure']:
        #     break

        if hasattr(p.location, 'n_to'):
            p.location = currentLocation.n_to
            # if hasattr(p.location, 's_to'):
            #     print("\n     Enter "S" to go Souther")
            # else:
            #     return
        else:
            os.system("clear")
            print("\n    You Can't Go Any Farther North, Go Another Direction \n\n")
            if hasattr(p.location, "S_to"):
                print("\n\n    'S' to" + str(p.location.s_to))
                if hasattr(p.location, "e_to"):
                    print("    'E' to" + str(p.location.e_to))
                    if hasattr(p.location, "n_to"):
                        print("    'N' to" + str(p.location.n_to))
                        if hasattr(p.location, "w_to"):
                            print("    'W' to" + str(p.location.w_to))
            elif hasattr(p.location, "w_to"):
                print("\n\n    'W' to" + str(p.location.w_to))
                if hasattr(p.location, "n_to"):
                    print("    'N' to" + str(p.location.n_to))
                    if hasattr(p.location, "e_to"):
                        print("    'E' to" + str(p.location.e_to))
                        if hasattr(p.location, "s_to"):
                            print("    'S' to" + str(p.location.s_to))
            elif hasattr(p.location, "e_to"):
                print("\n\n    'E' to" + str(p.location.e_to))
                if hasattr(p.location, "s_to"):
                    print("    'S' to" + str(p.location.s_to))
                    if hasattr(p.location, "w_to"):
                        print("    'W' to" + str(p.location.w_to))
                        if hasattr(p.location, "n_to"):
                            print("    'N' to" + str(p.location.n_to))
            else:
                print("\n\n    'N' to" + str(p.location.n_to))
                if hasattr(p.location, "e_to"):
                    print("    'E' to" + str(p.location.e_to))
                    if hasattr(p.location, "s_to"):
                        print("    'S' to" + str(p.location.s_to))
                        if hasattr(p.location, "w_to"):
                            print("    'W' to" + str(p.location.w_to)) 
    elif cmd.upper() == 'E':
        print(currentPlayer + ",")
        if hasattr(p.location, 'e_to'):
            p.location = currentLocation.e_to
        else:
            os.system("clear")
            print("\n    You Can't Go Any Farther East, Go Another Direction \n\n")
    elif cmd.upper() == 'S':
        print(currentPlayer + ",")
        if hasattr(p.location, 's_to'):
            p.location = currentLocation.s_to
        else:
            os.system("clear")
            print("\n    You Can't Go Any Farther Sorth, Go Another Direction \n\n")
    elif cmd.upper() == 'W':
        print(currentPlayer + ",")
        if hasattr(p.location, 'w_to'):
            p.location = currentLocation.w_to
        else:
            os.system("clear")
            print("\n    You Can't Go Any Farther West, Go Another Direction \n\n")
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
    # elif p.location == room['treasure']:
    #     pass
    else:
        print("Key Not Allowed")

    
    

