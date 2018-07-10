# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "objects": {},
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north, east and west.",
        "objects": {},
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
        "w_to": "study",
    },

    "study": {
        "name": "Study",
        "description": "You come across a small room with book shelves on either wall and a desk to the west.",
        "objects": {},
        "e_to": "foyer",
        "w_to": "desk",
    },

     "desk": {
        "name": "Desk",
        "description": "You walk up to the desk. It has many drawers to search through. The surface is covered with old papers in writing you don't recognize.",
        "objects": {
            "key": "An old key"
        },
        "e_to": "study",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "objects": {},
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "objects": {},
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been pillaged by
earlier adventurers. All that remains is a strange cup on the floor and a door to the east.""",
        "objects": {
            "cup": "Strange Cup from Treasure Chamber",
        },
        "s_to": "narrow",
        "e_to": "door",
    },

    "door": {
        "name": "Treasure Door",
        "description": "You approach the very large, old door. You try to push it open with all your might, but it doesn't budge. You notice a key hole. Perhaps the door can be unlocked.",
        "objects": {},
        "w_to": "treasure",
    },

}

""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        "objects": {},
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
    },
"""

# Write a class to hold player information, e.g. what room they are in currently

class Player:
    def __init__(self, room, inventory):
        self.room = room
        self.inventory = {}

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

p = Player("outside", [])

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
    elif action == "i":
        print(p.inventory)
    elif action == "search":
        if currentRoom["objects"] == {}:
            print("There are no discoverable items in this area")
        else:
            print(currentRoom["objects"])
            
    else:
        print("Action does not exist. Press 'n' to go north, 's' to go south, 'e' to go east, 'w' to go west, or 'q' to quit the game")