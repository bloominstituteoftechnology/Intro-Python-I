from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource


room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mounth beckons.", [Item('sword', 'looks sharp'), LightSource("lamp", 'good source of light'), Treasure('goldbag', 'looks like a small bag of gold', 50)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('key', 'looks important'), Item('rope', 'looks sturdy'), Treasure('beans', 'they appear to be magical beans', 20)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], False),

    'bridge':   Room("Long Bridge", """A long bridge above a bottomless pit of darkness stands before you. A Troll blocks your path across.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
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
room['narrow'].n_to = room['bridge']
room['bridge'].s_to = room['narrow']
room['bridge'].n_to = room['treasure']
room['treasure'].s_to = room['bridge']


#see if items in room
def check_area(room, player):
  if len(room.items) == 0:
    print(room)
  if len(room.items) == 1:
    print(f'{room} Also you notice a {room.items[0]}\n')
  if len(room.items) > 1:
    string = ''
    for i in room.items:
      string += i.name + ' '
    print(f"\n{room} Also you notice {len(room.items)} items nearby: {string.rstrip('/')}")
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
          print('\nTaken')
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

#task one
#I will add another room that has a troll in it
#the troll will need to be attacked with the sword
#will need to do the command attack troll

#first made the new room
#the new room will be a bridge to the treasure room
#it will be after the narrow passage


#have I been there yet?
been_outside = False
been_foyer = False
been_overlook = False
been_bridge = False
been_narrow = False
been_treasure = False

# my loop conditionals
outside_loop = True
foyer_loop = True
overlook_loop = True
narrow_loop = True
bridge_loop = True
treasure_loop = True

######################--------------######################
###################### START OF GAME #####################
######################--------------######################

while not res[0] == 'q':

  #while player is outside
  if location == 'outside':

    #for printing room info
    #only execute when I enter the room
    if been_outside == False:
      print(current_room)
    else:
      print('\n' + current_room.name)
    been_outside = True


    #### need loop here #
    while outside_loop == True:
      res = input('\n').split(" ")
      command(res, player, current_room)

      if res[0] == 'get' or res[0] == 'drop':
        pass
      elif res[0] == 'l':
        check_area(current_room, player)
      elif res[0] == 'n':
        current_room = current_room.room_direction(res[0])
        location = 'foyer'
        outside_loop = False
        foyer_loop = True
      elif res[0] == 'i':
        check_inventory(player)
      elif res[0] == 'q':
        outside_loop = False
      elif not res[0] == 'q':
        print('incorrect input')

  
  #while player is at foyer
  if location == 'foyer':

    #for printing room info
    #only execute when I enter the room
    if been_foyer == False:
      print(current_room)
    else:
      print('\n' + current_room.name)
    been_foyer = True

    while foyer_loop == True:
      res = input('\n').split(" ")
      command(res, player, current_room)

      if res[0] == 'get' or res[0] == 'drop':
        pass
      elif res[0] == 'l':
        check_area(current_room, player)
      elif res[0] == 'i':
        check_inventory(player)
      elif res[0] == 's':
        current_room = current_room.room_direction(res[0])
        location = 'outside'
        outside_loop = True
        foyer_loop = False
      elif res[0] == 'n':
        current_room = current_room.room_direction(res[0])
        location = 'overlook'
        overlook_loop = True
        foyer_loop = False
      elif res[0] == 'e':
        current_room = current_room.room_direction(res[0])
        location = 'narrow'
        narrow_loop = True
        foyer_loop = False
      elif res[0] == 'q':
        foyer_loop = False
      elif not res[0] == 'q':
        print('incorrect input')

  #while player is at overlook
  if location == 'overlook':

    #for printing room info
    #only execute when I enter the room
    if been_overlook == False:
      print(current_room)
    else:
      print('\n' + current_room.name)
    been_overlook = True
 
    while overlook_loop == True:
      res = input('\n').split(" ")
      command(res, player, current_room)

      if res[0] == 'get' or res[0] == 'drop':
        pass
      elif res[0] == 'l':
        check_area(current_room, player)
      elif res[0] == 'i':
        check_inventory(player)
      elif res[0] == 's':
        current_room = current_room.room_direction(res[0])
        location = 'foyer'
        overlook_loop = False
        foyer_loop = True
      elif res[0] == 'q':
        overlook_loop = False
      elif not res[0] == 'q':
        print('\nincorrect input\n')
  
  #while player is at narrow
  if location == 'narrow':

    #dark rooom!!! #################
    if current_room.is_light == False:
      if check_for_light(current_room, player) == False:
        print('\nits dark in here!')
      else:
        if been_narrow == False:
          print(current_room)
        else:
          print('\n' + current_room.name)
        been_narrow = True

    while narrow_loop == True:
      res = input('\n').split(" ")
      command(res, player, current_room)
      if res[0] == 'get' or res[0] == 'drop':
        pass
      elif res[0] == 'l':
        if check_for_light(current_room, player) == False:
          print("\nAll you see is darkness. Sure would be great to have a light source.")
        else:
          check_area(current_room, player)
      elif res[0] == 'i':
        if check_for_light(current_room, player) == False:
          print("\ntoo dark to check your inventory")
        else:
          check_inventory(player)
      elif res[0] == 'w':
        current_room = current_room.room_direction(res[0])
        location = 'foyer'
        narrow_loop = False
        foyer_loop = True
      elif res[0] == 'n':
        if check_for_light(current_room, player) == False:
          print("\nYour too scared to venture further into the darkness")
        else:
          current_room = current_room.room_direction(res[0])
          location = 'bridge'
          bridge_loop = True
          narrow_loop = False
      elif res[0] == 'q':
        narrow_loop = False
      elif not res[0] == 'q':
        print('\nincorrect input\n')

  #while player is at bridge
  if location == 'bridge':

    if been_bridge == False:
      print(current_room)
    else:
      print('\n' + current_room.name)
    been_bridge = True

    while bridge_loop == True:
      res = input('\n').split(" ")
      command(res, player, current_room)
      if res[0] == 'get' or res[0] == 'drop':
        pass
      elif res[0] == 'l':
        check_area(current_room, player)
      elif res[0] == 'i':
        check_inventory(player)
      elif res[0] == 'n':
        current_room = current_room.room_direction(res[0])
        bridge_loop = False
        treasure_loop = True
        location = 'treasure'
      elif res[0] == 's':
        current_room = current_room.room_direction(res[0])
        bridge_loop = False
        narrow_loop = True
        location = 'narrow'
      elif res[0] == 'q':
        bridge_loop = False
      elif not res[0] == 'q':
        print('\nincorrect input\n')


  #while player is at treasure
  if location == 'treasure':

    #for printing room info
    #only execute when I enter the room
    if been_treasure == False:
      print(current_room)
    else:
      print('\n' + current_room.name)
    been_treasure = True

    while treasure_loop == True:
      res = input('\n').split(" ")
      command(res, player, current_room)
      if res[0] == 'get' or res[0] == 'drop':
        pass
      elif res[0] == 'l':
        check_area(current_room, player)
      elif res[0] == 'i':
        check_inventory(player)
      elif res[0] == 's':
        current_room = current_room.room_direction(res[0])
        location = 'bridge'
        treasure_loop = False
        bridge_loop = True
      elif res[0] == 'q':
        treasure_loop = False
      elif not res[0] == 'q':
        print('\nincorrect input\n')

print('\nthank you for playing my game.')
print(f'your ending player score was {player.score}')