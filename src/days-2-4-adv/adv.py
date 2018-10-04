from room import Room, room
from player import Player
from item import Item, item
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
    print (f"\nYou are at: {player.room.name}")
    print (player.room.description)
    cmd = input(f"""\n-What do you want to do, {player.name}? You can: move 'n', move 'e', move 's', move 'w', press 'q' to quit 
    \n-Press 'i' to view items and 'drop' to drop items and 'get' to get items \n-Type 'score' to view score\n-> """)
    if cmd == "q":
        break
    elif cmd == "n":
        if hasattr(player.room, 'n_to'):
           player.room = player.room.n_to
           player.items = player.items.n_to
        else:
            print ("There is no room that way")
    elif cmd == "e":
        if hasattr(player.room, 'e_to'):
            player.room = player.room.e_to
            player.items = player.items.e_to
        else:
            print ("There is no room that way")
    elif cmd == "s":
        if hasattr(player.room, 's_to'):
           player.room = player.room.s_to
           player.items = player.items.s_to
        else:
            print ("There is no room that way")
    elif cmd == "w":
        if hasattr(player.room, 'w_to'):
           player.room = player.room.w_to
           player.items = player.items.w_to
        else:
            print ("There is no room that way")
    elif cmd == "i":
        player.printItems(player.items)
    elif cmd == "drop":
        player.drop(player.items)
    elif cmd == "get":
        player.get(item[player.room])
    elif cmd == "score":
        print (player.score)
    else:
        print("Invalid choice")
        cmd
