from room import Room
from player import Player
from item import Item

import textwrap
import sys

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east."""),

    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness.Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

# Add items to rooms
room["outside"].items.append(Item("mirror", "A small mirror."))

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

    # Print room name and description
    print("\n{}".format(room_name))
    print("{}".format(wrapped_desc))

    # Print items in room if any
    if len(p1.current_room.items) > 0:
        print("\nYou also find: ")
        for i in p1.current_room.items:
            print(i.description)

    # User input
    user_input = input("> ").strip().lower()
    user_input = user_input.split(" ")

    # Single word commands
    if len(user_input) == 1:

        # Directions
        if user_input[0] in ["n", "e", "s", "w"]:
            dirAttr = user_input + "_to"

            if hasattr(p1.current_room, dirAttr):
                p1.current_room = getattr(p1.current_room, dirAttr)
            else:
                print("Can't go that way.")
    
        # Inventory
        elif user_input[0] == "i":
            if len(p1.items) > 0:
                print("\nYour inventory contains: ")
                for i in p1.items:
                    print(i.description)
            else:
                print("\nYour inventory is empty.")

        # Help - show commands
        elif user_input[0] == "help":
            helper = "\nCOMMANDS:\nn - north\ne - east\ns - south\nw - west\nq - quit"
            print(helper)

        # Quit
        elif user_input[0] == "q":
            print("GG")
            done = True

        # Invalid input
        else:
            print("\n - Enter a valid command or type help - ")

    # Two word commands
    elif len(user_input) == 2:
        verb, obj = user_input

        # Pickup items
        if verb == "get":
            room_items = [item for item in p1.current_room.items if item.name == obj]
            print(obj + " was added to your inventory.")

            if len(room_items) == 0:
                print("That item doesn't seem to be here.")
            else:
                p1.items.append(room_items[0])
                p1.current_room.items.remove(room_items[0])