from room import Room
from player import Player

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

suppressRoomPrint = False

def printErrorString(errorString):
    print(f'\x1b[1;31;40m\n{errorString}\x1b[0m\n')
    global suppressRoomPrint
    suppressRoomPrint = True

player = Player(input('\nWhat is your name?: ') , room['outside'])

validDirection = ['n', 's', 'e', 'w']

print (f'Welcome, {player.name}!\n')

# ***** v2

def moveCommand(player, direction):
# def moveCommand(player, *args):
    newRoom = player.location.getRoomInDirection(inputList[0])
    if newRoom == None:
        printErrorString('You cannot move in that direction')
        # print("You cannot move in that direction")
    else:
        player.change_location(newRoom)

def lookCommand(playe, *args):
    if not(args[0] =='l' or args[0] == 'look'):
        printErrorString('That is not a look command')
    elif len(args) == 1:
        pass
    elif args[1] in validDirection:
        lookRoom = player.location.getRoomInDirection(args[1])
        if lookRoom is not None:
            print (lookRoom)
        else:
            printErrorString('There is nothing in that direction.')
        suppressRoomPrint = True

commands ={}
commands["n"] = moveCommand
commands["s"] = moveCommand
commands["e"] = moveCommand
commands["l"] = lookCommand

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print (player.location )
    inputList = input('>>> ').split(' ')
    if inputList[0] == "q":
        break
    elif inputList[0] in commands:
        suppressRoomPrint = commands[inputList[0]](player, *inputList)       
    else:
        printErrorString('I do not undestand that command')

# ************ v1
# while True:
#     if suppressRoomPrint:
#         suppressRoomPrint = False
#     else:
#         print (player.location )
#         # print (f"\n  {player.location.title}\n    {player.location.description}\n" )
#     # inp = input(">>> What is your command: ")
#     inputList = input('>>> ').split(' ')
#     # print(f'Your command has {len(inputList)} arguments')
#     # for arg in inputList:
#     #     print(arg)
#     if inputList[0] == "q":
#         break
#     if inputList[0] == "n" or inputList[0] == "s" or inputList[0] == "w" or inputList[0] == "e":
#         newRoom = player.location.getRoomInDirection(inputList[0])
#         if newRoom == None:
#             printErrorString('You cannot move in that direction')
#             # print("You cannot move in that direction")
#         else:
#             player.change_location(newRoom)
#     elif inputList[0] == 'look':
#         if len(inputList) == 1:
#             # print ('Do look')
#             # suppressRoomPrint = True
#             pass
#         elif inputList[1] in validDirection:
#             lookRoom = player.location.getRoomInDirection(inputList[1])
#             if lookRoom is not None:
#                 print (lookRoom)
#             else:
#                 printErrorString('There is nothing in that direction.')
#             suppressRoomPrint = True
#     else:
#         printErrorString('I do not undestand that command')