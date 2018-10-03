from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms
item = {
'twine': Item("twine", "a ball of tightly wound twine."),
'scissors': Item("scissors", "a pair of sewing shears."),
'coins': Item("coins", "a handful of gold coins"),
'meatloaf': Item("meatloaf", "a fragrant meatloaf, still warm."),
'sandals': Item("sandals", "a pair of sandals made of rope and cardboard")
}

item_list = item.keys()

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['scissors']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['twine']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['coins']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['meatloaf']),
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

suppressRoomPrint = False

# Make a new player object that is currently in the 'outside' room.

player = Player(input('What is your name? '), room['outside'], item['sandals'])

# Write a loop that:
valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

print("\n Where you are: {}".format(player.currentRoom))

while True:
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == 'inventory' or cmds[0] == 'i':
            player.inventory()
        else:
            print("I did not understand that command.")
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
            else:
                print("You want me to look where??")

        elif cmds[0] == "get":
            if cmds[1] in item_list:
                player.get(cmds[1])
            else:
                print("That item does not exist.")

        elif cmds[0] == "drop":
            if cmds[1] in item_list:
                player.drop(cmds[1])
            else:
                print("That item does not exist.")
        else:
            print("I did not understand that command.")
