# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
        "w_to": "garage",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
        "w_to": "library"
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
        "s_to": "maproom",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
    },

    "maproom": {
        "name": "Map Room",
        "description": "This is the map room, where all the maps that were used to acquire the treasure room are located!",
        "n_to": "narrow",
    },
    "library": {
        "name": "Library",
        "description": "This is where we study, so we can become enlightened individuals!",
        "e_to": "foyer",
        "s_to": 'garage',
    },
    "garage": {
        "name": "Garage",
        "description": "Where we have a 12 car garage, becase you know, we can. ;D",
        "n_to": "library",
        "e_to": "outside",
    }

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
class Player:
    def __init__(self, position):
        self.pos = rooms[position]
#
# Main
#


# Make a new player object that is currently in the 'outside' room.
new_player = Player('outside')

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
directions = {
    's':'s_to',
    'n':'n_to',
    'e': 'e_to',
    'w': 'w_to'
}

while True:
    print(new_player.pos['name'], ' is in ', new_player.pos['description'])
    move = input('Enter a direction or q to quit ')
    if move == 'q':
        break
    if move != 's' and move != 'n' and move != 'e' and move != 'w':
        print("{} is not a valid entry, please enter n, s, e, or w".format(move))
        continue
    if directions[move] in new_player.pos.keys():
        new_player.pos = rooms[new_player.pos[directions[move]]]
    else:
        print('Nothing to the {} of {}. Please enter a different direction or "q" to quit'.format(move, new_player.pos['name']))