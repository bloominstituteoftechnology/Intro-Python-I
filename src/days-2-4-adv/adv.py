from room import Room
from player import Player
from item import Item
from item import Commodity

# Declare all the rooms

room = {
    'cargo': Room("Cargo Bay", """You are inside the cargo hold of an abandonded space station. 
    The only door is to the north."""),
    'corridor': Room("Corridor", """Dim lights flicker in the corridor. 
    Derelict passages run north and east."""),
    'holodeck': Room("Holodeck", """The doors to the holodeck slide open. 
    You enter, an old program seems to be playing in a loop. 
    'Get ooouuuutt' a phantom voice seems to whisper quietly in the air. 
    The only exit is to the south"""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. 
    The smell of ash permeates the air."""),
    'incinerator': Room("Incinerator", """You've found the incinerator room! 
    All that remains is ash. 
    The only exit is to the south."""),
}

# Link rooms together

room['cargo'].n_to = room['corridor']
room['corridor'].s_to = room['cargo']
room['corridor'].n_to = room['holodeck']
room['corridor'].e_to = room['narrow']
room['holodeck'].s_to = room['corridor']
room['narrow'].w_to = room['corridor']
room['narrow'].n_to = room['incinerator']
room['incinerator'].s_to = room['narrow']

# items

item = Item("screwdriver", "A screwdriver, but it does extra space stuff too")
room['cargo'].contents.append(item)

item = Item("shield", "A small, broken shield")
room['cargo'].contents.append(item)

item = Item("cat skull", "The skull of a cat")
room['incinerator'].contents.append(item)

item = Commodity("platinum", "raw platinum ore", 500)
room['cargo'].contents.append(item)

item = Commodity("mithril", "raw mithril ore", 700)
room['incinerator'].contents.append(item)

item = Commodity("fluxerator", "an ancient alien machine part of unknown origin, cannot be reproduced", 1200)
room['holodeck'].contents.append(item)

# Game Variables
suppressRoomPrint = False
validDirections = ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']

#
# Main
#

# Make a new player object that is currently in the 'cargo' room.
player = Player(room['cargo'])  

# Command functions

def moveCommand(player, *args):
  newRoom = player.location.getRoomInDirection(args[0])
  if newRoom == None:
    printErrorString("You can't go that way")
    return True
  else:
    player.change_location(newRoom)
  return False

def look(player, *args):
  if (len(args)) == 1:
    print (f"\n  {player.location.title}\n    {player.location.description}\n" )
    if player.location.contents == []:
      print('The room is empty')
    else:
      print('The room contains:')
      for item in player.location.contents:
        print(f'{item}')
    return True
  currentInput = 1
  while currentInput < len(args):
    if args[currentInput] in validDirections:
      lookedRoom = player.location.getRoomInDirection(args[currentInput])
      if lookedRoom is not None:
        print(lookedRoom)
      else:
        printErrorString('There is nothing in that direction')
    else:
      itemToLookAt = player.findItemByName(args[currentInput])
      if itemToLookAt is None:
        itemToLookAt = player.location.findItemByName(args[currentInput])
      if itemToLookAt is None:
        printErrorString('No such item')
      else:
        print(itemToLookAt.getDescription())
    currentInput += 1
  return True

def checkInventory(player, *args):
  if(player.inventory == []):
    print(f'Score: {player.score}')
    printErrorString('Inventory is empty')
  else:
    print(f'Score: {player.score}')
    print('Items:')
    for item in player.inventory:
      print(item)
  return True

def getItem(player, *args):
  itemToGet = player.location.findItemByName(args[1])
  if itemToGet is not None:
    if getattr(itemToGet, 'value') > 0:
      if getattr(itemToGet, 'picked_up') == True:
        player.addItem(itemToGet)
        player.location.removeItem(itemToGet)
        print(f'You added {itemToGet} to inventory')
      elif getattr(itemToGet) == False:
        itemToGet.picked_up = True
        player.addItem(itemToGet)
        player.location.removeItem(itemToGet)
        print(f'You added {itemToGet} to inventory')
        print(f'You got {player.addToScore(item)} points!')
    elif getattr(itemToGet, 'value') == 0:
      player.addItem(itemToGet)
      player.location.removeItem(itemToGet)
      print(f'You added {itemToGet} to inventory')
  else:
    printErrorString('No such item in room')

def dropItem(player, *args):
  itemToDrop = player.findItemByName(args[1])
  if itemToDrop is not None:
    player.dropItem(itemToDrop)
    player.location.addItem(itemToDrop)
  else:
    printErrorString(f'You are not holding {args[1]}')
  return True

# Commands
commands = {}
commands['n'] = moveCommand
commands['north'] = moveCommand
commands['s'] = moveCommand
commands['south'] = moveCommand
commands['e'] = moveCommand
commands['east'] = moveCommand
commands['w'] = moveCommand
commands['west'] = moveCommand
commands['l'] = look
commands['look'] = look
commands['i'] = checkInventory
commands['inventory'] = checkInventory
commands['g'] = getItem
commands['get'] = getItem
commands['d'] = dropItem
commands['drop'] = dropItem

# Commands Help
commandsHelp = {}
commandsHelp['north'] = "Move North"
commandsHelp['south'] = "Move South"
commandsHelp['east'] = "Move East"
commandsHelp['west'] = "Move West"
commandsHelp['inventory'] = "Check inventory"
commandsHelp['look'] = "Check current location for or specify direction to look for rooms"
commandsHelp['get'] = "Get specififed item from room"
commandsHelp['drop'] = "Drop specified item from inventory"

# Util

def printErrorString(error):
  print(f'\x1b[1;31;40m\n{error}\x1b[0m\n')
  return True

def printHelp():
  for command in commandsHelp:
      print(f'{command} - {commandsHelp[command]}')
  return True

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

while True:
  if suppressRoomPrint == True:
      suppressRoomPrint = False
  else:
    print (f"\n  {player.location.title}\n    {player.location.description}\n" )
  inp = input(">>> ").split(" ")
  if inp[0] == "q":
      break
  elif inp[0] in commands:
    suppressRoomPrint = commands[inp[0]](player, *inp)
  elif inp[0] == "help":
    print('You may shorten any command to its first letter\n' )
    suppressRoomPrint = printHelp()
  else:
    suppressRoomPrint = printErrorString('Command not registered')