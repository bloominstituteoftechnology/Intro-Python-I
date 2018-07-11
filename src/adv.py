# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

import textwrap

# These are the existing rooms. Add more as you see fit.

rooms = {
    "menu": {
        "name": "TXT ADVNTR",
        "description": 
            """
            Welcome to TXT ADVNTR! Commands are: north, south, east, west, and q to quit. Type north to begin!
            """,
        "north_to": "outside"
    },

    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "north_to": "foyer",
        "west_to": "shortcut"
    },

    "shortcut": {
        "name": "Secret Shortcut to the Forest Beyond",
        "description": "You discover a secret path!",
        "west_to": "deep_forest",
        "east_to": "outside"
    },

    "foyer": {
        "name": "Foyer",
        "description": """Dim light filters in from the south. 
Dusty passages run north and east. You smell cookies to the west.""",
        "north_to": "overlook",
        "south_to": "outside",
        "east_to": "narrow",
        "west_to": "passage"
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "south_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": """The narrow passage bends here from west to north. 
The smell of gold permeates the air.""", 
        "west_to": "foyer",
        "north_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "south_to": "narrow",
    },

    "passage": {
        "name": "Mysterious Passage",
        "description": """A passage beckons you west. You smell cookies coming 
from a hut by the cliff to the north. To the West lies a forest.""",
        "north_to": "trap",
        "east_to": "foyer",
        "west_to": "forest"
    },

    "trap": {
        "name": "Trap Room",
        "description": """IT'S A TRAP! A Witch that is baking cookies 
and casts a spell on you, leaving you paralyzed.""",
    },

    "forest": {
        "name": "The Forest Beyond",
        "description": """You enter a dark and dank forest, 
will you venture further, or will you retreat?""",
        "north_to": "clearing",
        "south_to": "deep_forest",
        "east_to": "passage",
        "west_to": "stream",
    },

    "clearing": {
        "name": "Clearing By The Cliff",
        "description": """You come out of the trees to a clearing
by the cliff. To the East, you smell cookies comming from a hut""",
        "south_to": "forest",
        "east_to": "trap",
    },

    "deep_forest": {
        "name": "Deeper into the Forest Beyond",
        "description": "You venture deeper.",
        "north_to": "forest",
        "east_to": "shortcut",
        "west_to": "downstream",
    },

    "stream": {
        "name": "The River Geraltia",
        "description": "A river blocks the way west.",
        "east_to": "forest",
        "south_to": "downstream"
    },

    "downstream": {
        "name": "Southern River Geraltia",
        "description": "The river blocks the way west.",
        "north_to": "stream",
        "east_to": "deep_forest"
    }
}

""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        "north_to": "",
        "south_to": "",
        "east_to": "",
        "west_to": "",
    },
"""

# Write a class to hold player information, e.g. what room they are in currently
class Player:
    def __init__(self, startRoom):
        self.currentRoom = startRoom

def tryDirection(direction, currentRoom):
    key = direction + "_to"

    if key not in rooms[currentRoom]:
            print("Forbidden")
            return currentRoom

    move = rooms[currentRoom][key]

    return move

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('menu')

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

while not done:
    print("\n{}\n".format(rooms[player.currentRoom]['name']))

    for line in textwrap.wrap(rooms[player.currentRoom]['description']):
        print(line)

    command = input("\nWhere will you go? ").strip().lower()

    if command == "q":
        done = True
    elif command in ["north", "south", "east", "west"]:
        player.currentRoom = tryDirection(command, player.currentRoom)
    else:
        print("Unknown command {}".format(command))
