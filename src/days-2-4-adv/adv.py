from room import Room
from player import Player
from items import Item
from items import Treasure
from items import LightSource
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

items = {
    'dagger': Item("dagger", "a small dull blade. It's practically useless"),
}

treasure = {
    'potion': Treasure("healing potion", "Can restore HP and MP", 1000),
    'book': Treasure("book", "The Necronomicon", 50),
    'ribbon': Treasure("ribbon", "give immunity to all status effects", 200)
}



room['outside'].addItem(items['dagger'])
room['treasure'].addItem(treasure['potion'])
room['overlook'].addItem(treasure['book'])
room['foyer'].addItem(treasure['ribbon'])

suppressRoomPrint = False
validDirections = ["n", "s", "e", "w"]


def moveCommand(player, *args):
    newRoom = player.location.getRoomInDirection(args[0])
    if newRoom == None:
        printErrorString("You shall not pass!")
    else:
        player.change_location(newRoom)
    return False


def lookCommand(player, *args):
    """
    Returns suppressRoomString value
    """
    if not (args[0] == "l" or args[0] == "look"):
        printErrorString("That is not a look command")
    elif len(args) == 1:
        return False
    elif args[1] == "here":
        print('\n' + player.location.description +
              "\n\nYou see the following items: " + player.location.listOfItems() + '\n')
    elif args[1] in validDirections:
        lookRoom = player.location.getRoomInDirection(args[1])
        if lookRoom is not None:
            print('\n' + lookRoom.description + '\n')
        else:
            printErrorString("You cannot go that way.")
        return True


def takeItemCommand(player, *args):
    itemToGet = player.location.findItemByName(args[1])
    if not (args[0] == "g" or args[0] == "get"):
        printErrorString("That is not a get command")
    elif len(args) == 1:
        return False
    elif itemToGet is not None:
        player.addItem(itemToGet)
        player.location.removeItem(itemToGet)
        print(f'\n{player.name} has retrieved {itemToGet}.\n')
        player.getInventoryString()
    else:
        printErrorString(f'There is no {args[1]} to take\n')


def dropItemCommand(player, *args):
    itemToDrop = player.findItemByName(args[1])
    print(itemToDrop)
    if not (args[0] == "d" or args[0] == "drop"):
        printErrorString("That is not a drop command")
    elif len(args) == 1:
        return False
    elif itemToDrop is not None:
        player.removeItem(itemToDrop)
        player.location.addItem(itemToDrop)
        print(f'\n{player.name} has dropped {itemToDrop}.\n')
    else:
        printErrorString(f'\nThere is no {args[1]} to drop.\n')


def inventoryCommand(player, *args):
    print(f'\nYou currently have these items in your inventory:\n' +
          player.getInventoryString() + '\n')

def scoreCommand(player, *args):
    print(f'\nYour current score is {player.score}.\n')


def printErrorString(errorString):
    print(f'{errorString}')
    global suppressRoomPrint
    suppressRoomPrint = True


commands = {}
commands["n"] = moveCommand
commands["s"] = moveCommand
commands["e"] = moveCommand
commands["w"] = moveCommand
commands["l"] = lookCommand
commands["look"] = lookCommand

commands["get"] = takeItemCommand
commands["drop"] = dropItemCommand
commands["i"] = inventoryCommand
commands["inventory"] = inventoryCommand
commands["score"] = scoreCommand

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


player = Player(input("\nWhat is your name?: "), room['outside'], [])

print(f"Welcome, {player.name}!\n")

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print(f'Current location: {player.location.title}\n')
    inputList = input("> ").split(" ")
    if inputList[0] == "q":
        break
    elif inputList[0] in commands:
        suppressRoomPrint = commands[inputList[0]](player, *inputList)

    else:
        printErrorString("That command does not exist")
