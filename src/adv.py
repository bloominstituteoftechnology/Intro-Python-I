# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.
import random

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


current_room = 'outside'
# Write a class to hold player information, e.g. what room they are in currently
class player_information:
    def __init__(self, room, player):
        self.name = room[current_room]['name']
        self.description = room[current_room]['description']
        self.player = player
        self.health = 100

    def take_damage(self, trap):
        self.health = self.health - trap

venturer = player_information(rooms, 'Csaba')


print(venturer.health)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.


class Player:
    def __init__(self, position):
        self.position = rooms[position]

venturer = Player('outside')
directions = {
    's': 's_to',
    'n': 'n_to',
    'e': 'e_to',
    'w': 'w_to'
}


ways = directions.keys()

while True:

    user_input = input("Enter your direction: ").strip().lower()

    if user_input in ways: 
        if directions[user_input] not in rooms[current_room].keys():
            print("there is nothing in that way")
        elif rooms[current_room][directions[user_input]]:
            current_room = rooms[current_room][directions[user_input]]
            print("========================================\n\n")
            trap = random.randint(1,100)
            if trap > 50:
                venturer.take_damage(trap)
                print("you walked into a trap and your new health is {}\n\n".format(venturer.health))
            if venturer.health < 0:
                print("Game Over you died")
                break
            else:
                print("room: " + rooms[current_room]['name'] + "\n")
                print("description: " + rooms[current_room]['description'] + "\n\n")
                print("========================================")
        else:
            continue
    elif user_input == 'q':
        print("good bye" + venturer.player)
        break
    else:
        print("use 'w', 'e', 's', 'n' keys to navigate your character, or use 'q' to quit from the game")





# while True:
#     print(venturer.name)
#     print(venturer.description)

#     move = input("Choose your direction venturer: ")
#     if move == 'q':
#         break
#     elif move in directions:
#         if directions[move] in venturer.position.keys():
#             venturer = rooms[venturer.position[directions[move]]]
#         else:
#             print("There is nothing in that direction, choose something else")
#     else:
#         print("Use 'w' 'e' 's' 'n' to chose directions, and 'q' to quit game")


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
