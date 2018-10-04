from room import Room
from player import Player
from constants import move_directions
from item import Item
# Declare all the rooms

laboratory = Room("Gnarly Laboratory", "The lab has a faint smell of iron and ammonia. Flickering light overhead half-illuminates a gnarly scene.")
office =  Room("C-Suite Office", """The executive offices, of course, are empty.  Everyone in C-Suite managed to escape.""")
incinerator = Room("Grand Incinerator", """A hot, dark room barely lit by flame peaking out of the incinerator.""")
chapel = Room("The Passage Chapel", """Idols and iconography cover every inch of the chapel.""")
pendulum = Room("The Pendulum", """You've reached the Pendulum. Conditioned air envelopes you.  The doors lock behind you.  You see the key-switch ahead and you know what you must do.""")

laboratory.setRoomMoves({"f":office})
office.setRoomMoves({"b":laboratory, "f":incinerator, "r":chapel})
chapel.setRoomMoves({"l":office, "f":pendulum})
incinerator.setRoomMoves({"f":office})
pendulum.setRoomMoves({"b":chapel})

# Link rooms together

# room['laboratory'].f_to = room['office']
# room['office'].b_to = room['laboratory']
# room['office'].f_to = room['incinerator']
# room['office'].r_to = room['chapel']
# room['incinerator'].b_to = room['office']
# room['chapel'].l_to = room['office']
# room['chapel'].f_to = room['pendulum']
# room['pendulum'].b_to = room['chapel']

#
# Main
#

def detectCMD(room,cmd):
	if cmd == 'f' or 'b' or 'l' or 'r':
		if cmd == room.f_to:
			return f
		elif cmd == b:
			return b_to
		elif cmd == l:
			return l_to
		elif cmd == r:
			return r_to
	else:
		print(f'{cmd} is not an optional command.')


def Main():


  laboratory = Room("Gnarly Laboratory", "The lab has a faint smell of iron and ammonia. Flickering light overhead half-illuminates a gnarly scene.")
  office =  Room("C-Suite Office", """The executive offices, of course, are empty.  Everyone in C-Suite managed to escape.""")
  incinerator = Room("Grand Incinerator", """A hot, dark room barely lit by flame peaking out of the incinerator.""")
  chapel = Room("The Passage Chapel", """Idols and iconography cover every inch of the chapel.""")
  pendulum = Room("The Pendulum", """You've reached the Pendulum. Conditioned air envelopes you.  The doors lock behind you.  You see the key-switch ahead and you know what you must do.""")

  badCrystal = Item('Bad Crystal', 'A small glass capsule containing an experimental, protein-like macromolecule.', 'You place the Bad Crystal in your mouth and chomp down...')
  lumniscience = Item('Lumniscience', 'A suspension containing what the scientists said "frees users from the 3rd dimension". This will allow you to see ahead 2 moves.', 'You pop the vile open and gulp the suspension down, here comes the rabbit hole.')

  laboratory.setRoomMoves({"f":office})
  office.setRoomMoves({"b":laboratory, "f":incinerator, "r":chapel})
  chapel.setRoomMoves({"l":office, "f":pendulum})
  incinerator.setRoomMoves({"f":office})
  pendulum.setRoomMoves({"b":chapel})

  office.setRoomItem(lumniscience)
  chapel.setRoomItem(badCrystal)
  print(chapel.getRoomItem().getItemType())

  unicorn = Player(input('What is your name, punk...   '), laboratory)

  currRoom = unicorn.getCurrentRoom()

  print(f"Ok, {unicorn.sayName()}, you're in the {currRoom.getRoomType()}.  We need to get to the Pendulum quick!")
  print("\n\nSo, let's make a move:")

  gameLoop(unicorn, currRoom)

def gameLoop(plyr,curr):
  currRoom = curr
  while True:
    cmd = input('\n\n\To make a move type a direction: "f", "b", "l", "r", OR "q" to bite down on that tooth.: \n\n')
    print(cmd)
    if cmd == "q":
      break
    possMoves = currRoom.getRoomMoves()
  
    nextRoom = currRoom.checkIfRoomMove(cmd)
    if(nextRoom == False):
      print(f"You cannot move in the direction.")
    currRoom = nextRoom
    plyr.setCurrentRoom(nextRoom)
    roomName = currRoom.getRoomType()
    roomDesc = currRoom.getRoomDescription()
    print(f"Looks like we are in the {roomName}")
    print(f"{roomDesc}")

Main()