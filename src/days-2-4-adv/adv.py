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
player_inp = ''


# Gets the player's input and sets it in the global var user
def player_input():
    global player_inp
    player_inp = input("\n[n] North   [s] South   [e] East   [w] West   [q] Quit\n").lower()


# Display the screen message
def screen_message():
    print(f'\n{player.room.name}')
    desc = textwrap.wrap(player.room.description, width=70)
    for element in desc:
        print(element)


screen_message()
player_input()

# While the input is not q, keep get game going
while not player_inp == 'q':
    # if player chooses North
    if player_inp == 'n':
        player.move_north()
    elif player_inp == 's':
        player.move_south()
    elif player_inp == 'e':
        player.move_east()
    elif player_inp == 'w':
        player.move_west()
    else:
        print("Invalid selection. Please try again.\n")

    # if the player has a room, continue to display the
    # room message, else, display input message to avoid infinite loop of same room
    if player.room and player.previous_room is not player.room:
        screen_message()
    else:
        print(f'\n{player.name} tried to move to {player.direction} but was blocked. Try another direction.\n')

    player_input()
