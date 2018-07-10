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

#
# Main
#
class Main:
    def __init__(self, player, room):
        self.player = player
        self.room = room
    
    def getRoom(self):
        print('***********************************')
        print('You are in: ' + self.room['name'])
        print('This room is: ' + self.room['description'])
        
        
# Make a new player object that is currently in the 'outside' room.
playerA = Main({'name': 'Thuy'}, rooms['outside'])
print('Welcome ' + playerA.player['name'] + '!')
playerA.getRoom()

move = ''

while move != 'q':
    move = input(">>>>>>Your next move? w(west), s(south), n(north), e(east) or q(quit): ")
    
    if (move != 'q'):
        moveKey = move + '_to'
        
        try:
            playerA.room[moveKey]
        except KeyError:
            print('There is no way on that direction! Try again!')
            print(playerA.room)
        else:
            playerA.room = rooms[playerA.room[moveKey]]
            playerA.getRoom()
    else:
        print('See you later!')
        
    