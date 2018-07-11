import textwrap

# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.
"""
Mamooshka = "player 1"

welcomeIntro = "Welcome to Bee's adventure land game.\nEnter if you dare..."
east"
"""

# rooms['outside]
# rooms['outside']['description']
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
class PlayerInfo:
    #i__nit__ is like a constructor
    # self is like this in JS
    def __init__(self, roomNow):
        self.currRoom = roomNow

def directionMove(d, currRoom): #d='w' currRoom = 'outside'

    key = d + "_to" # print(key) => "w_to"

    if key not in rooms[currRoom]: #rooms['outside'] => {-------}
        print("Move not allowed.\nPick another direction.")
        return currRoom

    location = rooms[currRoom] [key] # rooms['foyer']['n_to']
    return location #'overlook'

    

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = PlayerInfo('outside')

#     print(newPlayer.currRoom)
# Write a loop that: 
#
# * Prints the current room name
#     print(newPlayer.currRoom)
# * Prints the current description (the textwrap module might be useful here).
#     rooms[newPlayer.currRoom]['description']
# rooms['outside']['description']
# * Waits for user input and decides what to do.
#
 #     d = input("Where do you want to go (w=west, n=north, s=south, e=east): ") # 'w'
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
#     directionMove(d, newPlayer.currRoom) #  ('w', 'outside')

done = False

## Write a loop that:
while not done:
# * Prints the current room name
    print(newPlayer.currRoom)

# * Prints the current description (the textwrap module might be useful here).
rooms[newPlayer.currRoom]['description']

# * Waits for user input and decides what to do.
d = input("Where do you want to go (w=west, n=north, s=south, e=east): ") # 'w'


# Handle input
if d == "q":
    done = True
elif d in ["n", "s", "w", "e"]:
    newPlayer.currRoom = directionMove(d, newPlayer.currRoom)
else:
    print("Unknown command {}".format(d))


"""    PERSONAL NOTES
a single underscore ( _ ) in front of a variable name (prefix) is a hint that a variable is meant for internal use only.
a double underscore ( __ ) causes the Python interpreter to rewrite the vaiable name in order to avoid naming conflicts in subclasses.
"""