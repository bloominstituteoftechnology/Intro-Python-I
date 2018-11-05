from room import Room
from player import Player

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
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mounth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

print(" ")
print("Game directions: to play enter n for north, e for east, s for south, and w for west or q to quite")

player = Player('outside')
res = '--start of game--'

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.

while not res == 'q':
  print(" ")

  #while at outside
  if player.room == 'outside':
    print(room['outside'])
    res = input('what direction will you go?  ')
    if res == 'n':
      print(" ")
      player = Player('foyer')
    if player.room == 'outside' and res not in ['e', 's', 'w', 'q']:
      print('only option is n')

  #while at foyer
  if player.room == 'foyer':
    print(room['foyer'])
    res = input('what direction will you go?  ')
    if res == 's':
      player = Player('outside')
    if res == 'n':
      player = Player('overlook')
      print(" ")
    if res == 'e':
      player = Player('narrow')
      print(" ")
    if player.room == 'foyer' and res not in ['w', 'q']:
      print('current options are n, e, and s')
  
  #while at overlook
  if player.room == 'overlook':
    print(room['overlook'])
    res = input('what direction will you go?  ')
    if res == 's':
      player = Player('foyer')
    if player.room == 'overlook' and res not in ['n', 'e', 'w', 'q']:
      print('only option is s')

  #while at narrow
  if player.room == 'narrow':
    print(room['narrow'])
    res = input('what direction will you go?'  )
    if res == 'w':
      player = Player('foyer')
    if res == 'n':
      player = Player('treasure')
      print(" ")
    if player.room == 'narrow' and res not in ['e', 's', 'q']:
      print('current options are n and w')
  
  #while at treasure
  if player.room == 'treasure':
    print(room['treasure'])
    res = input('what direction will you go?  ')
    if res == 's':
      player = Player('narrow')
    if player.room == 'treasure' and res not in ['n', 'e', 'w', 'q']:
      print('only option is s')

print(" ")
print("thank you for playering my game")