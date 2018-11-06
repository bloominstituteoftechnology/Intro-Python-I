from room import Room

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
# TODO: instantiate a player with this type of calling convention and write the player class to allow for this
# player = player(room['outside'])

# Write a loop that:
while True:

    # * Prints the current room name
    print_current_room_name()
    # * Prints the current description (the textwrap module might be useful here).
    print_current_description()
    # * Waits for user input and decides what to do.
    command = input("Some filler question prompt text : fill this in later")
    # If the user enters "q", quit the game.
    if command == "q":
        print("QUIT PLACEHOLDER")
        break
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif command.upper() == "NORTH":
        print("NORTH MOVE PLACEHOLDER")
    elif command.upper() == "SOUTH":
        print("SOUTH MOVE PLACEHOLDER")
    elif command.upper() == "EAST":
        print("EAST MOVE PLACEHOLDER")
    elif command.upper() == "WEST":
        print("WEST MOVE PLACEHOLDER")
    # Print an error message if the movement isn't allowed.
    #
    else:
        print("\nUnknown command!\n")
