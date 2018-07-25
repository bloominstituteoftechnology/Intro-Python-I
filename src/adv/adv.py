from room import Room
from player import Player
from commandslist import Commands
import math
import textwrap
import os

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
player1 = Player(input("Enter a username: ").strip()[0:20], room['outside'])
GamePlaying = True
message = None

# help functions
def formatMsg(msg):
	res = ""
	border = ""

	# is a list
	if type(msg) is list:
		# list is of dicts
		if type(msg[0]) is dict:
			print(len(msg[0].values()))

		# longest in the list
		length = len(max(msg, key=len)) + 6

		#sizes border
		for n in range(length + 2):
			border += "*"

		res += border
		for line in msg:
			res += "\n*"
			# separator
			if line == '=':
				res += " "
				for s in range(length - 2):
					res += '='
				res += " "
			# formats line
			else:
				spaceAmt = length - len(line)
				for s in range(math.ceil(spaceAmt / 2)):
					res += " "
				res += line
				for s in range(math.floor(spaceAmt / 2)):
					res += " "
			res += "*\n"
		res += border

		return res

	# single message
	else:
		for n in range(len(msg) + 9):
			border += "*"
		
		res = border + "\n*   " + msg + "   *\n" + border
		return res

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while GamePlaying == True:
	os.system('cls' if os.name == 'nt' else 'clear')
	desc = textwrap.wrap(player1.location.desc)

	if message != None:
		print(message)
	print("\n%s\n" % player1.location.name)
	for line in desc:
		print(line)

	# Input from user
	userInput = input("\nEnter direction: ").strip().lower()

	print("\n===========================================================\n")

	# If the user enters a cardinal direction, attempt to move to the room there.
	# Print an error message if the movement isn't allowed.

	# help / commands
	if userInput == 'h' or userInput == 'help' or userInput == 'commands':
		message = formatMsg(Commands)
	
	# move player
	elif len(userInput) == 1 and userInput in ['n', 's', 'e', 'w']:
		# is movable to
		if getattr(player1.location, userInput + '_to') != None:
			player1.location = getattr(player1.location, userInput + '_to')
			message = formatMsg("%s moved to the %c" % (player1.name, userInput))
		
		#is not movable to
		else:
			message = formatMsg("You can't move %c" % userInput)

	# display inventory
	elif userInput == 'i':
		message = formatMsg(player1.inventory)

	# quit game
	elif userInput == 'q' or userInput == 'quit' or userInput == 'exit':
		print("Quitting the game...")
		GamePlaying = False

	# invalid input
	else:
		message = formatMsg("Invalid input: use 'help' for commands")