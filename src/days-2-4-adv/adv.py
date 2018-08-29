from room import Room
from player import Player
import os

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
jedi = Player(room['outside'])

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

while True:
    incorrect_dir_msg = '\x1b[1;37;41m' + "Sorry that direction does not exist.. please try again" + '\x1b[0m'
    user_prompt_msg = '\x1b[6;30;42m' + "\n\n\nPlease enter a cardinal direction (n,s,e,w) or q to quit: " + '\x1b[0m'
    exit_msg = "\nThank you for playing!"
    bad_command_msg = '\x1b[1;37;41m' + "\nI didn't recognize that command, please enter, n,s,e,w" + '\x1b[0m'

    print("\n\n\nYou are currently in the {}".format(jedi.room.name))
    print("\n{}".format(jedi.room.description))
    
    inp = input(user_prompt_msg)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if inp == "q":
        print(exit_msg)
        break

    elif inp == "n":
        if not hasattr(jedi.room.n_to, 'name'):
            print(incorrect_dir_msg)
        else:
            jedi.room = jedi.room.n_to

    elif inp == "s":
        if not hasattr(jedi.room.s_to, 'name'):
            print(incorrect_dir_msg)
        else:
            jedi.room = jedi.room.s_to

    elif inp == "w":
        if not hasattr(jedi.room.w_to, 'name'):
            print(incorrect_dir_msg)
        else:
            jedi.room = jedi.room.w_to

    elif inp == "e":
        if not hasattr(jedi.room.e_to, 'name'):
            print(incorrect_dir_msg)
        else:
            jedi.room = jedi.room.e_to

    else:
        print(bad_command_msg)
