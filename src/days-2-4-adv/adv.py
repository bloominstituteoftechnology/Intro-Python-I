import textwrap

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

# Link rooms together

room['outside'].connect(room['foyer'], "n")
room['foyer'].connect(room['overlook'], "n")
room['foyer'].connect(room['narrow'], "e")
room['narrow'].connect(room['treasure'], "n")

i1 = Item("Rock", "This is a rock")
room['outside'].addItem(i1)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# Prints the current room name
# Checks if player has joined
# Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ["n", "s", "e", "w"]

player = Player(input("\nWhat is your name? "), room['outside'])

print("\nHello, %s!" % player.name)

error = ""

while True:
    print(player.curRoom)
    if error != "":
        print (error)
        error = ""
    inp = input(" >")
    inputs = inp.split()
    numArgs = len(inputs)
    if numArgs == 1:
        if inp in directions:
            player.mRooms(inp)
        elif inp == "q":
            print ("You have left the room!")
            break
        else:
            error = "Command not found..."
    else:
        if inputs[0] == "look":
            print (player.curRoom.lookItem(inputs[1]))
