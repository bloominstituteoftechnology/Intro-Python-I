from room import Room
from player import Player
import textwrap

# Declare all the rooms

# room dictionary creates reference from name of each room to an instance of a Room class object.
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
# give each room attributes for north, south, east, west to change current location from one room to another, according to the constraints of the map

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

while True:
    print(' ')
    print('Thy current location:', player.current_room.name)
    print(textwrap.wrap(player.current_room.description))
    move = input('Where will you move next?     ')
    print()
    try:
        move = move.lower()
    except AttributeError:
        print('Please enter a cardinal direction')
        continue
    if move in ['n', 'e', 's', 'w', 'q']:
        if move == 'n':
            try:
                player.current_room = player.current_room.n_to
            except AttributeError:
                print('You may not move in that direction. Try again')
                continue
        elif move == 'e':
            try:
                player.current_room = player.current_room.e_to
            except AttributeError:
                print('You may not move in that direction. Try again')
                continue
        elif move == 's':
            try:
                player.current_room = player.current_room.s_to
            except AttributeError:
                print('You may not move in that direction. Try again')
                continue
        elif move == 'w':
            try:
                player.current_room = player.current_room.w_to
            except AttributeError:
                print('You may not move in that direction. Try again')
                continue
        elif move == 'q':
            break
    else:
        print('Please enter a cardinal direction or "q" to quit')

    # print(f"You're currently in the {player.current_room.name}")
    # print(player.current_room.description)
    # user_input = input("\nCommand> ").strip().lower().split()

    # if len(user_input) > 2 or len(user_input) < 1:


    # getDir = input('Enter your next move: ')
    # print(getDir)
    # player_1.move(getDir)
    # print("title: {} room: {} ".format(player_1.title, player_1.current_room)))

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
