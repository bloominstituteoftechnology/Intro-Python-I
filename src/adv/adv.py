import os
from textwrap import wrap
from time import sleep

from player import Player
from room import Room
from item import Item
from item import Treasure

# Delcare items
items = {
    'sword':              Item('sword', 'Metal bladed weapon used to destory monsters'),
    "axe":                Item('axe', 'A weapon that is used to cut heads off'),
    'firestick':          Item('firestick', 'Created by magic and burns an enemey alive'),
    'pitchfork':          Item('pitchfork', 'Used to poke multiple holes in enemies'),
    'sickle':             Item('sickle', 'A fast medal bladed weapon in the chape of a moon that is useful when fighting multiple monsters at once'),
    'gun':                Item('gun', 'The gun carries 6 bullets but is an instant kill to enemies'),
    'chest':              Treasure('chest', 'a chest with rubys gems and coins', 100)
}

# Declare all the rooms"
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. """),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north.The smell of gold permeates the air. """),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers.The only exit is to the south. """),
    'dungeon':  Room("Dungeon Hell", """You are in the worst place in the world and
    should be careful where you step!!! """ ),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['dungeon']
room['dungeon'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to room
room['outside'].inventory.append(items['sword'])
room['foyer'].inventory.append(items['axe'])
room['narrow'].inventory.append(items['firestick'])
room['treasure'].inventory.append(items['chest'])
room['dungeon'].inventory.append(items['chest'])


# Main

# Make a new player object that is currently in the 'outside' room.
player = Player('Mark', room['treasure'])

# Game Controls
player_movement = ['s', 'n', 'e', 'w', 'q']
player_inventory = ['i', 'inventory']
player_score = ['score']

# Parse Functions
parser_commands = {
    'take': player.take,
    'drop': player.drop,
}

# Print Items
def print_items():
    items_info = []
    for item in player.location.inventory:
        items_info.append(item.info())
    print('\nThe following items are available:')
    print('-' * 50)
    print('\n'.join(items_info))

# Write a loop that:
while (True):
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
    command = None
    print(
        '\nYou are at:', '\n'.join(wrap(player.location.name, width=50)),
        '\nDescription:', '\n'.join(wrap(player.location.description, width=50))
        )
    print_items()
    command = input("\nIn what direction do you wish to go\n(N,E,W,S) or (Q: to quit) pick one: ").lower()    
    
    # Handle movement
    if command in player_movement:
        player.move_to(command)
    # See Player Score
    if command in player_score:
        os.system('cls' if os.name == 'nt' else 'clear')
        player.show_score()
    # Handle Display of Inventory 
    if command in player_inventory:
        player.display_inventory()
    else:
        try:
            # Make commands into an array
            argz = command.split(' ')
            if len(argz) == 2:
                parser_commands[argz[0]](argz[1])
        except:
            pass
    
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
