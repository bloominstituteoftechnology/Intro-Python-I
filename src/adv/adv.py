from room import Room
from player import Player
from item import Item
from treasure import Treasure
import printing
import commandparser as parser

# Declare the items
items = {
    'jewel': Treasure(100, "jewel",
        ["glittering"],
        "It is a deep red hue and seems to pulse to an unheard rhythm."),
    'locket': Item("locket", 
        ["battered", "silver"],
        "Opening it reveals a faded photograph of two lovers."),
    'dagger': Item("dagger",
        ["thin"],
        "It looks like it could be used to stab somebody.")
}

# Declare the rooms
rooms = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", True),
    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", True, [items['dagger']]),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", True, [items['locket']]),
    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.", False),
    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! The only exit is to the south.", False, [items['jewel']]),
}

# Link rooms together
rooms['outside'].connections['n'] = rooms['foyer']
rooms['foyer'].connections['s'] = rooms['outside']
rooms['foyer'].connections['n'] = rooms['overlook']
rooms['foyer'].connections['e'] = rooms['narrow']
rooms['overlook'].connections['s'] = rooms['foyer']
rooms['narrow'].connections['w'] = rooms['foyer']
rooms['narrow'].connections['n'] = rooms['treasure']
rooms['treasure'].connections['s'] = rooms['narrow']

#
# Main loop
#

# Make a new player object that is currently in the 'outside' room.
name = input("Welcome to the Dungeon of Diogenes! Who are you? ")
player = Player(name, rooms['outside'])
while True:
    printing.turn(player)
    command = input("\nEnter choice (or help): ")
    parser.process_command(command, player)