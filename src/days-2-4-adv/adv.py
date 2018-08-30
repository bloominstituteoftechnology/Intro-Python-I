from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("Rock", """Who knows how useful this could be!"""),
                     Item("Grass", """A nutritious treat should you get hungry in your travels"""),
                     Item("Key", """Who knows what doors this may open?""")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                    passages run north and east.""",
                    [Item("Umbrella", """This will protect against suppressive waterpower""")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Axe",
"""Heeeerrre's Johnny!"""), Item("Native American Artifact", """Legend says this
artifact allows the possessor to communicate telepathically with the ghost of
Scatman Crothers""")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Torch", """Batteries
included"""), Item("Wet Mud", """Gross!""")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Empty Treasure Chest",
"A big box that once held great treasure"), Item("Scribbled Note", """A note
containing a famous director's explanation of a mysterious hotel room...""")]),
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

#Game Variables
validDirections = ['n', 's', 'e', 'w']

###################
# Command Functions
###################
def moveCommand(player, *args):
    newRoom = player.location.getRoomDirection(args[0])
    if newRoom == None:
        # Print an error message if the movement isn't allowed.
        printErrorString(" -Thwack! You just hit a brick wall (or fell off a cliff), choose another direction-")
        suppressRoomPrint = True
    else:
        player.change_location(newRoom)

def lookCommand(player, *args):
    if not (args[0] == 'l' or args[0] == 'look'):
        printErrorString('That is not a look command') #What is the function of this line?
    elif len(args) == 1:
        return False
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif args[1] in validDirections:
        lookRoom = player.location.getRoomDirection(args[1])
        if lookRoom is not None:
            print('Player looks and takes a gander and sees...\n{}'.format(lookRoom))
        else:
            printErrorString('Nothing to see overthere')
        return True
    elif args[1] == 'around':
        print('\nRoom contains:')
        index = 0
        for item in player.location.items:
            print('\n-- ({}) {}: {} --\n'.format(index, item.name, item.description))
            index += 1
    elif args[1] == 'inside':
        print('\nINVENTORY: ')
        index = 0
        for item in player.inventory:
            print(f'\n-- ({index}) {item.name}: {item.description} --\n')
            index += 1

def getCommand(player, *args):
    if player.location.items[int(args[1])]:
        player.inventory.append(player.location.items[int(args[1])])
        print('You have obtained {}!'.format(player.location.items[int(args[1])].name))
        player.location.items.pop(int(args[1]))
    else:
        printErrorString('Better get the heck outta here! Not a valid get command, boss')


commands = {}
commands['n'] = moveCommand
commands['s'] = moveCommand
commands['e'] = moveCommand
commands['w'] = moveCommand
commands['l'] = lookCommand
commands['look'] = lookCommand
commands['get'] = getCommand

commandsHelp = {}
commandsHelp['n'] = "Move North"
commandsHelp['w'] = "Move West"
commandsHelp['e'] = "Move East"
commandsHelp['s'] = "Move South"
commandsHelp['l'] = "Look Somewhere"
commandsHelp['look'] = "Look Somewhere"

######
# Util
######

def printErrorString(errorString):
    print(f'\x1b[1;37;41m\n{errorString}\x1b[0m\n')
    global suppressRoomPrint
    suppressRoomPrint = False

# Make a new player object that is currently in the 'outside' room.

player1 = Player(room['outside'], [Item('Pen', 'A mighty instrument to influence minds'), Item('Sword', 'Not as mighty...')])

suppressRoomPrint = False

#Prints, current room name, description and waits for user input
while(True):
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print(player1.location)
    inputList = input('>>> ').split(' ')
    # If the user enters "q", quit the game.
    if inputList[0] == 'q':
        break
    elif inputList[0] in commands:
        suppressRoomPrint = commands[inputList[0]](player1, *inputList)
    elif inputList[0] == 'help':
        for command in commandsHelp:
            print(f"{command} - {commandsHelp[command]}")
    else:
        printErrorString("I do not understand that command")
