import os
import textwrap
from room import Room
from player import Player
from item import Item, Treasure, Weapon

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}

#  Link rooms together

room["outside"].n_to = room["foyer"]  # North   Up
room["foyer"].s_to = room["outside"]  # South    Down
room["foyer"].n_to = room["overlook"]  # North    Up
room["foyer"].e_to = room["narrow"]  # East    Left
room["overlook"].s_to = room["foyer"]  # South    Down
room["narrow"].w_to = room["foyer"]  # West    Right
room["narrow"].n_to = room["treasure"]  # North    Up
room["treasure"].s_to = room["narrow"]  # South    Down

# Items
gold = Treasure("gold", "coins", 100)

# Add items to rooms
room["treasure"].roomItems.append(gold)

#  


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Link', room['outside'])

# Write a loop that:
while (not True):
    # * Prints the current room name
    print("\n{}\n".format(player.curRoom.name))

    # * Prints the current description (the textwrap module might be useful here).
    for line in textwrap.wrap(player.curRoom.description):
        print(line)

    # Print any items found in the room
    if len(player.curRoom.contents) > 0:
        print("\nYou also see:\n")
        for i in player.curRoom.contents:
            print("     " + str(i))

    # * Waits for user input and decides what to do.
    move = input("\nCommand> ").strip().lower().split()

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
