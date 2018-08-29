from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'Cargo': Room("Cargo Bay", """You are inside the cargo hold of an abandonded space station. 
    The only door is to the north."""),
    'Corridor': Room("Corridor", """Dim lights flicker in the corridor. 
    Derelict passages run north and east."""),
    'Holodeck': Room("Holodeck", """The doors to the holodeck slide open. 
    You enter, an old program seems to be playing in a loop. 
    'Get ooouuuutt' a phantom voice seems to whisper quietly in the air. 
    The only exit is to the south"""),
    'Narrow':   Room("Narrow", """The narrow passage bends here from west to north. 
    The smell of ash permeates the air."""),
    'Incinerator': Room("Incinerator", """You've found the incinerator room! 
    All that remains is ash. 
    The only exit is to the south."""),
}

# Link rooms together

room['Cargo'].n_to = room['Corridor']
room['Corridor'].s_to = room['Cargo']
room['Corridor'].n_to = room['Holodeck']
room['Corridor'].e_to = room['Narrow']
room['Holodeck'].s_to = room['Corridor']
room['Narrow'].w_to = room['Corridor']
room['Narrow'].n_to = room['Incinerator']
room['Incinerator'].s_to = room['Narrow']

# items
item = Item("screwdriver", "A screwdriver, but it does extra space stuff too")
room['Cargo'].contents.append(item)

item = Item("cat skull", "The skull of a cat")
room['Incinerator'].contents.append(item)

# Game Variables
suppressRoomPrint = False
validDirections = ['n', 's', 'e', 'w']

#
# Main
#

# Make a new player object that is currently in the 'cargo' room.
player = Player(room['Cargo'])  

# Command functions

def moveCommand(player, *args):
  newRoom = player.location.getRoomInDirection(args[0])
  if newRoom == None:
    printErrorString("You can't go that way")
    return True
  else:
    player.change_location(newRoom)
  return False

def inspectRoom(player, *args):
  if player.location.contents == []:
    print('The room is empty')
  else:
    print('The room contains:')
    for item in player.location.contents:
      print(f'{item}')
  return True

def look(player, *args):
  if not args[0] == 'l':
    printErrorString("That is not a look command")
  elif (len(args)) == 1:
    return False
  elif args[1] in validDirections:
    lookedRoom = player.location.getRoomInDirection(args[1])
    if lookedRoom is not None:
      print(lookedRoom)
    else:
      printErrorString('Nothing is in that direction')
    return True

def checkInventory(player, *args):
  if(player.inventory == []):
    printErrorString('Inventory is empty')
  else:
    for item in player.inventory:
      print(item)
    return True

def getItem(player, *args):
  print(args[1])
  if(args[1] in player.location.contents):
    room[player.location.title].contents.remove(args[1])
    player.inventory.append(args[1])
    print(f'You have acquired the {args[1]}')
  else:
    printErrorString("No such item")
    return True

# Commands
commands = {}
commands['n'] = moveCommand
commands['s'] = moveCommand
commands['e'] = moveCommand
commands['w'] = moveCommand
commands['i'] = inspectRoom
commands['l'] = look
commands['c'] = checkInventory
commands['g'] = getItem

# Commands Help
commandsHelp = {}
commandsHelp['n'] = "Move North"
commandsHelp['s'] = "Move South"
commandsHelp['e'] = "Move East"
commandsHelp['w'] = "Move West"
commandsHelp['i'] = "Inspect Room for Items"
commandsHelp['l'] = "Check current location or specify direction to look"
commandsHelp['c'] = "Check current inventory"
commandsHelp['g'] = "Get specififed item from room"

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
    suppressRoomPrint = printHelp()
  else:
    suppressRoomPrint = printErrorString('Command not registered')