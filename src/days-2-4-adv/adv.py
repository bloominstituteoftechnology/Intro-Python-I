from room import Room
from player import Player
from item import Item

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
    'incinerator': Room("Incinerator room", """You've found the incinerator room! 
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

item = Item("cat skull", "The skull of a cat")
room['incinerator'].contents.append(item)

# Game Variables
suppressRoomPrint = False
validDirections = ['n', 's', 'e', 'w']

#
# Main
#

# Make a new player object that is currently in the 'cargo' room.
player = Player(room['cargo'])

# Util

def printErrorString(error):
  print(f'\x1b[1;31;40m\n{error}\x1b[0m\n')

# Command functions

def moveCommand(player, *args):
  newRoom = player.location.getRoomInDirection(args[0])
  if newRoom == None:
    printErrorString("You can't go that way")
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

# Commands
commands = {}
commands['n'] = moveCommand
commands['s'] = moveCommand
commands['e'] = moveCommand
commands['w'] = moveCommand
commands['i'] = inspectRoom
commands['l'] = look

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
  if suppressRoomPrint:
      suppressRoomPrint = False
  else:
    print (f"\n  {player.location.title}\n    {player.location.description}\n" )
  inp = input(">>> ").split(" ")
  if inp[0] == "q":
      break
  elif inp[0] in commands:
    supressRoomPrint = commands[inp[0]](player, *inp)
  else:
    printErrorString('Command not registered')