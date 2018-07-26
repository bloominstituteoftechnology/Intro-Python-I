from room import Room
from player import Player
from item import Item

import textwrap

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        Item("mirror", "Seems to have fallen from it's frame."),
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east.""",
        [],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness.Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
        [],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
        ["key"],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
        [],
    ),
}

# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p1 = Player("Player One", room["outside"])

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
done = False

while not done:
    room_name = p1.current_room.name
    wrapped_desc = textwrap.fill(p1.current_room.description)
    visible_item = p1.current_room.items

    print("\n{}".format(room_name))
    print("{}".format(wrapped_desc))
    print("You find a {}".format(visible_item))

    user_input = input("> ")

    if user_input in ["n", "e", "s", "w"]:
        dirAttr = user_input + "_to"

        if hasattr(p1.current_room, dirAttr):
            p1.current_room = getattr(p1.current_room, dirAttr)
        else:
            print("Can't go that way.")

    elif user_input == "q":
        print("GG")
        done = True

    elif user_input == "help":
        helper = "\nCOMMANDS:\nn - north\ne - east\ns - south\nw - west\nq - quit"
        print(helper)

    else:
        print("\n - Enter a valid command or type help - ")
