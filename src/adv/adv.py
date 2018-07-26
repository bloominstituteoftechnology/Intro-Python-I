from room import Room
from player import Player
from item import Item
from os import system
import textwrap

# Create all the items

item = {
  'lever': Item('lever', """It looks as though it was broken off at the base.
Maybe it goes to something."""),
}

# tools = Item('tools', "These could be used to fashion some thing handy")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty 
passages run north and east.""", """You see a wall to the west that seems to 
have very uniform gaps in the shape of a doorway. Upon further inspection there
appears to be a gab in the wall with a slot inside. It must be a mehcanism of some sort"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", """As you inspect the area, you see a strange
metal object near the edge of the cliff.
It appears to be a lever.""",[item['lever']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'workshop': Room("Smith's Workshop", """This hidden room has scraps strewn out
across the floor and containers along portions of the walls.""", """Around the corner seems
to be a functional workbench. Maybe we could use this to craft something useful"""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Devon', room['overlook'])

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

turn = 0
action = None
description = None

while(True):
  system('clear')
  turn += 1

  # print('\n{}:\n{}\n'.format(player.room.name,
  #   textwrap.fill(player.room.description, 50)))

  print('\n{}:\n{}\n'.format(player.room.name,
    textwrap.fill(player.room.description, 50)))

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
