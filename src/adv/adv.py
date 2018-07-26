from roomlist import RoomList
from player import Player
from commandslist import Commands
import math
import textwrap
import os

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
os.system('cls' if os.name == 'nt' else 'clear')
print(formatMsg(['Welcome to the Game']))
player1 = Player(input("\nEnter a username: ").strip()[0:20], RoomList['outside'])
GamePlaying = True
message = None

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