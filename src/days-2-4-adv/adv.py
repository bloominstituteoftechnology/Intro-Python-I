from room import Room
from player import Player
import os
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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

"""where add stuff to the rooms"""
# add an apple to the outside room
room['outside'].take('apple')

# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('DaBoss', 'outside')

enemy = Player('', 'narrow')

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
os.system('clear')
while True:
    print("{}".format(room[player.location].description))
    inp = input("\nEnter a command: ")
    if inp == 'q' or inp == 'quit':
        break
    elif inp =='n' or inp == "north":
        try:
            if (room[player.location].n_to):
                player.location = room[player.location].n_to
        except:
            print("Can't continue north\n")
    elif inp =='s' or inp == "south":
        try:
            if (room[player.location].s_to):
                player.location = room[player.location].s_to
        except:
            print("Can't continue south\n")
    elif inp =='e' or inp == "east":
        try:
            if (room[player.location].e_to):
                player.location = room[player.location].e_to
        except:
            print("Can't continue east\n")
    elif inp =='w' or inp == "west":
        try:
            if (room[player.location].w_to):
                player.location = room[player.location].w_to
        except:
            print("Can't continue west\n")
    elif inp =='exits':
        exits = 'You can exit: '
        try:
            if (room[player.location].n_to):
                exits += "n, "
        except:
            pass
        try:
            if (room[player.location].e_to):
                exits += "e, "
        except:
            pass
        try:
            if (room[player.location].w_to):
                exits += "w, "
        except:
            pass
        try:
            if (room[player.location].s_to):
                exits += "s, "
        except:
            pass
        # print the exits, minus the ", "
        print("{}\n".format(exits[:-2]))
    # PLAYER ACTIONS
    elif inp == "l" or inp == 'look':
        print("\n{}".format(room[player.location].name))
        if (room[player.location].inventory):
            print("Items in the room:")
        for key in room[player.location].inventory:
            if room[player.location].inventory[key]:
                print("\t{} {}".format(room[player.location].inventory[key], key))
                print()
            else:
                print("\tNothing to take here.\n")
    elif inp.startswith('take') or inp.startswith('get'):
        try:
            item = inp.split(' ')[1]
            # check to see if the item is in the room
            if (room[player.location].drop(item)):
                print('Taking {}\n'.format(item))
                # item is in the room, so player can take it
                player.take(item)
        except:
            print("You must enter something to take.")
    elif inp.startswith('drop'):
        try:
            item = inp.split(' ')[1]
            # check to see if the item is in player inventory
            if (player.drop(item)):
                print('Dropping {}\n'.format(item))
                room[player.location].take(item)
        except:
            print("You must enter something to drop.")
    elif inp == 'i' or inp == "inventory":
        inv = player.getInventory()
        if (inv.keys()):
            print("your stuff:")
            for key in inv:
                print("\t{} {}".format(inv[key], key))
            print()
        else:
            print("You aren't carrying anything\n")
    elif inp == "h" or inp == "help":
        print("\nCommands: n)orth, e)ast, w)est, s)outh, l)ook, take, get, drop, exits, i)nventory, q)uit, h)elp\n")
    else:
        print("I don't know that command")