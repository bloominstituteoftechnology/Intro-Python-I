from room import Room
from player import Player
from item import Item

import textwrap

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

room['outside'].items.append(Item("Rusty Shield", "Will probably protect you only once"))


player = Player(room['outside'])

#
# Main
#

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

wrapper = textwrap.TextWrapper(width=50)
done = False

while True:
    print(f"You're currently in {player.current_room.name}")
    print(wrapper.wrap(text=player.current_room.description))

    if len(player.current_room.items) > 0:
        for item in player.current_room.items:
            print(item.name + ": " + item.description)

    # Get user input
    user_input = input("\nCommand> ").strip().lower().split(" ", 1)

    print(user_input)

    # Check for user input
    if len(user_input) > 2 or len(user_input) < 1:
        print("I don't understand that.")
        continue

    if len(user_input) == 1:
        # Check to see if the user whated to quit
        if user_input == 'quit' or user_input[0] == 'q':
            done = True

        # check if user input matches the cardinal directions
        elif user_input[0][0] in ['n', 's', 'e', 'w']:
            player.current_room = player.try_move(user_input[0][0])

    elif len(user_input) == 2:
        if user_input[0] == "get" or user_input[0] == "take":
            item = player.find_item(user_input[1])
            if item:
                player.inventory.append(item)
                player.current_room.items.remove(item)
                print(player.inventory)
                print(player.current_room.items)
            else:
                print("No such item in this room!")













pass
