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
    # contructor
    def __init__(self, location):
        self.location = location

    # set_location()
    def set_location(self, location):
        self.location = location

    # move_north()
    def move_north(self):
        try:
            north = self.location['n_to']
            self.set_location(rooms.get(north))
            
            return '\n\n(N)orth'
        except:
            return f"There doesn't seem to be a passage to the north, try another direction."

    # move_east()
    def move_east(self):
        try:
            east = self.location['e_to']
            self.set_location(rooms.get(east))
            
            return '\n\n(E)ast'
        except:
            return f"There doesn't seem to be a passage to the east, try another direction."

    # move south
    def move_south(self):
        try:
            south = self.location['s_to']
            self.set_location(rooms.get(south))
            
            return '\n\n(E)ast'
        except:
            return f"There doesn't seem to be a passage to the south, try another direction."

    def move_west(self):
        try:
            west = self.location['w_to']
            self.set_location(rooms.get(west))
            
            return '\n\n(E)ast'
        except:
            return f"There doesn't seem to be a passage to the west, try another direction."

    # display_direction()
    def display_direction(self, rooms, direction):
        # player moving north
        if direction.lower() == 'n':
            return self.move_north()

        # player moving south
        if direction.lower() == 's':
            return self.move_south()

        # player moving east
        if direction.lower() == 'e':
            return self.move_east()

        # player moving west
        if direction.lower() == 'w':
            return self.move_west()

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
starting_room = rooms['outside']
player = Player(starting_room)

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

# print starting room description to user
# starting room is `Outside`
print(f"\n\n {player.location['description']}")

# grab the users input
user_input = input(f"\n\nYou may either (Q)uit or head (N)orth into the {player.location['n_to']}: ")

while (user_input.lower() != 'q'):
    print(player.display_direction(rooms, user_input))

    user_input = input('\n\nWhere to?: ')