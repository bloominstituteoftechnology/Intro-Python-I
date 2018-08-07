# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

import textwrap

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
        "contents": ['5 Gold Coins', 'Unknown Potion', 'Ration', 'Ration', 'Worn Pants']
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
        "contents": ['Stuff', 'Things', 'Other Stuff']
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "s_to": "foyer",
        "contents": ['Stuff', 'Things', 'Other Stuff']
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w_to": "foyer",
        "n_to": "treasure",
        "contents": ['Stuff', 'Things', 'Other Stuff']
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
        "contents": ['Stuff', 'Things', 'Other Stuff']
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
    def __init__(self, initRoom):
        self.currentRoom = initRoom
        self.health = 100
        self.inventory = ["6ft rope", "ration", "ration", "ration", "flint & steel", "small dagger"]

def movement(move, currentRoom):
    key = move + "_to"
    if key not in rooms[currentRoom]:
        print("\nChoose a different direction.\n")
        return currentRoom

    room = rooms[currentRoom][key]

    return room

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

Johnny = Player('outside')

completed = False
initialEntry = False

# Game Loop

while not completed:

    while not initialEntry:
        # Prints the current room name
        print("\n" + rooms[Johnny.currentRoom]['name'] + "\n")
        
        # Prints the current description (the textwrap module might be useful here).
        for line in textwrap.wrap(rooms[Johnny.currentRoom]['description']):
            print(line)
        
        initialEntry = True
    # Waits for user input and decides what to do.   
    attempt = input("\nChoose n, s, e or w for direction,\nc for contents of room, i for inventory and q to quit: \n").lower()
    
    # If the user enters "q", quit the game.
    if attempt == 'q':
        completed = True
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif attempt in ['n', 's', 'e', 'w']:
        Johnny.currentRoom = movement(attempt, Johnny.currentRoom)
        # Prints the current room name
        print("\n" + rooms[Johnny.currentRoom]['name'] + "\n")
        
        # Prints the current description (the textwrap module might be useful here).
        for line in textwrap.wrap(rooms[Johnny.currentRoom]['description']):
            print(line)
    elif attempt == 'c':
        print("\nContents of room: ")
        for item in rooms[Johnny.currentRoom]['contents']:
            print(item)
    elif attempt == 'i' or attempt == 'inventory':
        print("\nMy inventory contains: ")
        for item in Johnny.inventory:
            print(item)
    # Print an error message if the movement isn't allowed. 
    else:
        print("\nYou have entered an invalid option.\n")
