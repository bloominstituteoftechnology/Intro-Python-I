import sys
import platform
import textwrap
from os import system
from game import player, npc, item

# Detect operating system
plat = platform.system()

# Establish global variables for displaying information after clear
action, info = None, None

while(player.isAlive):
  # Call appropriate clear method
  if plat is 'Windows': system('cls')
  else: system('clear')

  # Print current room and description
  print(f'\n{player.room.name}:\n\n{textwrap.fill(player.room.description, 65)}\n')

  # Print most recent action and description then reset
  if action: print(action + '\n')
  if info: print(info + '\n')

  action, info = None, None

  # Take player input and split string to parse commands
  player_input = input('> ').split()
  
  # One word inputs (ex: look, north, e, inventory, help, quit)
  if len(player_input) == 1:
    command = player_input[0]

    # Display list of valid commands
    if command in ['help', 'options']:
      action = 'Your command options are:'
      info = '''One word -
  - [direction] : moves in direction
  - 'inspect', 'examine' or 'look' : inspects current room
  - 'equipped' : displays currently equipped items
  - 'help' or 'options' : displays all input option
  - 'q', 'quit' or 'end' : ends game session

Two words -
  - 'move' or 'go' [direction] : moves in direction
  - 'inspect' or 'examine' [item or being] : inspects item or being
  - 'use' [item] : uses item
  - 'equip' [item] : equips item
  - 'attack' [target_key] : attacks target
  - 'take' or 'grab' [item] : picks up item
  - 'drop' or 'leave' [item] : drops item
  - 'destroy' [item] : destroys item
  - 'quit game' or 'end game' : ends game session

[Directions] can be north, east, south, west or any of
their respective first letters.

[Items] are the name of any item that you see in game.

[Targets] are the names of any enemy you see in game.'''

    # Move to adjacent room
    elif command in ['north', 'east', 'south', 'west', 'n', 'e', 's', 'w']:
      player.move_room(command)
      action = 'You move to the ' + player.room.name

    # Inspect current room
    elif command in ['examine', 'inspect', 'look']:
      action = 'You look around the ' + player.room.name
      info = player.inspect()

    # Checks contents of inventory
    elif command in ['inventory', 'bag']:
      action = 'You take inventory of your bag.'
      info = player.check_inventory()

    # End game
    elif command in ['quit', 'q', 'end']:
      print('\nOk see ya later! Hope you had fun :)\n')
      break

    else:
      action = 'Invalid single command input'

  # Two word inputs (ex: move north, use torch)
  elif len(player_input) == 2:
    verb = player_input[0]
    noun = player_input[1]

    # Move to an adjacent room
    if verb in ['move', 'go'] and noun in ['north', 'east', 'south', 'west', 'n', 'e', 's', 'w']:
      action = player.move_room(noun)
    
    # Examine a target (being or item)
    elif verb in ['inspect', 'examine']:
      pass

    # Take item from room
    elif verb in ['take', 'grab']:
      taken = player.take(item[noun])
      
      if taken:
        action = 'You take the ' + noun
        info = item[noun].description

      else:
        info = 'Invalid item'

    # Drop item in room
    elif verb in ['drop', 'leave']:
      dropped = player.drop(item[noun])

      if dropped:
        action = 'You drop to the ' + noun
        info = item[noun].description
      
      else:
        info = 'Invalid Item'
    
    # Attack target
    elif verb in ['attack']:
      action = f'You attacked {noun}'
      info = player.attack(npc[noun])

    # End game
    elif verb in ['quite', 'end'] and noun in ['game']:
      print('\nOk see ya later! Hope you had fun :)\n')
      break

    else:
      action = 'Invalid two command input.'

  else:
    action = '''Currently only one and two word commands are valid.\n
Type 'help' or 'options' for a list of valid commands.'''

print('''Womp womp wooooooomp!!! 
You have parished. I hope that you enjoyed your time here warrior. 
Please come back when you would like another taste of adventure.''')