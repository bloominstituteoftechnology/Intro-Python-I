from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource


room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mounth beckons", [Item('sword', 'looks sharp'), LightSource("lamp", 'good source of light'), Treasure('gold', 'looks like a small bag of gold', 50)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('key', 'looks important'), Item('rope', 'looks sturdy'), Treasure('beans', 'they appear to be magical beans', 20)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('note', 'Sorry I took your gold, but this is a solid IOU which is pretty much as good as gold. Definatly planning to pay the money back. - Sinceraly a lying thief'), Treasure('knife', 'jewel incrusted knife. Probably accidently dropped by the thief', 30)]),
}


player = Player('marshall')
current_room = room['outside']

res = '--start of game--'
location = 'outside'

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#see if items in room
def check_area(room, player):
  if len(room.items) == 0:
    print("you do not notice any items in the room")
  if len(room.items) == 1:
    print(f'\nin the area you notice a {room.items[0]}\n')
  if len(room.items) > 1:
    print('\nin the area you see:\n')
    for i in room.items:
      print(i)
#end of check_area function

#for getting and dropping items in room
def command(player_input, player, current_room):

  #=print(player.score)
  # for get item and drop item
  if len(player_input) == 2:

    #look for item and add it to inventory
    #remove item from room
    count1 = 0
    if player_input[0] == "get":
      for i in current_room.items:
        if player_input[1] == i.name:

          #check if its a treasure
          #if so only adds score to player only on first time picked up
          if i.__class__.__name__ == 'Treasure':
            if i.check_scored() == False:
              player.score += i.score_amount
    
          player.items.append(i)
          current_room.items.remove(i)
          print('player has taken ' + i.name)
          count1 += 1

      #no item inform player
      if count1 == 0:
        print('item not found')
    
    #look for item to drop
    count2 = 0
    if player_input[0] == 'drop':
      for i in player.items:
        if player_input[1] == i.name:
          current_room.items.append(i)
          player.items.remove(i)
          i.on_drop()
          count2 += 1

      if count2 == 0:
        print("you don't have item to drop")
#end of command function

def check_inventory(player):
  if len(player.items) == 0:
    print('\ninventory is currently empty')
  else:
    print('\ncurrent inventory includes:')
    for i in player.items:
      print(i.name)
#end of check_inventory

def check_for_light(room, player):
  boolv = False

  #check room for light source
  for i in room.items:
    if i.__class__.__name__ == 'LightSource':
      boolv = True

  #check player for light source
  for i in player.items:
    if i.__class__.__name__ == 'LightSource':
      boolv = True

  #return false if no light and true if there is light
  return boolv


while not res[0] == 'q':

  #while player is outside
  if location == 'outside':

    #base commands #################
    print(current_room)
    res = input('\nwhat will you do?\n').split(" ")
    command(res, player, current_room)
    #################################

    if res[0] == 'get' or res[0] == 'drop':
      pass
    elif res[0] == 'l':
      check_area(current_room, player)
    elif res[0] == 'n':
      current_room = current_room.room_direction(res[0])
      location = 'foyer'
    elif res[0] == 'i':
      check_inventory(player)
    elif not res[0] == 'q':
      print('incorrect input')
  
  #while player is at foyer
  if location == 'foyer':

    #base commands #################
    print(current_room)
    res = input('\nwhat will you do?\n').split(" ")
    command(res, player, current_room)
    #################################

    if res[0] == 'get' or res[0] == 'drop':
      pass
    elif res[0] == 'l':
      check_area(current_room, player)
    elif res[0] == 'i':
      check_inventory(player)
    elif res[0] == 's':
      current_room = current_room.room_direction(res[0])
      location = 'outside'
    elif res[0] == 'n':
      current_room = current_room.room_direction(res[0])
      location = 'overlook'
    elif res[0] == 'e':
      current_room = current_room.room_direction(res[0])
      location = 'narrow'
    elif not res[0] == 'q':
      print('incorrect input')

  #while player is at overlook
  if location == 'overlook':

    #base commands #################
    print(current_room)
    res = input('\nwhat will you do?\n').split(" ")
    command(res, player, current_room)
    #################################
 
    if res[0] == 'get' or res[0] == 'drop':
      pass
    elif res[0] == 'l':
      check_area(current_room, player)
    elif res[0] == 'i':
      check_inventory(player)
    elif res[0] == 's':
      current_room = current_room.room_direction(res[0])
      location = 'foyer'
    elif not res[0] == 'q':
      print('\nincorrect input')
  
  #while player is at narrow
  if location == 'narrow':

    #base commands #################
    if current_room.is_light == False:
      if check_for_light(current_room, player) == False:
        print('its dark in here!')
      else:
        print(current_room)

    res = input('\nwhat will you do?\n').split(" ")
    command(res, player, current_room)
    #################################

    if res[0] == 'get' or res[0] == 'drop':
      pass
    elif res[0] == 'l':
      check_area(current_room, player)
    elif res[0] == 'i':
      check_inventory(player)
    elif res[0] == 'w':
      current_room = current_room.room_direction(res[0])
      location = 'foyer'
    elif res[0] == 'n':
      current_room = current_room.room_direction(res[0])
      location = 'treasure'
    elif not res[0] == 'q':
      print('\nincorrect input')

  #while player is at treasure
  if location == 'treasure':

    #base commands #################
    print(current_room)
    res = input('\nwhat will you do?\n').split(" ")
    command(res, player, current_room)
    #################################

    if res[0] == 'get' or res[0] == 'drop':
      pass
    elif res[0] == 'l':
      check_area(current_room, player)
    elif res[0] == 'i':
      check_inventory(player)
    elif res[0] == 's':
      current_room = current_room.room_direction(res[0])
      location = 'narrow'
    elif not res[0] == 'q':
      print('\nincorrect input')

print('\nthank you for playing my game')