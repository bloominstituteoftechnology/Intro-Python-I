# Game variables
suppressRoomPrint = False
validDirections = ["n", "s", "e", "w"]



############
# Command functions
############
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
commandsHelp["e"] = "Move Eath"
commandsHelp["w"] = "Move West"
commandsHelp["l"] = "Look somewhere"
commandsHelp["look"] = "Look somewhere"


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
            printErrorString("There is nothing in that direction.")
        return True

#######
# Util
#######

def printErrorString(errorString):
    print(f'\x1b[1;31;40m\n{errorString}\x1b[0m\n')
    global suppressRoomPrint
    suppressRoomPrint = True

# Room.connect(<Room>, <direction>)



######
# Start Game loop here
######


player = Player( input("\nWhat is your name?: ") , room['outside'])

print (f"Welcome, {player.name}!\n")

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print (player.location)
    inputList = input(">>> ").split(" ")
    if inputList[0] == "q":
        break
    elif inputList[0] in commands:
        suppressRoomPrint = commands[inputList[0]](player, *inputList)
    elif inputList[0] == "help":
        for command in commandsHelp:
            print (f"{command} - {commandsHelp[command]}")
    else:
        printErrorString("I do not understand that command")