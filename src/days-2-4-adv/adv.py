from setup import room, commandsHelp
from character import Player

# Make a new player object that is currently in the 'outside' room.
global player
player = Player(room['outside'])

gameRunning = True
def quitGame():
        print('Quitting Game')
        global gameRunning
        gameRunning = False

####################
# Command functions
###################

def parseInput(*args):
    args = args[0]
    command1 = args[0].lower()
    if command1 in "nesw": move(player, command1)
    elif command1 in {"look", "l"}: look(player, args)
    elif command1 in {"score", "s"}: player.getScore()
    elif command1 in {"pickup", "p"}: player.pickupItem(args)
    elif command1 in {"drop", "d"}: player.dropItem(args)
    elif command1 in {"q", "quit"}: quitGame()
    elif command1 in {"h", "help"}: help()

def move(character, direction):
    newRoom = character.location.peekDirection(direction)
    if newRoom == None:
        print("You cannot move in that direction")
    else:
        player.location = newRoom

def look(character, *args):
    commands = args[0]
    if len(commands) == 1:
        print("You look around the room and see:")
        character.location.roomContents()
    else:
        nextRoom = character.location.peekDirection(commands[1])
        if nextRoom is not None:
            nextRoom.roomInfo()

def checkLights(player):
    if player.location.isLit or player.hasLight():
        player.location.roomInfo()
    else:
        print("Its pitch black!")

def help():
    print("--------------------")
    print("Commands:")
    for command, description in commandsHelp.items():
        print(f"   {command}  :  {description}")
    print("--------------------")
#Start game
# name = input("What is your name?")
while gameRunning:
    print('')
    checkLights(player)
    inputList = input(">>> ").split(" ")
    parseInput(inputList)
