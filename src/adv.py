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
class PlayerInfo:
    def __init__(self, startRoom):
        self.curRoom = startRoom

def directionalInput(d, curRoom):
    curLoc = d + "_to"

    if curLoc not in rooms[curRoom]:
        print("The door can't be opened from this side")
        return curRoom
    resultLocation = rooms[curRoom][curLoc]

    return resultLocation

    
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
pObject = PlayerInfo('outside')
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

done= False
while not done:

    print("\n{}\n".format(rooms[pObject.curRoom]['name']))

    for line in textwrap.wrap(rooms[pObject.curRoom]['description']):
        print(line)

    s = input("\nCommand> ").strip().lower()
    if s == "q":
        done = True

    elif s in ["n", "s", "w", "e"]:
        pObject.curRoom = directionalInput(s, pObject.curRoom)

    else:
        print("Unknown command {}".format(s))