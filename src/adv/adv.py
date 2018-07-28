import sys
import platform
import textwrap
from os import system
from being import player
from item import item
from room import room

# Detect operating system
plat = platform.system()

# Establish global variables for displaying information after clear
action, info = None, None

while(True):
  # Call appropriate clear method
  if plat is 'Windows': system('cls')
  else: system('clear')

  # Print current room and description
  print(f'\n{player.room.name}:\n{textwrap.fill(player.room.description, 50)}\n')

  # Print most recent action and description then reset
  if action: print(action + '\n')
  if info: print(info + '\n')

  action, info = None, None

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
      action = 'You take inventory of your bag.'
      info = player.check_inventory()

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
