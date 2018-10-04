from room import Room
from player import Player
from constants import move_directions
# Declare all the rooms

laboratory = Room("Gnarly Laboratory", "The lab has a faint smell of iron and ammonia. Flickering light overhead half-illuminates a gnarly scene.", {"f":office})
office =  Room("C-Suite Office", """The executive offices, of course, are empty.  Everyone in C-Suite managed to escape.""", {"b":laboratory, "f":laboratory, "r":chapel})
incinerator = Room("Grand Incinerator", """A hot, dark room barely lit by flame peaking out of the incinerator.""", {"b":office})
chapel = Room("The Passage Chapel", """Idols and iconography cover every inch of the chapel.""", {"l":office, "f":pendulum})
pendulum = Room("The Pendulum", """You've reached the Pendulum. Conditioned air envelopes you.  The doors lock behind you.  You see the key-switch ahead and you know what you must do.""", {"b":chapel})

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

# Make a new player object that is currently in the 'laboratory' room.

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

uD = Player(input('What is your name, punk...   '), laboratory)


class Main():
  def __init__(self):

  

  def gameLoop():
  unicornDown = Player(input('What is your name, punk...   '), laboratory)
  print(f"Ok, {unicornDown.sayName()}, you're in the {unicornDown.getCurrentRoom()}.  We need to get to the Pendulum quick!")
  print("\n\nSo, let's make a move:")
  while True:
    cmd = input('\n\n\To make a move type a direction: "f", "b", "l", or "r": \n')
    # move = detectCMD(cmd)
    print(move)







# if cmd == 'r':
#     print(f'\n\n\nLooks like you are in thw {uD.getCurrentRoom()} room\n\n')
#     print(room[uD.getCurrentRoom()].room_descr)
# elif cmd == 'u':
#     print(f'\nYou dont look like an "{uD.sayName()}"\n\n\n')
# elif cmd == 'q':
#     print(f'\n\n\nLater, {uD.sayName()}!\n\n\n')
#     break
# else:
#     print('\n\n\nDont type anything by u, r, or q.\n\n\n')


