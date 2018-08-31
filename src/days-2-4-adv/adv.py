from room import Room
from player import Player
from items import Item
from items import Treasure
from items import LightSource
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),
}

items = {
    'sword': Item("sword", "A wooden sword. It's dangerous to go alone! Take this."),
}

treasure = {
    'necklace': Treasure("necklace", "A necklace made out of pure gold", 1000),
    'book': Treasure("book", "A dusty book with the title 'Incantions of the Nether Realm'", 50),
    'ring': Treasure("ring", "A basic iron ring", 200)
}

lamp = LightSource('lamp', "A lamp filled with oil")

room['outside'].addItem(items['sword'])
room['treasure'].addItem(treasure['necklace'])
room['overlook'].addItem(treasure['book'])
room['foyer'].addItem(treasure['ring'])
room['overlook'].addItem(lamp)
suppressRoomPrint = False
validDirections = ["n", "s", "e", "w"]


def moveCommand(player, *args):
    newRoom = player.location.getRoomInDirection(args[0])
    if newRoom == None:
        printErrorString("You cannot move in that direction!")
    else:
        player.change_location(newRoom)
    return False

def lookCommand(player, *args):
    """
    Returns suppressRoomString value
    """
    if player.location.hasLight(LightSource) or player.hasLight(LightSource) or player.location.is_light:
        if not (args[0] == "l" or args[0] == "look"):
            printErrorString("That is not a look command")
        elif len(args) == 1:
            return False
        elif args[1] == "here":
            print ('\n' + player.location.description + "\n\nThere are the following items here: " + player.location.listOfItems() + '\n')
        elif args[1] in validDirections:
            lookRoom = player.location.getRoomInDirection(args[1])
            if lookRoom is not None:
                print ('\n' + lookRoom.description + '\n')
            else:
                printErrorString("You cannot go that way.")
            return True
    else:
        print("\n It's pitch black!")

def takeItemCommand(player, *args):
    if player.location.hasLight(LightSource) or player.hasLight(LightSource) or player.location.is_light:
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
    else:
        print("\nGood luck finding that in the dark!\n")

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
    print(f'\nYou currently have these items in your inventory:\n' + player.getInventoryString() + '\n')

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

room['outside'].connectRooms(room['foyer'], "n")
room['foyer'].connectRooms(room['overlook'], "n")
room['foyer'].connectRooms(room['narrow'], "e")
room['narrow'].connectRooms(room['treasure'], "n")

player = Player(input("\nWhat is your name?: ") , room['outside'], [])

print (f"Salutations, {player.name}!\n")

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    if player.location.hasLight(LightSource) or player.hasLight(LightSource) or player.location.is_light:
        print(f'Current location: {player.location.title}\n')
    elif player.location.is_light is False:
        print("It's pitch black!")

    inputList = input("> ").split(" ")
    if inputList[0] == "q":
        break
    elif inputList[0] in commands:
        suppressRoomPrint = commands[inputList[0]](player, *inputList)

    else:
        printErrorString("That command does not exist")
