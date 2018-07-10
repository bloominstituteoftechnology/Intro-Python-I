# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.
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

    "mirror": {
        "name": "Mirror Room",
        "description": "Covered head-to-toe in glass - A good place to reflect on your day.",
        "n_to": "foyer",
        "s_to": "overlook",
    },

}




# Write a class to hold player information, e.g. what room they are in currently
class Player:
    def __init__(self, currentRoom):
        self.currentRoom = rooms[currentRoom]

        
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player("outside")


moves = {
'n': 'n_to',
's': 's_to',
'e': 'e_to',
'w': 'w_to',
}

while True:
    print(newPlayer.currentRoom["name"])

    print(textwrap.fill(newPlayer.currentRoom["description"]))

    userInput = input('What direction would you like to go next? n, s, e, w, or q to quite the game..')

    if userInput not in moves:
        print('The directions you have given do not exist. Please choose n, s, e, w, or q to quite the game..')
        continue

    if userInput == 'q':
        break

    if moves[userInput] in newPlayer.currentRoom.keys():
        newPlayer.currentRoom = rooms[newPlayer.currentRoom[directions[userInput]]]

    else:
        print("That's not a valid direction! try again.")

        
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
