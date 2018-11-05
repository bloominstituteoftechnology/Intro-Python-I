from room import Room
from player import Player

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

print("Game directions: to play enter n for north, e for east, s for south, and w for west or q to quite")

player = Player('outside')
current_room = room['outside']
res = '--start of game--'

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

while not res == 'q':

  #while player is outside
  if player.room == 'outside':
    print(current_room)
    res = input('what direction will you go \n')
    if res == 'n':
      current_room = current_room.room_direction(res)
      player = Player('foyer')
    elif not res == 'q':
      print('\nincorrect input')
  
  #while player is at foyer
  if player.room == 'foyer':
    print(current_room)
    res = input('what direction will you go?\n')
    if res == 's':
      current_room = current_room.room_direction(res)
      player = Player('outside')
    elif res == 'n':
      current_room = current_room.room_direction(res)
      player = Player('overlook')
    elif res == 'e':
      current_room = current_room.room_direction(res)
      player = Player('narrow')
    elif not res == 'q':
      print('\nincorrect input')

  #while player is at overlook
  if player.room == 'overlook':
    print(current_room)
    res = input('what direction will you go?\n')
    if res == 's':
      current_room = current_room.room_direction(res)
      player = Player('foyer')
    elif not res == 'q':
      print('\nincorrect input')
  
  #while player is at narrow
  if player.room == 'narrow':
    print(current_room)
    res = input('what direction will you go?\n')
    if res == 'w':
      current_room = current_room.room_direction(res)
      player = Player('foyer')
    elif res == 'n':
      current_room = current_room.room_direction(res)
      player = Player('treasure')
    elif not res == 'q':
      print('\nincorrect input')

  #while player is at treasure
  if player.room == 'treasure':
    print(current_room)
    res = input('what direction will you go?\n')
    if res == 's':
      current_room = current_room.room_direction(res)
      player = Player('narrow')
    elif not res == 'q':
      print('\nincorrect input')

print('\nthank you for playing my game')