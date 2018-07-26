from room import Room
from player import Player
from item import Item,Treasure, LightSource


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
chamber!"""),
}


# Link rooms together
room['outside'].items.append(LightSource('lantern','gives light'))
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].items.append(Treasure('chest','a treasure chest',100))
room['treasure'].items.append(Treasure('ring','a magical ring',500))
room['treasure'].items.append(Treasure('diamond','a diamond',1000))
room['foyer'].is_light = True

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal userInput, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

userInput = ""
while userInput != "q":
  print("\n")
  if(player.has_light() or player.current.is_lit()):
    print(player.current.description)
    if(len(player.current.items) == 0):
      print('this room has no items')
    else:
      for i in player.current.items:
        print('\n ' + i.name + ': ' + i.description)
  else:
    print("It's pitch black")
  print("\n")
  userInput = input("Direction? (q to quit) ").split(' ')
  print("\n")

  if(len(userInput) == 1):
    userInput = userInput[0]
    if userInput == "north":
      if player.current.n_to != None:
        player.current = player.current.n_to
      else:
        print("Invalid Move")
    elif userInput == "east":
      if player.current.e_to != None:
        player.current = player.current.e_to
      else:
        print("Invalid Move")
    elif userInput == "south":
      if player.current.s_to != None:
        player.current = player.current.s_to
      else:
        print("Invalid Move")
    elif userInput == "west":
      if player.current.w_to != None:
        player.current = player.current.w_to
      else:
        print("Invalid Move")
    elif userInput == 'i' or userInput == 'inventory':
      if(len(player.items) == 0):
        print("you currently have no items")
      else:
        for i in player.items:
          print('\n ' + i.name + ': ' + i.description)
    elif userInput != 'q':
      print("Invalid Command")
  else:
    if userInput[0] == 'get' or userInput[0] == 'take':
      found = False
      for i in player.current.items:
        if(i.name == userInput[1]):
          player.current.items.remove(i)
          player.items.append(i)
          i.on_take()
          found = True
      if not found:
        print('that item is not here')
    elif userInput[0] == 'drop':
      found = False
      for i in player.items:
        if(i.name == userInput[1]):
          player.items.remove(i)
          player.current.items.append(i)
          i.on_drop()
          found = True
      if not found:
        print('you do not have that item')
    else:
      print("Invalid Command")
