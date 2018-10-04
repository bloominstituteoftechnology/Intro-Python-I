from room import Room,room
from player import Player
import time
# Declare all the rooms

# Make a new player object that is currently in the 'outside' room.

player = Player(input("What is your name?\n-> "), room['outside'], [])
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
    print (f"You are at: {player.room.name}")
    print (player.room.description)
    cmd = input(f"\n-What do you want to do, {player.name}? You can: move 'n', move 'e', move 's', move 'w', press 'q' to quit  \n-Press 'i' to view items and 'd' to drop items and 'g' to get items  \n-> ")
    if cmd == "q":
        break
    elif cmd == "n":
        if hasattr(player.room, 'n_to'):
           player.room = player.room.n_to
        else:
            print ("There is no room that way")
    elif cmd == "e":
        if hasattr(player.room, 'e_to'):
            player.room = player.room.e_to
        else:
            print ("There is no room that way")
    elif cmd == "s":
        if hasattr(player.room, 's_to'):
           player.room = player.room.s_to
        else:
            print ("There is no room that way")
    elif cmd == "w":
        if hasattr(player.room, 'w_to'):
           player.room = player.room.w_to
        else:
            print ("There is no room that way")
    elif cmd == "i":
        player.printItems(player.items)
    elif cmd == "d":
        player.drop(player.items)
    elif cmd == "g":
        player.get(player.room.items)
    else:
        print("Invalid choice")
        cmd
