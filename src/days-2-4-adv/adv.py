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

suppressRoomPrint = True

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print('\n ==========================-----------------------==========================\n')
        print(f"{player.room.name}\n{player.room.description}\nItems: {player.room.items}")

    inp = input('\nWhere would you like to move? (n/e/s/w) enter \'q\' to quit: ').split(' ')

    if(inp[0] == 'q'):
        print('\nThanks for playing, exiting now!')
        break
    elif(inp[0] in ['n', 'e', 's', 'w']):
        if hasattr(player.room, inp[0] + '_to'):
            player.room = getattr(player.room, inp[0] + '_to')
        else:
            print('\nCannot go that way!')
            suppressRoomPrint = True
    elif(inp[0] == 'get' or inp[0] == 'take'):
        print('hi')
    else:
        print('\nInvalid input, please try again.')
        suppressRoomPrint = True

                     
