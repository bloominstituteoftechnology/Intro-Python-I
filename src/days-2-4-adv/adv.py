from room import Room
from player import Player
from item import Item
from item import Treasure
from item import Light
import textwrap

# Declare all the rooms
item = {
'twine': Item("twine", "a ball of tightly wound twine [get twine]"),
'scissors': Item("scissors", "a pair of sewing shears [get scissors]"),
'coins': Treasure("coins", "a handful of gold coins [get coins]", 20),
'meatloaf': Item("meatloaf", "a fragrant meatloaf, still warm [get meatloaf]"),
'sandals': Item("sandals", "a pair of sandals made of rope and cardboard [get sandals]"),
'lamp': Light("lamp", "an old kerosene lamp [get lamp]"),
'jewels': Treasure("jewels", "a small bag of precious jewels [get jewels]", 80),
'jewelry': Treasure("jewelry", "a box with diamond earings, necklace, and bracelet [get jewelry]", 120)
}

item_list = item.keys()

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True, [item['coins'], ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True, [item['scissors'], item['lamp']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False, [item['twine'], item['jewels']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False, [item['jewelry'], ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False, [item['meatloaf'], ]),
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

player = Player(input('What is your name? '), room['outside'], [item['sandals'], ])

# Write a loop that:
valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

print("\n{}".format(player.currentRoom))

while True:
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == 'inventory' or cmds[0] == 'i':
            player.inventory()
        elif cmds[0] == 'look':
            player.look()

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
                player.get(item[cmds[1]])
                player.inventory()
            else:
                print("That item does not exist.")

        elif cmds[0] == "drop":
            if cmds[1] in item_list:
                player.drop(item[cmds[1]])
                player.inventory()
            else:
                print("That item does not exist.")
        else:
            print("I did not understand that command.")
