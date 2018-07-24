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
player1 = Player(room['outside'])
GamePlaying = True

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while GamePlaying == True:
	# print("\n%s\n\n%s" % (player1.location.name, player1.location.desc))
	desc = textwrap.wrap(player1.location.desc)

	print("\n****************************************")
	print("\n%s\n" % player1.location.name)
	for line in desc:
		print(line)
	print("\n****************************************")

	direction = input("\nEnter direction: ").lower()

	# If the user enters a cardinal direction, attempt to move to the room there.
	# Print an error message if the movement isn't allowed.
	options = ['n', 's', 'e', 'w']
	getRoom = [
		player1.location.n_to,
		player1.location.s_to,
		player1.location.e_to,
		player1.location.w_to
	]

	if len(direction) == 1 and direction in options:
		if getRoom[options.index(direction)] != None:
			print("\nYou move to the %c" % direction)
			player1.location = getRoom[options.index(direction)]
		else:
			print("\nInvalid: There's nothing that direction")
	elif direction == 'q':
		print("\nQuitting the game...")
		GamePlaying = False
	else:
		print("\nERROR: You can only move n, s, e, or w.")

	# If the user enters "q", quit the game.
