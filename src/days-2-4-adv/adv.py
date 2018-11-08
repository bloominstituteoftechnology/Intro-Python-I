from room import Room
from player import Player
import textwrap
from item import Item

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
                     "North of you, the cave mount beckons", [Item("sword"), Item("key")]),

    'foyer':    Room("in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",["dragon's egg"]),

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

directions = {"N","S","W","E","n","s","w","e"}
action_verbs = {"take", "drop"}

# Make a new player object that is currently in the 'outside' room.
def printList(array):
	result = []
	for item in array:
		result.append(item.name)
	return result


def play_game():
	clear()
	print("Welcome to the game!")
	name = input("Type your name to begin:")
	
	player = Player(name, room["outside"], [Item("torch"), Item("book")])

	while True:
		clear()
		print(f"You are {player.location.name}:")
		print(" ".join(textwrap.wrap(player.location.description)))
		
		print("\nYour items: " + ", ".join(printList(player.inventory)))

		if len(player.location.items) > 0:
			print("Items in the room: " + ", ".join(printList(player.location.items)))
		
		user_input = input("\nWill you go N, S, E, or W? ")

		#  exits game
		if user_input.lower() == "q":
			break

		input_split = user_input.split(" ", 1)

		# User chooses a direction
		if len(input_split) == 1:
			try:
				if not user_input in directions:
					raise ValueError()
			except ValueError:
				clear()
				input(f"{user_input} is not a valid direction. Press enter to try again")
				continue

			player.try_move(user_input.lower())
		elif len(input_split) == 2:
			# User chooses an action
			verb = input_split[0].lower()
			item = input_split[1].lower()
			if verb in action_verbs:
				if verb.lower() == "take":
					player.pickup_item(item)
				elif verb.lower() == "drop":
					player.drop_item(item)
			else:
				input("You cannot perform this action. Hit Enter to try again")
		else:
			input("Invalid input. Press enter to try again.")





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

play_game()
