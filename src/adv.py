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

##This only works for windows
from msvcrt import getch
from msvcrt import kbhit


import _thread
import time




# Write a class to hold player information, e.g. what room they are in currently

class Player:
  def __init__(self, name, room):
    self.name = name
    self.room = room
  def __str__(self):
    strMsg = "Player {}"
    return strMsg.format(self.name)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Vlad', 'outside')

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

char = None

def keypress():
    global char
    char = getch().decode('utf-8')
    print('')
    return char

while(char != 'q'):
  try:
    # clear the keyboard buffer
    while kbhit():
      getch()
    room = rooms[player.room]
    print("%s you are in %s" % (player, room['name']))
    print("%s" % (room['description']))
    keypress()
    if char == 'n':
      player.room = room['n_to']
    elif char == 'w':
      player.room = room['w_to']
    elif char == 's':
      player.room = room['s_to']
    elif char == 'e':
      player.room = room['e_to']
    elif char == 'q':
      print('Goodbye!')
    else:
      print('Invalid key try: n, s, e or w')
  except KeyError:
    print("Oops!  That was no valid.  Try again...")
