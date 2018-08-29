from room import Room
from player import Player
from item import Item

# Declare all the rooms
# Which rooms are empty?? Who knows?
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
new_item = Item("flashlight", "Good light source")
room['outside'].items.append(new_item)

player = Player(room['outside'])
allowed = ['north', 'south', 'east', 'west']
"""print(player.room)
player = Player(room['outside'].n_to)
print(player.room)"""
suppressRoomPrint = False

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print("----------------Treasure Game----------------")
        print("You are at {}.".format(player.room.getDescription()))
    message = input("\nWhere do you want to go? (north/south/east/west): ")
    if message == 'quit':
        print("Game over")
        break
    if message not in allowed:
        #print("\nPlease only choose north, south, east, or west.\n")
        newMessage = message.split(" ")
        if len(newMessage) > 1:
            if (newMessage[0] == "take" or newMessage[0] == "get"):
                for item in player.room.items:
                    if item.name == newMessage[1]:
                        player.room.items.remove(item)
                        player.items.append(item)
                        print("You have picked up the {}".format(item))
                    else:
                        print("{} is not in the room.".format(newMessage[1]))
            elif (newMessage[0] == "drop"):
                for item in player.items:
                    if item == newMessage[1]:
                        player.room.items.append(item)
                        player.items.remove(item)
                        print("You have picked dropped the {} in the {}".format(
                            item, player.room.name))
                    else:
                        print("You are not holding that item. ")
            else:
                print("An error has occurred.")
        elif (newMessage[0] == "show"):
            for item in player.items:
                print("You are holding {}".format(item.name))
        else:
            print("Not a valid option, please choose another.")
    else:
        if hasattr(player.room, message[0] + '_to'):
            # print("Worked!")
            player.room = getattr(player.room, message[0] + '_to')
        elif hasattr(player.room, message[0] + '_to') == False:
            print("That doesn't lead anywhere, please choose another direction.")
            suppressRoomPrint = True


"""
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
"""
