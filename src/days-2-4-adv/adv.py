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

while True:
    invalid_move = '\nYou shall not pass!'

    print(f'\nLocation: {player.location.name}')
    print(f'{player.location.description}')

    answer = input("\nWhich way will you go? n, s, e, w. \nIt's not to late to turn back. Press q to quit\n")

    if answer == "q":
        print("Perhaps it is for the best.")
        break

    if answer == "n":
        if not hasattr(player.location.n_to, 'name'):
            print(invalid_move)
        else:
            player.location = player.location.n_to

    if answer == "s":
        if not hasattr(player.location.s_to, 'name'):
            print(invalid_move)
        else:
            player.location = player.location.s_to

    if answer == "e":
        if not hasattr(player.location.e_to, 'name'):
            print(invalid_move)
        else:
            player.location = player.location.e_to
    if answer == "w":
        if not hasattr(player.location.w_to, 'name'):
            print(invalid_move)
        else:
            player.location = player.location.w_to
