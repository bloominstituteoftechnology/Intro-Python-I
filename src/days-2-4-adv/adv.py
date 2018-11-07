from room import Room
from player import Player
import textwrap

# import only system from os 
from os import system, name 
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
   
# Declare all the rooms

room = {
    'outside':  Room("outside the Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("at the Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """You've found the long-lost treasure
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
def game():
	clear()
	print("Welcome to the game!")
	name = input("Type your name to begin:")
	
	player = Player(name, room["outside"])

	while True:
		clear()
		print(f"You are {player.location.name}:")
		print(" ".join(textwrap.wrap(player.location.description)))
		direction = input("Will you go N, S, E, or W? ")

		if direction.lower() == "q":
			break

		try:
			if not (direction == "N" or direction == "S" or direction == "E" or direction == "W"):
				raise ValueError()
		except ValueError:
			clear()
			input(f"{direction} is not a valid direction. Press enter to try again")
			continue

		if direction == "N":
			next = player.location.n_to
		elif direction == "S":
			next = player.location.s_to
		elif direction == "E":
			next = player.location.e_to
		else:
			next = player.location.w_to
		if next:
			player.location = next
		else:
			clear()
			print("There is nothing in that direction")
			input("Press enter to try again")
			continue
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

game()
