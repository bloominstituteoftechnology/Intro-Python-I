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
playerOne = Player('Dray', room['outside'])

# Write a loop that:
#
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).
print()
# * Waits for user input and decides what to do.
#
# playerOne.moveTo('north')
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

arr = ['n', 'e', 's', 'w']
while True:
    print('\nIt is ' + playerOne.room.name + '.')
    print(playerOne.room.description)
    inp = input("\nChoose direction n/s/e/w  or enter q to quit: ").strip().lower()
    
    if (inp == 'q'):
        print('Goodbye!')
        break
    elif (inp in arr):
        if hasattr(playerOne.room, inp+'_to'):
            playerOne.room = getattr(playerOne.room, inp + '_to')
        else:
            print('This path is blocked. Choose another direction')
    else:
        print ("I did not recognize that command")

# *************
# hasattr(object, name)
# The arguments are an object and a string. 
# *************
# getattr(object, name[, default])
# Return the value of the named attribute of object. name must be a string. 

# For example, getattr(x, 'foobar') is equivalent to x.foobar. 
# If the named attribute does not exist, default is returned if provided, 
# otherwise AttributeError is raised.
# *************