# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.
import textwrap

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
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.freedom = 0
    
    def move(self, input):
        try:
            next_room = rooms[self.location][f'{input}_to']
        except KeyError:
            print(system_text['key_error'])
            return 
        self.location = next_room 

    def print_location(self):
        current_loc = rooms[self.location]
        print(f'*-------*\nLocation: {current_loc["name"]}\n')
        location_description = current_loc["description"]
        print_multilines(location_description)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p1 = Player('mister-corn','outside')
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

# A bunch of functions/dicts
system_text = {
    'welcome': 
    '''\nWelcome to adv.py!
Input a cardinal direction (e.g. 'n', 's', 'e', 'w') to explore the world.
Quit the game by inputting 'q'\n''',
    'key_error': 
    '''\nIt seems you cannot go that way...
(Remember, type in the cardinal direction you wish to move as a single lower-case letter. For example, type in 'n', 's', 'w', 'e'. Not all directions are valid. Read the description carefully to find out where you can go.)\n'''
}

def print_multilines(text):
    textwrap_list = textwrap.wrap(text)
    for line in textwrap_list:
        print(line)

# Game Start
print(system_text['welcome'])
p1.print_location()
player_input = input(">> ")

while player_input != 'q':
    p1.move(player_input)
    p1.print_location()
    player_input = input(">> ")

exit(0)
