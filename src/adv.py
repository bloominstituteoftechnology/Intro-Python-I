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
        "e": "bridge",
        "i": "show inventory"
    },

    "foyer": {
        "name": "Foyer",
        "description": """Dim light filters in from the south. Dusty passages run north and east.
You find a potion and a parchment which says 'Drink this to fight foul monsters but beware. Your urge to kill grows with every strike' """,
        "items": ['torch', 'potion', 'parchment'],
        "n": "overlook",
        "s": "outside",
        "e": "narrow",
        "w": "armory",
        "i": "show inventory"
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """You find the ancient hero's statue and find his sword locked in its scabbard. Beyond,a steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "items": ["hero's sword"],
        "s": "foyer",
        "i": "show inventory"
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w": "foyer",
        "n": "treasure",
        "s": "cathedral",
        "i": "show inventory"
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, all but a brass key have been taken by
earlier adventurers. The only exit is to the south.""",
        "items": ["brass key"],
        "s": "narrow",
        "i": "show inventory"
    },

    "bridge": {
        "name": "Bridge",
        "description": """Rough winds blow acoss a lonely bridge. The smell of dragon fire and brimstone is heavy here.
On the other side you see a red dragon sleeping in the sunlight. It guards the entrance to an ancient cathedral""",
        "w": "outside",
        "n": "cathedral",
        "e": "outside",
        "i": "show inventory"
    },

    "cathedral": {
        "name": "Cathedral",
        "description": """Broken pews, torn tapestries, and skeletons of past adventurers are all that remain inside.
At the end, sunlight illuminates the lady's chapel. You see a crack in the wall.""",
        "n": "narrow",
        "s": "bridge",
        "i": "show inventory"
    },

    "armory": {
        "name": "Armory",
        "description": """You find a small armory filled with rusted weapons and some tools. At the far end lies a locked chest
and a blackened shield. You find an encryption on the chest lid: 'The ancient hero offers his sword but only to those he deems worthy' """,
        "items": ["blackened shield"],
        "e": "foyer",
        "i": "show inventory"
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
        self.inventory = []
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

    # show items in room when player walks in"items"]
    if "items" in new_player.room:
        print("Items: {0}".format(new_player.room["items"]))
    player_input = input("Where will you go next?")
    # quit game
    if player_input == "q":
        quit = True
        sys.exit(1)

    # validate player input - is the next room a neighbor to the current one?
    if player_input in new_player.room:
        new_room = new_player.room[player_input]
        # update player instance with the new room
        new_player.room = rooms[new_room]
    else:
        # player enters an invalid direction
        print("Please enter a valid direction: n_to, e_to, s_to, or w_to")





