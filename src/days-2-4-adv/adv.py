from room import Room
from player import Player
from constants import move_directions
from item import Item
from cmds import commands
# Declare all the rooms

laboratory = Room("Gnarly Laboratory",
				  "The lab has a faint smell of iron and ammonia. Flickering light overhead half-illuminates a gnarly scene.")
office = Room("C-Suite Office",
			  """The executive offices, of course, are empty.  Everyone in C-Suite managed to escape.""")
incinerator = Room("Grand Incinerator",
				   """A hot, dark room barely lit by flame peaking out of the incinerator.""")
chapel = Room("The Passage Chapel",
			  """Idols and iconography cover every inch of the chapel.""")
pendulum = Room("The Pendulum", """You've reached the Pendulum. Conditioned air envelopes you.  The doors lock behind you.  You see the key-switch ahead and you know what you must do.""")

laboratory.setRoomMoves({"f": office})
office.setRoomMoves({"b": laboratory, "f": incinerator, "r": chapel})
chapel.setRoomMoves({"l": office, "f": pendulum})
incinerator.setRoomMoves({"f": office})
pendulum.setRoomMoves({"b": chapel})

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


# def detectCMD(room, cmd):
#     if cmd == 'f' or 'b' or 'l' or 'r':
#         if cmd == room.f_to:
#             return f
#         elif cmd == b:
#             return b_to
#         elif cmd == l:
#             return l_to
#         elif cmd == r:
#             return r_to
#     else:
#         print(f'{cmd} is not an optional command.')


#
# Main: initializes items, room, and player.  Calls GameLoop function
#
def Main():
	#
	# Initializing Rooms
	#
	laboratory = Room("Gnarly Laboratory",
					  "The lab has a faint smell of iron and ammonia. Flickering light overhead half-illuminates a gnarly scene.")
	office = Room("C-Suite Office",
				  """The executive offices, of course, are empty.  Everyone in C-Suite managed to escape.""")
	incinerator = Room(
		"Grand Incinerator", """A hot, dark room barely lit by flame peaking out of the incinerator.""")
	chapel = Room("The Passage Chapel",
				  """Idols and iconography cover every inch of the chapel.""")
	pendulum = Room("The Pendulum", """You've reached the Pendulum. Conditioned air envelopes you.  The doors lock behind you.  You see the key-switch ahead and you know what you must do.""")

	#
	# Initializing Pick-Up Items
	#
	badCrystal = Item('Bad Crystal', 'A small glass capsule containing an experimental, protein-like macromolecule.',
					  'You place the Bad Crystal in your mouth and chomp down...')
	lumniscience = Item('Lumniscience', 'A suspension containing what the scientists said "frees users from the 3rd dimension". This will allow you to see ahead 2 moves.',
						'You pop the vile open and gulp the suspension down, here comes the rabbit hole.')

	# setting possible room_moves for each room
	laboratory.setRoomMoves({"f": office})
	office.setRoomMoves({"b": laboratory, "f": incinerator, "r": chapel})
	chapel.setRoomMoves({"l": office, "f": pendulum})
	incinerator.setRoomMoves({"f": office})
	pendulum.setRoomMoves({"b": chapel})

	# setting pickup-items as attributes to certain rooms
	office.setRoomItem(lumniscience)
	chapel.setRoomItem(badCrystal)
	print(chapel.getRoomItem().getItemType())

	# creating / initializing Player
	unicorn = Player(input('What is your name, punk...   '), laboratory)

	# grabbing initial room name
	currRoom = unicorn.getCurrentRoom()

	print(f"Ok, {unicorn.sayName()}, you're in the {currRoom.getRoomType()}.  We need to get to the Pendulum quick!")
	print("\n\nSo, let's make a move:")
	gameLoop(unicorn, currRoom)


#
# GameLoop:
#
def gameLoop(plyr, curr):
	currRoom = curr
	initCmdDialog = False
	cmd = None
	while True:

		if initCmdDialog == False:
			print(
				'\n\n\To make a move type a direction: "f", "b", "l", "r", OR "q" to bite down on that tooth. \n\n')
			print('Too, you can always type "cmds" to see a list of possible commands.')
			initCmdDialog = True
		else:
			cmd = input('Type your command: ')

			if cmd == "q":
				break
			elif cmd == "cmds":
				printCommands()
			elif cmd == "inventory":
				plyr.listInventory()
			elif currRoom.checkIfRoomMove(cmd) is True and currRoom is not currRoom.getNextRoom(cmd):
				currRoom = currRoom.getNextRoom(cmd)
				plyr.setCurrentRoom(currRoom)
				roomName = currRoom.getRoomType()
				roomDesc = currRoom.getRoomDescription()
				print(f"Looks like we are in the {roomName}")
				print(f"{roomDesc}")
			else:
				print('Try a different direction')

			if currRoom.getRoomItem() is not False:
				roomItem = currRoom.getRoomItem()
				print(
					f"Wait, it looks like there is a {roomItem.getItemType()} here.")
				pickupCmd = input("Would you like to pick it up? 'y' or 'n'")
				if pickupCmd == 'y':
					plyr.pickUpItem(roomItem)
					currRoom.setRoomItem(None)
					print("Current items in your inventory:")
					for item in plyr.inventory:
						print(item.getItemType())
				else:
					print("That is not a proper response.")


def printCommands():
	print("Here are your command options: \n")
	for cmd in commands:
		print(f"{cmd} : {commands.get(cmd)}\n")


Main()
