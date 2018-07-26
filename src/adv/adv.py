import os
from time import sleep
from textwrap import wrap

from room import Room
from player import Player
from minimap.minimap import MiniMap # Importing from subdirectories
from item import Item

# Declare Global Items
items = {
    'dandelions':   Item('dandelions', 'A handful of dandelions. Can be found at the entrance of the cave.'),
    'sword':        Item('sword', 'A masterfully crafted sword, suited for a champion!'),
    'lamp':         Item('lamp', 'An old and rusty lamp, looks like it still has oil in it'),
    'amulet':       Item('amulet', 'A glowing amulet, it vibrates as you get closer to treasures'),
    'backpack':     Item('backpack', 'A very large backpack. This can come in handy!'),
    'laptop':       Item('laptop', 'A personal laptop, too bad the batteries have run out')
}

# Declare all the rooms

room = {
    #outside:   { name: "Outside Cave Entrance", description: "North of you, the cave mount beckons", n_to: {POINTS TO FOYER}}
    'outside':  Room("Outside Cave Entrance", "Dandelions grow on the outside of the cave entrance. North of you, the cave mount beckons"),
    'foyer':    Room("Foyer","Dim light filters in from the south. Dusty passages run north and east."),
    'overlook': Room("Grand Overlook","A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),
    'narrow':   Room("Narrow Passage","The narrow passage bends here from west to north. The smell of gold permeates the air."),
    'treasure': Room("Treasure Chamber","You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
    # Add your own room here
    'corridor': Room("Main Corridor", "You are located at a narrow corridor. West of you a dim light can be seen. East of you is the foyer"),
    'gallery': Room(
                    "Grand Gallery", 
                    "The passage opens up to a very large gallery with rocks hanging from above, and a piercing hole in the center where light rays seep into the darkness of the caverns. At first the room appeared as a dead end because of the blinding light hiding the shadowy corners. To the South lies the same narrow corridor. But as your eyes adjust to the darkness of the caverns you notice on the far East of the room there seems to be a shining golden light coming from a hole in the ground leading into another cavity."
                    ),
}

# Add Inventory to Rooms
room['outside'].inventory.append(items['dandelions'])
room['foyer'].inventory.append(items['lamp'])
room['gallery'].inventory.append(items['sword'])
room['treasure'].inventory.append(items['laptop'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['corridor']
room['corridor'].e_to = room['foyer']
room['corridor'].n_to = room['gallery']
room['gallery'].s_to = room['corridor']
room['gallery'].e_to = room['treasure']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.
# { name: 'Moises', location: SOME OBJECT REFERENCE }
player = Player('Moises', room['outside'])
player.inventory.append(items['backpack'])
player.inventory.append(items['amulet'])

# Define the game controlls!
player_movement = ['s', 'n', 'e', 'w', 'q']
player_inventory = ['i', 'inventory']

# Parser Key and Functions assigned
input_parser = {
    'take':     player.loot,
    'get':      player.loot,
    'loot':     player.loot,
    'drop':     player.drop,
    'discard':  player.drop,
}

def print_items():
    # Print Items in current location
    items_info = []
    for item in player.location.inventory:
        items_info.append(item.info())
    print('\nThe following items are available:')
    print('-'*50)
    print('\n'.join(items_info))

while(True):
    # Clear the console so it is more immersive    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'*50)
    command = None
    print(
        '\nYou are located at:','\n'.join(wrap(player.location.name, width=50)),
        '\nDescription:', '\n'.join(wrap(player.location.description, width=50))
        )
    print_items()
    command = input("\nIn what direction do you wish to proceed\n(N,E,W,S) or (Q: for quitting) pick one: ").lower()
    # Handle movement and quit commands inside player
    if command in player_movement:
        player.move_to(command)
    # Handle Displaying Player Inventory
    if command in player_inventory:
        player.display_inventory()
    else:
        # Figure alternative commands in here and handle them
        try:
            # turn commands into an array
            argz = command.split(' ')
            if len(argz) == 2:
                input_parser[argz[0]](argz[1])
        except:
            pass
        #     print('Command not available')
        #     input()
