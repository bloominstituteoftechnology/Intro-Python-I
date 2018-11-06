from room import Room
from player import Player

import textwrap

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

player = Player("Nicocchi", room['outside'])
print(f'{player.room.name}')
desc = textwrap.wrap(player.room.description, width=100)
for element in desc:
    print(element)

user = input("[n] North   [s] South   [e] East   [w] West   [q] Quit\n").lower()

while not user == 'q':
    # if player chooses North
    if user == 'n':
        # player.direction = 'north'
        player.move_north()

        # if player.room.n_to:
        #     player = Player("Nicocchi", player.room.n_to)
    elif user == 's':
        player.move_south()
        # player.direction = 'south'
        #
        # if player.room.s_to:
        #     player = Player("Nicocchi", player.room.s_to)
    elif user == 'e':
        player.direction = 'east'

        if player.room.e_to:
            player = Player("Nicocchi", player.room.e_to)
    elif user == 'w':
        player.direction = 'west'

        if player.room.w_to:
            player = Player("Nicocchi", player.room.w_to)
    else:
        print("Invalid selection. Please try again.")

    if player.room:
        print(f'{player.room.name}')
        desc = textwrap.wrap(player.room.description, width=100)
        for element in desc:
            print(element)
    else:
        print(f'{player.name} tried to move to {player.direction} but was blocked. Try another direction.')

    print(f'{player.name} pick a direction...')
    user = input("[n] North   [s] South   [e] East   [w] West   [q] Quit\n").lower()
