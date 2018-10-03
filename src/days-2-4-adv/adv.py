from room import Room
from player import Player
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

player = Player(room.get("outside", 'outside'), ["flashlight", "first-aid kit", "rock"])
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

while True:
    player.printRoom(player.room)
    cmd = input("-What do you want to do? You can: move 'n', move 'e', move 's', move 'w', press 'q' to quit \n-Pess 'i' to view item \n -> " )
    if cmd == "q":
        break
    elif cmd == "n":
        if hasattr(player.room, 'n_to'):
            player.room(player.room.n_to)
        else:
            print ("There is no room that way")
    elif cmd == "e":
        if hasattr(player.room, 'e_to'):
            player.room(player.room.e_to)
        else:
            print ("There is no room that way")
    elif cmd == "s":
        if hasattr(player.room, 's_to'):
            player.room(player.room.s_to)
        else:
            print ("There is no room that way")
    elif cmd == "w":
        if hasattr(player.room, 'w_to'):
            player.room(player.room.w_to)
        else:
            print ("There is no room that way")
    elif cmd == "i":
        player.printItems(player.items)
    else:
        print("Invalid choice")
        cmd
