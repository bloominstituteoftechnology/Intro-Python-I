import textwrap
import time
from room import Room
from player import Player
from item import Item

##### Items #####
item = {
    'torch': Item('torch', "a light to be carried in the hand, consisting of some combustible substance."),
    'flower': Item('flower', "Looks like a Sunflower"),
    'stick': Item('stick', "Made of wood"),
    'rope': Item('rope', "Long and strong"),
    'plank': Item('mushrooms', "fleshy, spore-bearing fruiting body of a fungus."),
    'coin': Item('coin', "Has no markings but it's gold."),
    'sword': Item('knife', "Can be used to cut")
}

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

print("#######################")
print("# Welcome to MUD Game #")
print("    -----Rules-----    ")
print("   Make it out Alive!  ")
print("#######################")


# while True:

#     print("\n{}\n".format(player.current_room.name))

#     for text in textwrap.wrap(player.current_room.description):
#         print(text)
#     print()

#     path = input(
#         "Choose your path (N)North, (S)South, (E)East, (W)West, or (Q)Quit\n").lower()

#     if path == "q":
#         print("Better luck next time")
#         break
#     else:
#         if path == "n" and hasattr(player.current_room, "n_to"):
#             player.current_room = player.current_room.n_to
#         elif path == "s" and hasattr(player.current_room, "s_to"):
#             player.current_room = player.current_room.s_to
#         elif path == "e" and hasattr(player.current_room, "e_to"):
#             player.current_room = player.current_room.e_to
#         elif path == "w" and hasattr(player.current_room, "w_to"):
#             player.current_room = player.current_room.w_to
#         else:
#             print("\n === You cant go this way ===\n")
#             time.sleep(1.5)
