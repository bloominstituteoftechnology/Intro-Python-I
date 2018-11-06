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


# Link rooms together - refactored directions

room['outside'].north_to = room['foyer']
room['foyer'].south_to = room['outside']
room['foyer'].north_to = room['overlook']
room['foyer'].east_to = room['narrow']
room['overlook'].south_to = room['foyer']
room['narrow'].west_to = room['foyer']
room['narrow'].north_to = room['treasure']
room['treasure'].south_to = room['narrow']

# helper functions

# print current room details
def print_current_room_details(room_name, description):
    # * Prints the current room name
    print_current_room_name(room_name)
    # * Prints the current description (the textwrap module might be useful here).
    print_current_player_room_description(description)

def print_current_room_name(room):
    print("\nYou are in the %s." % (room.name))

def print_current_player_room_description(description):
    print("\nYou are in the %s." % (description))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# instantiate player object with a starting room
player = player(room['outside'])

# Write a loop that:
while True:
    # print the current room details
    print_current_room_details(player.room.name, player.room.description)
    # * Waits for user input and decides what to do.
    command = input("Some filler question prompt text : fill this in later")
    # If the user enters "q", quit the game.
    if command == "q":
        print("QUIT PLACEHOLDER")
        break
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif command.upper() == "NORTH":
        print("NORTH MOVE PLACEHOLDER")
        # logic for move north
        if player.room.north_to:
            player.room = player.room.north_to

    elif command.upper() == "SOUTH":
        print("SOUTH MOVE PLACEHOLDER")
        # logic for move south
        if player.room.south_to:
            player.room = player.room.south_to

    elif command.upper() == "EAST":
        print("EAST MOVE PLACEHOLDER")
        # TODO: logic to move east
        if player.room.east_to:
            player.room = player.room.east_to
            
    elif command.upper() == "WEST":
        print("WEST MOVE PLACEHOLDER")
        # TODO: logic to move west

    # Print an error message if the movement isn't allowed.
    else:
        print("\nUnknown command!\n")
