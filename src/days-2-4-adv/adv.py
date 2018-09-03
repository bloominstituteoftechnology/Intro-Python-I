from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons.\n"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.\n"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.\n"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.\n"""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.\n"""),
}

player = {'default_character': Player('JJ', room['outside']),}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']

# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']

# room['overlook'].s_to = room['foyer']

# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

room['outside'].connectRooms(room['foyer'], 'n')
room['foyer'].connectRooms(room['overlook'], 'n')
room['foyer'].connectRooms(room['narrow'], 'e')
room['narrow'].connectRooms(room['treasure'], 'n')


def printErrorString(errorString):
  print("\n{}\n".format(errorString))
  global noPrint
  noPrint = True

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
validDirection = ['n', 's', 'e', 'w']
noPrint = False
current_room = room['outside']
user_character = player['default_character']
print("Welcome to the game!")
inp = input("Type 'JJ' to play as default character, or Type 'C' to create a character:")
if inp == 'JJ':
  user_character == player['default_character']
  print(user_character)
elif inp == 'C' or inp == 'c':
  user_character = Player(input("Please enter your characters name: "), start_room = room['outside'])
  print('Welcome, {}!'.format(user_character.name))

while True:
  if noPrint:
    noPrint = False
  else:
    print("  \n---- You are at the {} ----\n".format(current_room.name))
    print("    {}".format(current_room.description))
  inp = input("What is your input: ")
  inplist = inp.split(' ')
  print(f'Your input has {len(inplist)} arguments')
  for arg in inplist:
    print(arg)

  if inplist[0] == 'q':
    print("See ya!")
    break

  if inplist[0] in validDirection:
    current_room = user_character.location.getRoomInDirection(inplist[0])
    newRoom = user_character.location.getRoomInDirection(inplist[0])
    if newRoom == None:
      printErrorString('You cannot go that way')
    else:
      user_character.changeLocation(newRoom)
  
  elif inplist[0] == 'look':
    if len(inplist) == 1:
      print(f'\nWhere would you like to look? (please specify look and direction)\n')
      noPrint = True
    elif inplist[1] in validDirection:
      lookRoom = user_character.location.getRoomInDirection(inplist[1])
      if lookRoom == None:
        printErrorString('\nThere is nothing to see in that direction\n')
      else:
        print(f'To the {inplist[1]} you see {lookRoom.name}.\n')
        noPrint = True
  else:
    printErrorString("\nI don't understand your command\n")
    


  # elif inp == 'n' and current_room == room['outside']:
  #   current_room = room['outside'].n_to
  # elif inp == 's' and current_room == room['outside']:
  #   print("Can not go any further South.")
  # elif inp == 'e' and current_room == room['outside']:
  #   current_room = room['outside'].s_to
  # elif inp == 'me':
  #   print(player[player_name])
    

    


#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
