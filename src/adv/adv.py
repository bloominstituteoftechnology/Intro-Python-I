from room import Room
from player import Player
from item import Item, Treasure
import textwrap
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
item = Item('sword', 'silver sword')
item2 = Item('cat', 'fuzzy cat')
item3 = Item('dog', 'big dog')
item4 = Item('knife', 'sharp knife')
item5 = Item('nerf gun', 'blue nerf gun')
player = Player('Tylar', room['outside'])
room['outside'].addItem(item)
room['foyer'].addItem(item2)
room['overlook'].addItem(item3)
room['narrow'].addItem(item4)
room['treasure'].addItem(item5)
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
def direction(command, curRoom):
    dirAttr = command + "_to"
    if hasattr(curRoom, dirAttr):
        player.room = getattr(curRoom, dirAttr)
    else:
        print("You can't go that way.")
    return curRoom

done = False
inputCommand = []

def directionCommand():
    global done, player
    dirCommands = ['n', 's', 'w', 'e']
    if inputCommand[0] == 'q' or inputCommand[0] == 'quit' or inputCommand[0] == 'exit':
        done = True
    elif inputCommand[0] in dirCommands:
        player.curRoom = direction(inputCommand[0], player.room)
    elif inputCommand[0] in ['i', 'inv', 'inventory']:
        player.printInventory()
    elif inputCommand[0] == 'score':
        player.printScore()
    else:
        print('Unknown command {}'.format(inputCommand))


def verbCommand():
    verbCommands = ['get', 'take', 'pickup']
    if inputCommand[0] in verbCommands:
        player.pickupItem(inputCommand[1])
    elif inputCommand[0] in ['drop']:
        player.dropItem(inputCommand[1])
    else:
        print('Unkown command {}'.format(inputCommand))


def startGame():
    curRoom = player.room

    prettyDesc = textwrap.fill(curRoom.description)

    print(f'\n{curRoom.name}\n{prettyDesc}')

    if len(player.room.items) > 0:
        print('\nYou see:')
        for i in player.room.items:
            print('  ' + str(i.name))


while not done:
    startGame()
    inputCommand = input("Command> ").strip().lower().split()

    if len(inputCommand) > 2 or len(inputCommand) < 1:
        print('Cannot use command')
    
    if len(inputCommand) == 1:
        directionCommand()

    if len(inputCommand) == 2:
        verbCommand()
    
