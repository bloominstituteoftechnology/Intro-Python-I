from room import Room
from player import Player
from item import Item
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

#print(room['outside'].name)

# Make a new player object that is currently in the 'outside' room.

player1 = Player(room['outside'], [Item('Pen', 'A mighty instrument to influence minds'), Item('Sword', 'Not as mighty...')])

while(True):
    inp = input('Which direction will you move?')
    if inp == 'q':
        break;
    elif inp == 'n':
        if hasattr(player1.location, 'n_to'):
            player1.location = player1.location.n_to
            print('\n [{}]...\n'.format(player1.location.name))
            print('...{}\n'.format(player1.location.description))
        else:
            print('\nNone has traveled catacorner to the three dimensions...invalid input try again...')

    elif inp == 'w':
        if hasattr(player1.location, 'w_to'):
            player1.location = player1.location.w_to
            print('\n [{}]...\n'.format(player1.location.name))
            print('...{}\n'.format(player1.location.description))
        else:
            print('\nNone has traveled catacorner to the three dimensions...invalid input try again...')
    elif inp == 'e':
        if hasattr(player1.location, 'e_to'):
            player1.location = player1.location.e_to
            print('\n [{}]...\n'.format(player1.location.name))
            print('...{}\n'.format(player1.location.description))
        else:
            print('\nNone has traveled catacorner to the three dimensions...invalid input try again...')
    elif inp == 's':
        if hasattr(player1.location, 's_to'):
            player1.location = player1.location.s_to
            print('\n [{}]...\n'.format(player1.location.name))
            print('...{}\n'.format(player1.location.description))
        else:
            print('\nNone has traveled catacorner to the three dimensions...invalid input try again...')
    elif inp == 'i':
        for item in player1.inventory:
            print('{} {}'.format(item.name, item.description))
    else:
        print('None has traveled catacorner to the three dimensions...invalid input try again...')

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
