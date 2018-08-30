from room import Room
from player import Player
from items import *
from dialogue import Dialogue
from game_system import Game_System
from functools import partial
import os
import re
from functools import partial

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

room['outside'].connect_rooms('e', room['foyer'])
room['foyer'].connect_rooms('n',room['overlook'])
room['overlook'].connect_rooms('w',room['narrow'])
room['narrow'].connect_rooms('s',room['treasure'])
room['treasure'].connect_one_way('s',room['outside'])

# Item Creation
debris = Item('debris', 'It is just a useless item', {})
print(debris.name)
# Add items to rooms

room['outside'].add_item(debris)
# functions that only belong in this file
def print_format_string(color, message):
    colors = {
        'success': '\x1b[6;30;42m',
        'error': '\x1b[1;31;40m'
    }
    print(f'${colors[color]}{message}\x1b[0m')

def treeSearch(userInput, obj):
  if type(obj) != dict:
    obj()
    return
  
  if userInput[0] in obj:
    newObj = obj[userInput[0]]
  else:
    print_format_string('error','Invalid command')
    return
  
  newUserInput = userInput[1:]

  treeSearch(newUserInput, newObj)

# Start of game
Dialogue.intro()

# name, age, height, weight, hp, attack, defense, inventory
restart = 'r'
while restart == 'r':
    player = Player.create_player()

    restart = input(
    f"""
    Your starting character attributes:

    {player}

    Enter r to restart putting bio information

    Press enter to continue
    """)

player.set_location(room['outside'])
Dialogue.greet_player(player.name)

playerCommands = {
    'n': partial(player.go_direction, 'n'),
    's': partial(player.go_direction, 's'),
    'e': partial(player.go_direction, 'e'),
    'w': partial(player.go_direction, 'w'),
    'help': Game_System.display_help,
    'hp': player.get_hp,
    'q': quit,
    'look':{
        'for': {
            'items': player.look_for_items,
            'enemies': player.look_for_enemies
        },
    },
    'check':{
         'inventory': player.get_inventory,
    },
}


player.get_current_location()

while(True):
    
    command = input(">>> ")
    
    os.system('cls' if os.name == 'nt' else 'clear')

    pattern = re.compile(r'\s+')
    command = re.split(pattern, command)
    treeSearch(command, playerCommands)


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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
