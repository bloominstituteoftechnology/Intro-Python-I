from room import Room  # importing room object
from player import Player

# Declare all the rooms

#dictionary called room
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
#
room['outside'].n_to = room['foyer'] #north_to connector pointing to foyer
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

new_player = Player("Endor", room['outside'])

# Write a loop that:

# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.

# If the user enters "q", quit the game.

done = False

while not done:
    current_room = new_player.room
    print(f'{current_room.name}\n{current_room.description}')
    
    command = input("Command> ").strip().lower()

    if command == 'q' or command == 'quit' or command == 'exit':
        done == True

    elif command in ["s", "n", "e", "w"]:
        dirAttr = command + "_to"

        if hasattr(current_room, dirAttr):
            new_player.room = getattr(current_room, dirAttr)
        else:
            print("You can't go that way\n")