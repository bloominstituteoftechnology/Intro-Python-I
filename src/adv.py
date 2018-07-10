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
    def __init__(self, room):
        self.room = room

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

p = Player("outside")

game = True

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

while game:
    currentRoom = {key: value for key, value in rooms.items() if key == p.room}
    currentRoom = next(iter(currentRoom.values()))
    print(f"\nCurrent Location: {currentRoom['name']}\n")
    print(currentRoom['description'])
    action = input("\nWhich way would you like to go?\n")
    if action == "q":
        game = False
        print("\nGame Over\n")
    elif action == "n":
        if "n_to" in currentRoom:
            p.room = currentRoom["n_to"]
            print("You move north...")
        else:
            print("Something blocks your path, you cannot go north. Try another direction")
    elif action == "s":
        if "s_to" in currentRoom:
            p.room = currentRoom["s_to"]
            print("You move south...")
        else:
            print("Something blocks your path, you cannot go south. Try another direction")
    elif action == "e":
        if "e_to" in currentRoom:
            p.room = currentRoom["e_to"]
            print("You move east...")
        else:
            print("Something blocks your path, you cannot go east. Try another direction")
    elif action == "w":
        if "w_to" in currentRoom:
            p.room = currentRoom["w_to"]
            print("You move west...")
        else:
            print("Something blocks your path, you cannot go west. Try another direction")
    else:
        print("Action does not exist. Press 'n' to go north, 's' to go south, 'e' to go east, 'w' to go west, or 'q' to quit the game")