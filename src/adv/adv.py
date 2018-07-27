from os import system

import sys
import textwrap

from being import player
from item import item
from room import room


## Main

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

# Establish global variables for displaying information after console refresh
action = None
description = None

while(True):
  system('clear')

  print(f'\n{player.room.name}:\n{textwrap.fill(player.room.description, 50)}\n')

  if action:
    print(action + '\n')
    action = None
  
  if description:
    print(description + '\n')


  player_input = input('> ').split()
  
  # One word inputs (ex: look, north, e, inventory, help, quit)

  if len(player_input) == 1:
    command = player_input[0]

    if command in ['help', 'options', 'h', 'o']:
      print('''\nYour command options are as follows:\n
'room' - gives the name and basic decriptions of your location\n
'look' or 'inspect' - allows you to examine the room that you are
  currently in\n
'move [direction]' or 'go [direction]' - input direction(north, east, ect..)
  or first letter of direction to move\n
'inventory' or 'bag' - check\'s what you have on your person\n
'quit or q' - ends the game\n''')

    elif command in ['look', 'inspect']:
      player.room.inspected = True
      action = 'You look around the ' + player.room.name
      description = f'{textwrap.fill(player.room.look_description, 50)}\n{player.room.list_items()}'

    elif command in ['inventory', 'bag', 'i', 'b']:
      print(player.inventory)
      action = 'You take inventory of your bag'
      description = 'It contains the following:'

      for item in self.inventory:
        print('\n{}:\n{}\n'.format(item.name,
        textwrap.fill(item.description, 50)))

    elif command in ['quit', 'q']:
      print('\nOk see ya later! Hope you had fun :)\n')
      break

    else:
      print('\nInvalid single command input\n')

  # Two word inputs (ex: move north, use torch)

  elif len(player_input) == 2:
    verb = player_input[0]
    noun = player_input[1]

    if verb in ['move', 'go']:
      player.move(noun)
      action = 'You move to the ' + player.room.name

    elif verb in ['take', 'grab']:
      player.take(noun)
      action = 'You take to the ' + noun
      description  = item[noun].description

    elif verb in ['drop']:
      player.drop(noun)
      action = 'You drop to the ' + noun
      description  = item[noun].description

    else:
      print('\nInvalid two command input.\n')
