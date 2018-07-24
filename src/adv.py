import textwrap
import sys
# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

rooms = {
    "outside": 
    {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n": "foyer",
        "e": "bridge"
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n": "overlook",
        "s": "outside",
        "e": "narrow",
        "w": "armory"
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "s": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w": "foyer",
        "n": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s": "narrow",
    },

    "bridge": {
        "name": "Bridge",
        "description": """Rough winds blow acoss a lonely bridge. The smell of dragon fire and brimstone is heavy here.
On the other side you see a red dragon sleeping in the sunlight. It guards the entrance to an ancient cathedral""",
        "w": "outside",
        "n": "cathedral"
    },

    "cathedral": {
        "name": "Cathedral",
        "description": """Broken pews, torn tapestries, and skeletons of past adventurers are all that remain inside.
At the end, sunlight illuminates the lady's chapel. You see a crack in the wall.""",
        "n": "narrow",
        "s": "bridge"
    },

    "armory": {
        "name": "Armory",
        "description": """You find a small armory filled with rusted weapons and some tools. At the far end lies a chest but it's locked.
You find an encryption on the chest lid: 'The ancient hero offers his sword but only to those he deems worthy' """,
        "e": "foyer"
    }

}

""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        "n": "",
        "s": "",
        "e": "",
        "w": "",
    },
"""

# Write a class to hold player information, e.g. what room they are in currently
class Player:
    def __init__(self,room):
        self.room = room
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player(rooms["outside"])
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

quit = False # describes game state

while not quit:
    print("current room: {0}".format(new_player.room["name"]))
    print(textwrap.fill(new_player.room["description"]))
    move_to_room = input("Where will you go next?")
    if move_to_room == "q":
        quit = True
        sys.exit(1)
    print("player wants to move {0}".format(move_to_room))
    # validate player input - is the next room a neighbor to the current one?
    if move_to_room in new_player.room:
        new_room = new_player.room[move_to_room]
        print("player chose to move in {0} direction to the {1} room".format(move_to_room, new_room))
        # update player instance with the new room
        new_player.room = rooms[new_room]
    else:
        # player enters an invalid direction
        print("Please enter a valid direction: n_to, e_to, s_to, or w_to")





