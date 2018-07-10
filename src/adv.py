# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
 		},

}

""" template room to copy into code
		"room": {
			"name": "",
			"description": "",
			"n_to": "",
			"s_to": "",
			"e_to": "",
			"w_to": "",
		},
"""

# Write a class to hold player information, e.g. what room they are in currently
	

class Userlocation:
	def __init__(self, roomname):
		self.roomname = rooms[roomname]
#
# Main
#
# Make a new player object that is currently in the 'outside' room.

newplayerobject = Userlocation('outside')

# Write loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# 
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

import textwrap
# Don't forget this part!

carddir = {
'n': 'n_to',
's': 's_to',
'e': 'e_to',
'w': 'w_to',
}

start = input('Enter "b" to begin the game, or any other key to exit: ')
if start == 'b':
	myloop = True 
else:
	myloop = False

# Xang suggested that I make it so the player is not thrown directly into the game as soon as they run it, and can choose when to start.
# but I think he thinks this is still not right because it doesn't encapsulate my loop?? I don't know. I trust his judgment on this as I don't really play games but I'm not sure how to fix it yet.

while myloop:
	print(newplayerobject.roomname['name'])
	print(textwrap.fill(newplayerobject.roomname['description']))

# I really thought it ought to be textwrap(wrap) based on the docs but that ended up including the brackets. Good to know for future reference.
	
	plyrinput = input('Enter a direction (n,s,e,w) or "q" to quit: ')
	if plyrinput == 'q':
		break
 
# section 4.4 in the python docs - this ends the loop

	if plyrinput not in carddir:
		print('invalid input, please try again')
		continue

# this allows the player to try again - before I put this in, the game would just end as soon as someone entered 'd' or something.
	
	if carddir[plyrinput] in newplayerobject.roomname.keys():
		newplayerobject.roomname = rooms[newplayerobject.roomname[carddir[plyrinput]]]

# I think I tried about 17 different variants of this before it worked.
# If the plyrinput actually matches a cardinal direction (nsew) which also happens to be valid, then reassign the newplayerobject's roomname to the new room. 

	else:
		print('Ow! Quit walking into walls! Try a different direction.')

# Otherwise, if the player enters a nsew direction but it is not valid according to the rooms object(dict?), then tell them to try again.
