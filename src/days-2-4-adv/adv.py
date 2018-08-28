from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("outside the cave entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("in the foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at the grand overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("in the narrow passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("inside the treasure chamber", """You've found the long-lost treasure
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

print('\nWelcome to TAG, the text adventure game!')
print('\nFollow the prompts on screen.\n~Enter \'Where am I?\' for your current location\n~Enter \'q\' to quit')
while True:
    print('\n ~ ~ ~')
    print('\nYou are currently %s'  % (player.room.name))
    print('\n... %s' % (player.room.description))

    inp = input('\nWhich direction do you want to go? (n/e/s/w): ')
    if inp == 'q':
        print('\nQuitting application...\n')
        break
    elif inp in ['n', 's', 'e', 'w']:
        if hasattr(player.room, inp + '_to'):
            player.room = getattr(player.room, inp + '_to')
        else:
            print('\nTHOUGH SHALL NOT PASS. TRY A DIFFERENT DIRECTION.')
    elif inp != ['n', 's', 'e', 'w']:
        print("\nINVALID INPUT, PLEASE ENTER \'n\', \'e\', \'s\' or \'w\'")
        