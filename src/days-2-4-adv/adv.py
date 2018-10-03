from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "silver"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "sword"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "gold"),
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
player = Player(room['outside'], 'rock')
player
# gold = Item('gold coins', '10')
# print(gold)
# room['outside'].add_item('pebble')
# room['outside'].view_items

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
    print(f'Hello, you are currently at {player.location}.')
    cmd = input("Heading Towards N, E, S or W ?-> ").lower().split()
    # if cmd == 'v':
    #     player.location.view_items
    # if cmd == 'i':
    #     player.view_items
    if cmd[0] == 'q':
        break
    elif cmd == "n":
        if hasattr( player.location , 'n_to' ):
            player.to(player.location.n_to)
        else:
            print('The movement is not allowed.')
    elif cmd == 's':
        if hasattr( player.location , 's_to' ):
            player.to(player.location.s_to)
        else:
            print('The movement is not allowed.')
    elif cmd == 'e':
        if hasattr( player.location , 'e_to' ):
            player.to(player.location.e_to)
        else:
            print('The movement is not allowed.')
    elif cmd == 'w':
        if hasattr( player.location , 'w_to' ):
            player.to(player.location.w_to)
        else:
            print('The movement is not allowed.')