from room import Room
from player import Player
from item import Item
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


items = {
    'Small Knife': Item('Small Knife', True),
    'Torch': Item('Torch', True),
    'Matches': Item('Matches'),
    'Rations': Item('Rations'),
    'Cigarettes': Item('Cigarettes'),
    '9mm Pistol': Item('9mm Pistol', True),
    '9mm Ammunition': Item('9mm Ammunition', True)
}

# initialize the player to be outside
player = Player(room['outside'])

while True:
    # print the current room
    print("\n CURRENT ROOM:\n" + "  " + player.room.name + "\n" + "    " + player.room.description + "\n")

    command = input("Please enter a direction to move: [NORTH] [SOUTH] [EAST] [WEST]. \n Input [QUIT] to leave the game. \n\n Command: ")

    if command.upper() == 'QUIT':
        break

    elif command.upper() == 'NORTH':
        if player.room.n_to:
            player.room = player.room.n_to
            print(f"\n You move north into the {player.room.name}. {player.room.description}")
        else:
            print("\n There is nowhere to move north.")
            continue

    elif command.upper() == 'SOUTH':
        if player.room.s_to:
            player.room = player.room.s_to
            print(f"\n You move south into the {player.room.name}. {player.room.description}")
        else:
            print('\n There is nowhere to move south.')
            continue

    elif command.upper() == 'EAST':
        if player.room.e_to:
            player.room = player.room.e_to
            print(f"\n You move ease into the {player.room.name}. {player.room.description}")
        else:
            print("\n There is nowhere to move east.")
            continue

    elif command.upper() == 'WEST':
        if player.room.w_to:
            player.room = player.room.w_to
            print(f"\n You move west into the {player.room.name}. {player.room.description}")
        else:
            print("\n There is nowhere to move west.")
            continue

    else:
        print("\n Unknown command, please try again.")
