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
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def currentRoom(self):
        print('This is the ' + self.room['name'])
        print('You see that ' + self.room['description'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

thePlayer = Player({"name": 'Jareth'}, rooms['outside'])
print('Greetings ' + thePlayer.name['name'] + '... Your adventure begins here...')
thePlayer.currentRoom()


moveOptions = {
    "n": "n_to",
    "e": "e_to",
    "s": "s_to",
    "w": "w_to"
}

playerMove = ''

while playerMove != 'q':
    playerMove = input("Enter (w)est, (e)ast, (n)orth, or (s)outh to move, or (q)uit")
    print(thePlayer.currentRoom())

    # if playerMove == 'q':
    #     print("Thanks for playing!")
    #     break

    if (playerMove != 'q'):
        moveAction = playerMove + '_to'
    
        try: 
            thePlayer.room[moveAction]

        except KeyError:
            print("Hey, listen! The {} direction proved to be troublesome to traverse, maybe you should try a different one...")
            print(thePlayer.room)

        else:
            thePlayer.room = rooms[thePlayer.room[moveAction]]
            thePlayer.currentRoom
    
    else:
        print('Thanks for playing, come back soon!')

# Write a loop that:
#
# * Prints the current room name
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
