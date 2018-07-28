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

    if command in ['help', 'options']:
      action = 'Your command options are:'
      info = '''  One word -
    - [direction] : moves in direction
    - 'examine' or 'inspect' or 'look' : default to examine 
        current room in detail
    - 'equipped' : displays currently equipped items
    - 'help' or 'options' : displays all input option
    - 'quit' or 'q' or 'end' : ends game session

  Two word -
    - 'move' or 'go' [direction] : moves in direction
    - 'examine' or 'inspect' [item] : examines item if on
        person or in room
    - 'use' [item] : uses item if on person or in room
    - 'equip' [item] : equips item if on persom or in room
    - 'attack' [target] : attacks with equipped weapon
    - 'pickup' [item] : picks up item
    - 'drop' [item] : drops item
    - 'destroy' [item] : destroys item if able
    - 'quit game' or 'end game' : ends game session'''

    elif command in ['north', 'east', 'south', 'west', 'n', 'e', 's', 'w']:
      player.move_room(command)
      action = 'You move to the ' + player.room.name

    elif command in ['examine', 'inspect', 'look']:
      action = 'You look around the ' + player.room.name
      info = player.room.inspect()

    elif command in ['inventory', 'bag']:
      action = 'You take inventory of your bag.'
      info = player.check_inventory()

    elif command in ['quit', 'q', 'end']:
      print('\nOk see ya later! Hope you had fun :)\n')
      break

    else:
      action = 'Invalid single command input'

  # Two word inputs (ex: move north, use torch)
  elif len(player_input) == 2:
    verb = player_input[0]
    noun = player_input[1]

    if verb in ['move', 'go'] and noun in ['north', 'east', 'south', 'west', 'n', 'e', 's', 'w']:
      action = player.move_room(noun)

    elif verb in ['take', 'grab', 'pickup']:
      taken = player.take(item[noun])
      
      if taken:
        action = 'You take the ' + noun
        info = item[noun].description

      else:
        action = 'Invalid item'

    elif verb in ['drop']:
      player.drop(noun)
      action = 'You drop to the ' + noun
      description  = item[noun].description

    elif verb in ['quite', 'end'] and noun in ['game']:
      print('\nOk see ya later! Hope you had fun :)\n')
      break

    else:
      action = 'Invalid two command input.'

  else:
    action = '''Currently only one and two word commands are valid.\n
Type 'help' or 'options' for a list of valid commands.'''
