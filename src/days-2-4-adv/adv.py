from room import Room
from player import Player
import textwrap

wrapper = textwrap.TextWrapper(width=50)

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
p1 = Player("Adventurer #1", "outside")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    print('Current room: %s, Description: %s' % (p1.location, room[p1.location].description))
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    inp = input('\nWhich direction (n/s/e/w): ')
    if inp == 'q':
        break
    elif inp == 'n':
        p1.location = 'foyer'
    elif inp == 's':
        print('This move is not allowed')
    elif inp == 'e':
        print('This move is not allowed')
    elif inp == 'w':
        print('This move is not allowed')
# If the user enters "q", quit the game.
