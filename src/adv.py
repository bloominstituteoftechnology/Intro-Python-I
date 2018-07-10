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

# This is the list of available items in the game
items = {
    {
        "name": "Wooden Sword",
        "description": "Basic weapon to attack against weak enemies",
        "value": "10 HP"
    },
    {
        "name": "Wooden Shield",
        "description": "Basic shield to defend against enemies attacks",
        "value": "20 HP"
    },
    {
        "name": "Bronze Sword",
        "description": "A better sword for attacking enemies",
        "value": "20 HP"
    },
    {
        "name": "Bronze Shield",
        "description": "A more solid shield to defend against enemies",
        "value": "40 HP"
    },
    {
        "name": "Silver Sword",
        "description": "A great sword for destroying enemies",
        "value": "40 HP"
    },
    {
        "name": "Silver Shield",
        "description": "A great and sturdy shield to defend against enemies",
        "value": "80 HP"
    },
    {
        "name": "Excalibur",
        "description": "THE ULTIMATE SWORD OF SWORDS FOR VANQUISHING FOOLS",
        "value": "100 HP"
    },
    {
    "name": "Golden Shield",
        "description": "A ancient shield blessed by Zeus",
        "value": "200 HP"
    }
}

# Write a class to hold player information, e.g. what room they are in currently
class Player:
    """Will include playerName, currentRoom, playerInventory, and playerSkills"""
    def __init__(self, playerName, currentRoom, playerInventory, playerSkills)
        self.name = playerName
        self.location = currentRoom
        self.inventory = playerInventory
        self.skills = playerSkills

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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
