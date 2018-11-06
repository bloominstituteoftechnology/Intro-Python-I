from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Complex Entrance",
                     "North of you, the enemy building with a large iron staircase"),

    'foyer':    Room("Foyer", """The baked bean tin to the south of the random noises. Dusty
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
    "JohnWick": Item("JohnWick")
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
    
    # tell me the truth
    elif command.upper() == "TELL ME THE TRUTH":
        print("\nYOU CAN'T HANDLE THE TRUTH!\n")

    elif command.upper() == "PING WWW.GOOGLE.COM":
        print("\nPinging www.google.com [172.217.20.68] with 32 bytes of data:\n")
        for x in range(30):
            print("Reply from 172.217.20.68: bytes=32 time=34ms TTL=50\n")
        print("\nPackets: Sent = 4, Received = 4, Lost = 0 (0 loss)\n")
    # Print an error message if the movement isn't allowed.
    else:
        print("\nUnknown command!\n")
