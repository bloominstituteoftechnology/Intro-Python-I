from room import Room
from player import Player
import textwrap
import sys
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
player = Player("Justin", room['outside'])
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

move_inputs = ["n", "e", "s", "w"] # valid inputs to advance game

quit = False # describes overall game state

while not quit:
	current = player.room
	description = textwrap.fill(current.description)
	# show player the room they are in
	print("{0}\n{1}".format(current.name, description))
	# take player commands and remove formatting
	player_input = input("Command: ").strip().lower()
	# player quits/exits game
	if (player_input == "q") or (player_input == "quit"):
		quit = True
	# player moves in a new direction
	elif player_input in move_inputs:
		dirAttr = player_input + "_to"
		# check if move input is valid
		if hasattr(current, dirAttr):
			player.room = getattr(current, dirAttr) # update player's location
		else:
			print("You can't go that way!")
	# player inputs an unknown command
	else:
		print("That doesn't mean anything!")















