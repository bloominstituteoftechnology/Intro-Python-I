from room import Room
from player import Player

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
p = Player(room['outside'])

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
playing = True
show_description = True
while playing:
    if show_description:
        print(p.c_room.location)
        print(p.c_room.description)
    show_description = True
    direction = input('Choose a direction to continue (N, E, S, W): ')
    if str(direction).upper() == 'N' and hasattr(p.c_room, 'n_to'):
        p.__update_room__(p.c_room.n_to)
    elif str(direction).upper() == 'E' and hasattr(p.c_room, 'e_to'):
        p.__update_room__(p.c_room.e_to)
    elif str(direction).upper() == 'S' and hasattr(p.c_room, 's_to'):
        p.__update_room__(p.c_room.s_to)
    elif str(direction).upper() == 'W' and hasattr(p.c_room, 'w_to'):
        p.__update_room__(p.c_room.w_to)
    elif str(direction).upper() == 'Q':
        print("Better luck next time!")
        playing = False
    else:
        print("I'm sorry, that command is invalid, please input another")
        show_description = False
