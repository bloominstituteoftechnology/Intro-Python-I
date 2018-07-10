import re
import os
import time
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


class Player:
    def __init__(self, startingLocation):
        self.location = startingLocation

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
gertrudiz = Player('outside')

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

gameStates = {
    'correctInput': True,
    'allowedDirections': [],
    'lastDirecton': 'input',
}


def printWrongInput():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''

ADVENTURE TO THE TREASURE.
{'-'*20}

Bad direction, please pick one of these: n = north, s = south, w = west, e = east
'''
          )

    time.sleep(5)


def printMessage():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
    
ADVENTURE TO THE TREASURE.
{'-'*30}
Current location: {rooms[gertrudiz.location]['name']}...

{rooms[gertrudiz.location]['description']}
'''
          )

    # print(gertrudiz.location)
    # print(gameStates)


def processInput(input):
    if input == 'q' or input == 'Q':
        gertrudiz.location = None
    if ['n', 's', 'e', 'w'].__contains__(input) and rooms[gertrudiz.location].__contains__(input + '_to'):
        gameStates['correctInput'] = True
        gertrudiz.location = rooms[gertrudiz.location][input + '_to']
    else:
        gameStates['correctInput'] = False


def game():
    printMessage()

    while gertrudiz.location:
        newLocation = input(
            '\nWhere to go? (n = north, s = south, w = west, e = east): ')

        processInput(newLocation)

        if not gameStates['correctInput']:
            printWrongInput()

        printMessage()



# STRECH
#  1. Add more rooms
#  2.
game()
