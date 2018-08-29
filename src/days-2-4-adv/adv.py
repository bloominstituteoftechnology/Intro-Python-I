import textwrap
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Dan", room["outside"])
# print(player.current_room)
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


# def choosePath(room, path):
#     if path == "n" and room.n_to:
#         return True
#     elif path == "s" and room.s_to:
#         return True
#     elif path == "e" and room.e_to:
#         return True
#     elif path == "w" and room.w_to:
#         return True
#     else:
#         print("\n ===== Please return a valid selection (N), (S), (E) or (W) =====\n")


while True:
    print("%a" % (player.current_room.name))
    print("%a" % (player.current_room.description))

    path = input(
        "Choose your path (N)North, (S)South, (E)East, (W)West, or (Q)Quit\n").lower()

    if path == "q":
        print("I guess you were too scared to play")
        break
    else:
        if path == "n" and hasattr(player.current_room, "n_to"):
            player.current_room = player.current_room.n_to
        elif path == "s" and hasattr(player.current_room, "s_to"):
            player.current_room = player.current_room.s_to
        elif path == "e" and hasattr(player.current_room, "e_to"):
            player.current_room = player.current_room.e_to
        elif path == "w" and hasattr(player.current_room, "w_to"):
            player.current_room = player.current_room.w_to
        else:
            print("\n === You cant go this way ===\n")

# choosePath()
# roomNames()
