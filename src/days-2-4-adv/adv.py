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
p1 = Player("Adventurer #1", room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
print('\nWelcome %s to the text adventure game!')
print('\nFollow prompts on screen.\n~Enter \'q\' to quit\n~Enter \'player\' for name and location')
while True:
    print('\n \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/')
    print('\nCurrent room: %s Description: %s' % (p1.location.name, p1.location.description))
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    inp = input('\nWhich direction (n/s/e/w): ')
    if inp == 'q':
        print('Quitting application...')
        break
    elif inp in ['n', 's', 'e', 'w']:
        if hasattr(p1.location, inp + '_to'):
            p1.location = getattr(pq.location, inp + '_to')
        else:
            print('\nThis move is not allowed')
    elif inp == 'player':
        print('\nName: %s Current Location: %s' % (p1.name, p1.location.name))
    else:
        print('\nInvalid entry, try again')
# If the user enters "q", quit the game.
