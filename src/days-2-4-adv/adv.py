from room import Room
from player import Player
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['rocks', 'gloves']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['hammer', 'flashlight']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['caribiner', 'rope', 'harness']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['mushies', 'tent', 'hashies', 'mollys']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['gold', 'silver', 'titanium']),
}


# Link rooms together
room['outside'].connectRooms(room['foyer'], 'n')
room['foyer'].connectRooms(room['overlook'], 'n')
room['foyer'].connectRooms(room['narrow'], 'e')
room['narrow'].connectRooms(room['treasure'], 'n')
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

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

def printRedMsg(msg):
    print(f"\x1b[1;31;40m {msg} \x1b[0m")


user_prompt_msg = '\x1b[1;32;40m' + "\n\n\nPlease enter a cardinal direction [n,s,e,w] or q to quit: " + '\x1b[0m'
exit_msg = "\nThank you for playing!"


while True:
    print("\n\n\nYou are currently in the {}".format(player.room.name))
    print("\n{}".format(player.room.description))
    print("\n\nThis room has the following items: ")
    player.room.displayItems()

    inp = input(user_prompt_msg)
    os.system('cls' if os.name == 'nt' else 'clear')

    number_of_args = len(inp.split(' '))
    print(f'Number of args is: {number_of_args}')

    if number_of_args == 1:

        if inp == "q":
            print(exit_msg)
            break

        elif inp == "n" or inp == "s" or inp == "e" or inp == "w":
            nextRoom = player.room.getRoomInDirection(inp)
            if nextRoom ==  None:
                printRedMsg("Sorry that direction does not exist.. please try again")
            else:
                player.set_room(nextRoom)

        else:
            printRedMsg("I didn't recognize that command, please enter, [take/drop] or [n,s,e,w]")

    elif number_of_args == 2:
        print('HOoray')

    else:
        printRedMsg('Too many input arguments!')

