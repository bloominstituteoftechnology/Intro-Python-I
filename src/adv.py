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
    def __init__(self, name):
        self.name = name
        self.current_room = outside
    
    def current_room(self, room):
        self.current_room = room
#
# Main
#

class Controller:
    def __init__(self, player, rooms):
        self.player = player
        self.rooms = rooms
    
    def move_north(self):
        print("move north")

    def move_south(self):
        print("move south")

    def move_east(self):
        print("move east")

    def move_west(self):
        print("move west")

    def start(self):
        player_move = input("Please enter n for north s for south w for west and e for east and q for quit")
        while(player_move != "q"):
            if(player_move == "n"):
                self.move_north()
                player_move = input("Please enter n for north s for south w for west and e for east and q for quit")
            elif(player_move == "s"):
                self.move_south()
                player_move = input("Please enter n for north s for south w for west and e for east and q for quit")
            elif(player_move == "w"):
                self.move_west()
                player_move = input("Please enter n for north s for south w for west and e for east and q for quit")
            elif(player_move == "e"):
                self.move_east()
                player_move = input("Please enter n for north s for south w for west and e for east and q for quit")
            else:
                player_move = input("Please enter n for north s for south w for west and e for east and q for quit")

            
newGame = Controller("Xang", "test")
newGame.start()




class Room: 
    def __init__(self, name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

class Board: 
    def __init__(self, player, rooms_obj):
        self.player = player
        self.rooms = rooms_obj
        # self.rooms_obj["outside"] = rooms_obj["outside"]
        # self.rooms_obj["foyer"] = rooms_obj["foyer"]
        # self.rooms_obj["overlook"] = rooms_obj["overlook"]
        # self.rooms_obj["narrow"] = rooms_obj["narrow"]
        # self.rooms_obj["treasure"] = rooms_obj["treasure"]
    

    


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
