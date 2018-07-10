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
class player:
    def __init__(self,currentRoom):
        self.currentRoom = currentRoom
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
samar = player("outside")

userInput = ''

while userInput != 'q':
    print(samar.currentRoom)
    room = rooms[samar.currentRoom]
    print(room["description"])
    
    userInput = input("Please give directions beep-beep - 'n' for North, 's' for South, 'w' for West, 'e' for East or press 'q' to quit: ")
    
    if userInput not in ['s', 'n', 'q', 'w', 'e']:
        print("   you dead mate!   ")
        break
        
    if userInput == 'n':
        try:
            samar = player(room["n_to"])
        except:
            print("you can't go there mate that's risky AF!!!")

        
    if userInput == 's':
        try:
            samar = player(room["s_to"])
        except:
            print("you can't go there mate that's risky AF!!!")
    
    if userInput == 'w':
        try:
            samar = player(room["w_to"])
        except:
            print("you can't go there mate that's risky AF!!!")
        
    if userInput == 'e':
        try:
            samar = player(room["e_to"])
        except:
            print("you can't go there mate that's risky AF!!!")
        


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
