from room import Room
from player import Player
from item import Item
import textwrap
from os import system
import platform

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Map", "Map is faded but still readable"), Item("Sword", "Rusted sword that could still be used to fight enemies")]),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Overlook", """A steep cliff appears before you, falling
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
player = Player("Stan", room['outside'], [])

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
done = False

def clear():
   if platform.system() == "Linux" or platform.system() == "Mac":
       _ = system("clear")
   elif platform.system() == "Windows":
       _ = system("cls")

while not done:
	curRoom = player.room
	
	prettyDesc = textwrap.fill(curRoom.description)
	
	print(f'{curRoom.name}\n{prettyDesc}\n{curRoom.itemList}')

	command = input("Command > ").strip().split(" ")

	if command[0] == 'q' or command[0] == 'quit' or command[0] == 'exit':
		done = True

	elif command[0] in ["s", "n", "e", "w"]:
		dirAttr = command[0] + "_to"

		if hasattr(curRoom, dirAttr):
			player.room = getattr(curRoom, dirAttr)

		else:
  			print("You can't go that way.")

	elif command[0] in ['m']:
		for i in range (len(player.inventory)):
  			if player.inventory[i].name == 'map':
  				  player.check_map()
		print("there is no map!")

	elif command[0] == 'Grab':
		player.addToInventory(command[1])
		pass

	elif command[0] == 'drop':
  		player.dropItem(command[1])

	elif command[0] == 'inventory':
		clear()
		player.showInventory()

  					  
	else:
		print("I don't understand that.")

