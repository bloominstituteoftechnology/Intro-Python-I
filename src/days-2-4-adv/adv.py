from room import Room
from player import Player
from item import Item

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

## declare some items [ will elaborate and subclass some of these later ]
items = {
    "L115a": Item("L115a"),
    "AK47": Item("AK47"),
    "Stiletto": Item("Stiletto"),
    "C4": Item("C4"),
    "Katana": Item("Katana"),
    "Notepad": Item("Notepad"),
    "Wick": Item("Wick")
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
def print_current_room_details(room):
    print("\n You are in the %s" % (room))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# instantiate player object with a starting room
player = Player(room['outside'])
# Write a loop that:
while True:
    # print the current room details
    print(player.room)
    # * Waits for user input and decides what to do.
    command = input("PLEASE ENTER a Command to move : [NORTH] [SOUTH] [EAST] [WEST] or [QUIT] to exit the game >> ")
    # If the user enters "q", quit the game.
    if command.upper() == "QUIT":
        break
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif command.upper() == "NORTH":
        # logic for move north
        if player.room.north_to:
            player.room = player.room.north_to

    elif command.upper() == "SOUTH":
        # logic for move south
        if player.room.south_to:
            player.room = player.room.south_to

    elif command.upper() == "EAST":
        # logic to move east
        if player.room.east_to:
            player.room = player.room.east_to

    elif command.upper() == "WEST":
        # logic to move west
        if player.room.west_to:
            player.room = player.room.west_to

    # Print an error message if the movement isn't allowed.
    else:
        print("\nUnknown command!\n")
