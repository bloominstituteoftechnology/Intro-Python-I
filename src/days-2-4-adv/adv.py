from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource
import textwrap
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True,
                     [Item("Rock", """Who knows how useful this could be!"""),
                     Item("Grass", """A nutritious treat should you get hungry in your travels"""),
                     Item("Key", """Who knows what doors this may open?"""),
                     LightSource("Torch", """Batteries included""")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                    passages run north and east.""", False,
                    [Item("Umbrella", """This will protect against suppressive waterpower"""),
                    Treasure("Briefcase", """An Ominous Black Briefcase with
                    gold light emanating from inside""", 666)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm.""", True,
                    [Item("Axe", """Heeeerrre's Johnny!"""),
                    Treasure("Native American Artifact",
                    """Legend says this artifact allows the possessor to
                    communicate telepathically with the ghost of Scatman Crothers""",
                    1980)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air.""", False,
                    [Item("Wet Mud", """Gross!""")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south.""", False,
                    [Item("Empty Treasure Chest",
                    "A big box that once held great treasure"),
                    Treasure("Gold Coin", """All that's left...""", 1),
                    Item("Scribbled Note", """A note containing a famous
                    director's explanation of a mysterious hotel room...""")]),
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
        light_sources = [item for item in player.inventory if isinstance(item, LightSource)]
        is_light = player.location.is_light or len(light_sources) > 0
        if is_light:
            print(player.location)
            return True
        else:
            print("It's pitch black!")
            return True


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
        light_sources = [item for item in player.inventory if isinstance(item, LightSource)]
        is_light = player.location.is_light or len(light_sources) > 0
        if is_light:
            print('\nRoom contains:')
            index = 0
            for item in player.location.items:
                print(f'\n-- ({index}) {item} --\n')
                index += 1
            return True
        else:
            print("It's pitch black!")
            return True

    elif args[1] == 'inside':
        print('\nINVENTORY: ')
        index = 0
        for item in player.inventory:
            print(f'\n-- ({index}) {item} --\n')
            index += 1
        return True

def getCommand(player, *args):
    if len(player.location.items) == 0:
        printErrorString("All you do is take! There's nothing more to get in this room")
    elif int(args[1]) >= len(player.location.items):
        printErrorString('Grasping at straws...No item with that ID!')
    elif len(player.location.items) > 0:
        player.inventory.append(player.location.items[int(args[1])])
        player.score += player.location.items[int(args[1])].on_take()
        player.location.items.pop(int(args[1]))
        return True
    else:
        printErrorString("Better GET the heck outta here! Not a valid command, boss")

def dropCommand(player, *args):
    if int(args[1]) >= len(player.inventory):
        printErrorString('No such object to drop!')
    elif len(player.inventory) > 0:
        player.location.items.append(player.inventory[int(args[1])])
        player.inventory[int(args[1])].on_drop()
        player.inventory.pop(int(args[1]))
        return True
    else:
        printErrorString('You have nothing to drop')

def  viewCommand(player, *args):
    if args[0] == 'i' or args[0] == 'inventory':
        print('\nINVENTORY: ')
        index = 0
        for item in player.inventory:
            print(f'\n-- ({index}) {item} --\n')
            index += 1
        return True
    elif args[0] == 'score':
        print('\nSCORE: ')
        print(f'Player1: {player1.score}')
        return True
    elif args[0] == 'opener':
        printGameOpener()
        return True
    elif args[0] == 'survey':
        light_sources = [item for item in player.inventory if isinstance(item, LightSource)]
        is_light = player.location.is_light or len(light_sources) > 0
        if is_light:
            print('\nRoom contains:')
            index = 0
            for item in player.location.items:
                print(f'\n-- ({index}) {item} --\n')
                index += 1
            return True
        else:
            print("It's pitch black!")
            return True

def printGameOpener():
    openingStrings = [" _______             __                                   ",
    "/       \           /  |                                  ",
    "$$$$$$$  | __    __ $$ |  ______                          ",
    "$$ |__$$ |/  |  /  |$$ | /      \                         ",
    "$$    $$/ $$ |  $$ |$$ |/$$$$$$  |                        ",
    "$$$$$$$/  $$ |  $$ |$$ |$$ |  $$ |                        ",
    "$$ |      $$ \__$$ |$$ |$$ |__$$ |                        ",
    "$$ |      $$    $$/ $$ |$$    $$/                         ",
    "$$/        $$$$$$/  $$/ $$$$$$$/                          ",
    "                        $$ |                              ",
    "                        $$ |                              ",
    "                        $$/                               ",
    "  ______   __        __            __                     ",
    " /      \ /  |      /  |          /  |                    ",
    "/$$$$$$  |$$ |____  $$/  _______  $$/  _______    ______  ",
    "$$ \__$$/ $$      \ /  |/       \ /  |/       \  /      \ ",
    "$$      \ $$$$$$$  |$$ |$$$$$$$  |$$ |$$$$$$$  |/$$$$$$  |",
    " $$$$$$  |$$ |  $$ |$$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |",
    "/  \__$$ |$$ |  $$ |$$ |$$ |  $$ |$$ |$$ |  $$ |$$ \__$$ |",
    "$$    $$/ $$ |  $$ |$$ |$$ |  $$ |$$ |$$ |  $$ |$$    $$ |",
    " $$$$$$/  $$/   $$/ $$/ $$/   $$/ $$/ $$/   $$/  $$$$$$$ |",
    "                                                /  \__$$ |",
    "                                                $$    $$/ ",
    "                                                 $$$$$$/  ",
    "\n",
    '                                               ______',
    '            _                 _ __...----~~~~~ _',
    '           //   ___...--- ~~~ \\       .      //  \|/',
    '   __..--_// ~~~        .     _\\   .         \\_     .',
    '        //\\\    \|/.        //\\\           ///\\ .',
    '       //-\-\\              //-/-\\         //-/-\\',
    '      //\_-_/\\            //\_-_/\\    .  //\_-_/\\',
    '  .    /\ @ /\              /\\_//\         /\\_//\     .',
    '      /\ \_/ /\            /\ \O/ /\       /\.\=/./\ ',
    '     /__\_\_/__\     .    /__\_\_/__\     /__\_\_/__\ ',
    '    /___________\        /___________\   /___________\  .',
    '   (   _____/:_) )      (  _______/:_)) ((_:\_______  )',
    '    \_(_:\______/        \_(_:\______/   \______/:_)_/   \|/',
    '                          (',
    '    .                      ) /( ( (  .    .',
    '             /\   .       )\ )\  /(         /\    /\ ',
    '            /=/           \(/ _\/ /(        \=\  /=/   .',
    '     .     /=/___       ()__)/ /(__()   .    \=\/=/',
    '          /=/////\\         (_)             __\=|/',
    '          \_\////_(_                       ////(_)\  .',
    "          //////   _\       .             _)_\\\\\\\ ",
    '          \///(.  _\                     /_   .)\\\\\ ',
    '   .       (:) | _\              __     __/___o/\\\\\\_    .',
    "        ___(:) ' \___ .__/\/\___/_/    /         \\\\\\\ ",
    '       /   (:)       \   \  /         /(*)(*)(*)(*\\\\\\\ ',
    '      /  _ (:)     _  \  / /          | _  _  _  _ \\\\\\',
    '     /  / \__   __/ \  \/ /           |/_\/_\/_\/_\/_\/_|',
    '     (  \ |       |__\   /   .         \_/\_/\_/\_/\_/\/  .',
    '      \  \|       |   \_/              |/_\/_\/_\/_\/_\|',
    '       \  |_______|/   \               |\_/\_/\_/\_/\_/|',
    '  .     \/         \   /         .    /              jro\   .',
    '        /           \ /              /(*)(*)(*)(*)(*)(*)(\ ',
    '        \___________//   .           \___________________/',
    '     .                       \|/ .             .            .',
    '',
    '                    "Remember: When you have reached the',
    '                    end you have only just begun."',
    '',
    '                        ASCII ART CREDIT: Jonathon R. Oglesbee',
    '\n']
    for string in openingStrings:
        print(string)
        time.sleep(.0500)


commands = {}
commands['n'] = moveCommand
commands['s'] = moveCommand
commands['e'] = moveCommand
commands['w'] = moveCommand
commands['l'] = lookCommand
commands['look'] = lookCommand
commands['get'] = getCommand
commands['take'] = getCommand
commands['i'] = viewCommand
commands['inventory'] = viewCommand
commands['score'] = viewCommand
commands['opener'] = viewCommand
commands['drop'] = dropCommand

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

player1 = Player(room['outside'], 0, [Item('Pen', 'A mighty instrument to influence minds'), Item('Sword', 'Not as mighty...')])

suppressRoomPrint = False

#Prints, current room name, description and waits for user input
while(True):
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        printGameOpener()
        print("Welcome to the game you are...")
        print(room['outside'])
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
