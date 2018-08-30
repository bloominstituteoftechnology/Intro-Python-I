from room import Room
from player import Player

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
    if not (args[0] == "l" or args[0] == "look"):
        printErrorString("That is not a look command")
    elif len(args) == 1:
        return False
    elif args[1] in validDirections:
        lookRoom = player.location.getRoomInDirection(args[1])
        if lookRoom is not None:
            print (lookRoom)
        else:
            printErrorString("You cannot go that way.")
        return True

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

commandsHelp = {}
commandsHelp["n"] = "Move North"
commandsHelp["s"] = "Move South"
commandsHelp["e"] = "Move East"
commandsHelp["w"] = "Move West"
commandsHelp["l"] = "Look somewhere"
commandsHelp["look"] = "Look somewhere"

# Link rooms together

room['outside'].connectRooms(room['foyer'], "n")
room['foyer'].connectRooms(room['overlook'], "n")
room['foyer'].connectRooms(room['narrow'], "e")
room['narrow'].connectRooms(room['treasure'], "n")

player = Player(input("\nWhat is your name?: ") , room['outside'])

print (f"Salutations, {player.name}!\n")

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print(f'{player.location.title}')
    inputList = input(">>> ").split(" ")
    if inputList[0] == "q":
        break
    elif inputList[0] in commands:
        suppressRoomPrint = commands[inputList[0]](player, *inputList)
    elif inputList[0] == "help":
        for command in commandsHelp:
            print (f"{command} - {commandsHelp[command]}")
    else:
        printErrorString("That command does not exist")
