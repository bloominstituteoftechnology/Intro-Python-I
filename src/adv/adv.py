from room import Room
from playerInfo import player

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
new_player = Player('outside')

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
directions = {
    's':'s_to',
    'n':'n_to',
    'e': 'e_to',
    'w': 'w_to'
}

while True:
    print(new_player.pos['name'], ' is in ', new_player.pos['description'])
    move = input('Enter a direction or q to quit ')
    if move == 'q':
        break
    if move != 's' and move != 'n' and move != 'e' and move != 'w':
        print("{} is not a valid entry, please enter n, s, e, or w".format(move))
        continue
    if directions[move] in new_player.pos.keys():
        new_player.pos = rooms[new_player.pos[directions[move]]]
    else:
        print('Nothing to the {} of {}. Please enter a different direction or "q" to quit'.format(move, new_player.pos['name']))
