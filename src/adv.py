# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.
import textwrap

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "items": "hatchet",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "items": "sboots",
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
        "description": """The narrow passage bends here from west to north. 
The smell of gold permeates the air.""", 
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "items": "hatchet",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied, by earlier adventurers
except for a hatchet on the floor. 
There is an exit east across a trecherous rope bridge,
or you could go south back the way you came.
""",
        "s_to": "narrow",
        "e_to": "rbridge"
    },
    "rbridge": {
        "name": "Rope Bridge",
        "description": """There are two exits from the end of the bridge, one to the north which leads 
        to a grove of some kind, and one to the west which is partially covered in snow.
        """,
        "n_to": "grove",
        "e_to": "snowyexit",
        "w_to": "narrow",
    },
    "grove": {
        "name": "Secluded Grove",
        "description": """A Secluded Grove, duh. There is no exit here, nothing to see,
go back the way you came 
""",
        "s_to": "rbridge",
    },
    "snowyexit": {
        "name": "Snowy Exit",
        "description": """ You knock some of the snow out of the way to get a better view.
        It looks as if this exit opens up to the side of a mountain,
        there is a small ledge but you do not have the correct footwear to proceed. Maybe there
        is a room somewhere that has what you are looking for.
        """,
        "e_to": "rbridge",
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

items = {
    "hatchet": {
        "name": "Rusty Hatchet",
        "description": "A rusted piece of sharpened metal, can hardly be called a sword",
        "str": 1,
        "weight": 1
    },
    "sboots": {
        "name": "Snow Boots",
        "description": "A pair of boots made for traversing snowy conditions",
        "weight": 1,
    }
}

inventory = []

# Write a class to hold player information, e.g. what room they are in currently
class Player:
    def __init__(self, name, startLocation, inv):
        self.name = name
        self.location = startLocation
        self.inv = inv
   
    

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

newPlayer = Player("Sam", "outside", "")

#def take(take, location, item):

def take(item):
    actualItem = items[item]
    inventory.append(actualItem)
    newPlayer.inv = inventory

    print("\n{}\n".format(inventory))


def directional(d, location):
   
    key = d + "_to"

    if key not in rooms[location]:
        print("You bump into a wall, try another direction")
        return location

    destination = rooms[location][key]

    return destination

done = False

while not done:
    print("\n{}\n".format(rooms[newPlayer.location]['name']))

    for l in textwrap.wrap(rooms[newPlayer.location]['description']):
        print(l)

    s = input(">> ").strip().lower()

    if s == "q":
        done = True
    
    elif s in ["n", "s", "e", "w"]:
        newPlayer.location = directional(s, newPlayer.location)

    elif s == "inv":
        print(" \n{}\n \n".format(newPlayer.inv))

    elif s == "l":
        print("\n{}\n".format(rooms[newPlayer.location]['description']))

    
    elif s == "take hatchet":
        take(rooms[newPlayer.location]['items'])
 
    elif s == "take snow boots":
        take(rooms[newPlayer.location]['items'])
        
    
    elif s == "help":
        print("Help \n Use n,s,e,w to navigate \n q to exit game \n type stats to see your stats \n type inv to see your inventory")

    else:
        print("Incorrect input {}".format(s))