# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.
import textwrap

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
class Player:
    def __init__(self, location, hp):
        self.location = location
        self.hp = hp

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(rooms['outside'], 10)
playing = True
# Write a loop that:
while playing is True:
    # desc = TextWrapper(width = 150, initial_indent="    ", fill=player.location['name'])
# * Prints the current room name
    print('\nLocation: %s' % (player.location['name']))
# * Prints the current description (the textwrap module might be useful here).
    print(player.location['description'])
# * Waits for user input and decides what to do.
    direction = str(input('\n\nWhich way will you go? n, s, e, w (q to quit): '))
#
# If the user enters a cardinal direction, attempt to move to the room there.
    try:
        if direction == 'n':
            player.location = rooms[player.location['n_to']]
        elif direction == 's':
            player.location = rooms[player.location['s_to']]
        elif direction == 'e':
            player.location = rooms[player.location['e_to']]
        elif direction == 'w':
            player.location = rooms[player.location['w_to']]
        elif direction == 'q':
            break
    except:
        raise ValueError("That is not an option.")
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
