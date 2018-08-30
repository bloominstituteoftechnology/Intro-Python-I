from room import Room
from player import Player
from item import Treasure
# Declare all the rooms

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].is_light = False

t1 = Treasure('Gold', 'Some nice looking gold', 50)
t2 = Treasure('Silver', 'Some nice looking silver', 20)
t3 = Treasure('Staff', 'A rare looking staff', 200)
room['foyer'].items.append(t1)
room['narrow'].items.append(t2)
room['treasure'].items.append(t3)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

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

def printErrorString(errorString):
    print(f'\x1b[1;31;40m\n{errorString}\x1b[0m')
    global suppressRoomPrint
    suppressRoomPrint = True

def printPlayerItems():
    if(len(player.items) > 0):
        printErrorString('Player Items:')
        for item in player.items:
            print(f'{item.name}: {item.description}')
    else:
        printErrorString('Player Items: None')

def printRoomItems():
    if(len(player.room.items) > 0):
        print('\nRoom Items:')
        for item in player.room.items:
            print(f'{item.name}: {item.description}')
    else:
        print('\nRoom Items: None')

def printCommands():
    printErrorString("""q = Quit
n = Move North
e = Move East
s = Move South
w = Move West
r = Show current room info
i / inventory = Check player items
get (item) / take (item) = Takes item from room
drop (item) = Drops item from player inventory""")

suppressRoomPrint = None

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print('\n ==========================-----------------------==========================\n')
        if(player.room.is_light):
            print(f"{player.room.name}\n{player.room.description}")
            printRoomItems()
        else:
            print('It\'s pitch black!')

    inp = input('\nType help to get a list of commands >>> ').lower().split(' ')

    if(inp[0] == 'q'):
        print('\nThanks for playing, exiting now!')
        break
    if(len(inp) == 1):
        if(inp[0] in ['n', 'e', 's', 'w']):
            if hasattr(player.room, inp[0] + '_to'):
                player.room = getattr(player.room, inp[0] + '_to')
            else:
                printErrorString('Cannot go that way!')
        elif(inp[0] == 'r'):
            print(f'{player.room.name}\n{player.room.description}')
            printRoomItems()
        elif(inp[0] in ['i', 'inventory']):
            printPlayerItems()
        elif(inp[0] == 'help'):
            printCommands()
        elif(inp[0] == 'score'):
            printErrorString(f'Score: {player.score}')
        else:
            printErrorString('Invalid input, please try again.')
    elif(len(inp) == 2):
        if(inp[0] in ['get', 'take']):
            if(len(player.room.items) > 0):
                for item in player.room.items:
                    if item.name.lower() == inp[1]:
                        item.on_take(player)
                        player.room.items.remove(item)
                        player.items.append(item)
                        suppressRoomPrint = True
                    else:
                        printErrorString('Item not found.')
            else:
                printErrorString('There are no items in this room to take!')
        elif(inp[0] == 'drop'):
            if(len(player.items) > 0):
                for item in player.items:
                    if item.name.lower() == inp[1]:
                        item.on_drop()
                        player.items.remove(item)
                        player.room.items.append(item)
                        suppressRoomPrint = True
                    else:
                        printErrorString('Item not found.')
            else:
                printErrorString('You have no items to drop!')
        else:
            printErrorString('Invalid input, please try again.')
    else:
        printErrorString('Invalid input, please try again.')


                     
