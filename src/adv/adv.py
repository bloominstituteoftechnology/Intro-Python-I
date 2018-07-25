from room import Room
from player import Player

# Declare all the rooms

rooms = {
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

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

startingRoom = rooms['outside']
player1 = Player(startingRoom)

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

playing = True

while(playing is True):
    print(player1.room)
    direction = input("Enter a direction (n/w/e/s): ")
    if direction+"_to" == "n_to":
        # print("n_to")
        for room in rooms:
            # print(room)
            # print(rooms[room])
            if room == player1.room['n_to']:
                player1.room = rooms[room]
                break
    elif direction+"_to" == "w_to":
        # print("w_to")
        for room in rooms:
            if room == player1.room['w_to']:
                player1.room = rooms[room]
                break
    elif direction+"_to" == "s_to":
        # print("s_to")
        for room in rooms:
            if room == player1.room['s_to']:
                player1.room = rooms[room]
                break
    elif direction+"_to" == "e_to":
        # print("e_to")
        for room in rooms:
            if room == player1.room['e_to']:
                player1.room = rooms[room]
                break
    elif direction == "q":
        print("Game Ogre")
        playing = False
    else:
        print("Invalid input")
        break
