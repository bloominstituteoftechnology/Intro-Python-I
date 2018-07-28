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
info = None

while(True):
  system('clear')

  # Display current room and description

  print(f'\n{player.room.name}:\n{textwrap.fill(player.room.description, 50)}\n')

  # Display most recent action and description

  if action:
    print(action + '\n')
    action = None
  
  if info:
    print(info + '\n')
    info = None


  # Take player input and split string to parse commands

  player_input = input('> ').split()
  
  # One word inputs (ex: look, north, e, inventory, help, quit)

  if len(player_input) == 1:
    command = player_input[0]

    if command in ['help', 'options', 'h', 'o']:
      action = 'Your command options are:'
      info = '''  One word -
    - [direction] : moves in direction
    - 'examine' : default to examine current room in detail
    - 'equipped' : displays currently equipped items
    - 'help' or 'h' : displays all input option
    - 'quit' or 'q' : quits game session

  Two word -
    - 'move' or 'go' [direction] : moves in direction
    - 'examine' [item] : examines item if on person or in room
    - 'use' [item] : uses item if on person or in room
    - 'equip' [item] : equips item if on persom or in room
    - 'attack' [target] : attacks with equipped weapon
    - 'pickup' [item] : picks up item
    - 'drop' [item] : drops item
    - 'destroy' [item] : destroys item if able'''

    elif command in ['look', 'inspect']:
      action = 'You look around the ' + player.room.name
      info = player.room.inspect()

    elif command in ['inventory', 'bag', 'i', 'b']:
      print(player.inventory)
      action = 'You take inventory of your bag'
      info = 'It contains the following:'

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
