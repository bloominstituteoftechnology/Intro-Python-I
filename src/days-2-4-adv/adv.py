import textwrap
from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["torch", "matches", "food", "water", "pen and paper"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["sword"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["stool"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["matches"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["gold"]),
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

'''room['outside'].connectRooms(room['foyer'], "n")
room['foyer'].connectRooms(room['overlook'], "n")
room['foyer'].connectRooms(room['narrow'], "e")
room['narrow'].connectRooms(room['treasure'], "n")'''

suppressRoomPrint = False

def printErrorString(errorString):
    #print("\n -You cannot travel in that direction-\n")
    print(f'\x1b[1;31;40m\n{errorString}\x1b[0m\n')
    #global suppressRoomPrint
    #suppressRoomPrint = True


#print(player)


name = input("\nWhat is your name? ")
player = Player(name, room['outside'], [])
#player = Player( input("\nWhat is your name?: ") room['outside'])
print(f"Hello, {player.name}!\n")


validDirection = ["n", "s", "e", "w"]


while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        #print (f"\n  {player.location.title}\n    {player.location.description} \n " )
        print("\n".join(textwrap.wrap(player.location.title)))
        print("\n".join(textwrap.wrap(player.location.description)))
        print("\nI can see ", player.location.items)
        print("Do you want to take any items with you, only three allowed")
        inputList = input("\nWhat direction of travel or action will you take? \n").split(" ")
    #print(f"Your command has {len(inputList)} arguments)
    if inputList[0] == "q":
        break
    elif inputList[0] == "take" and len(player.items) < 3:
        player.add_item(inputList[1])
        player.location.drop_item(inputList[1])
    elif inputList[0] == "inventory":
        print("Your inventory now includes", player.items)
    elif inputList[0] == "drop":
        player.drop_item(inputList[1])
        player.location.add_item(inputList[1])
        print(player.location.items)
        print("Your inventory now includes", player.items)
    elif inputList[0] in validDirection:
        newRoom = player.location.getRoomInDirection(inputList[0])
        if newRoom == None:
            printErrorString("You cannot move in that direction!")
        else:
            player.change_location(newRoom)
    else:
            printErrorString("I do not understand that command")
            #suppressRoomPrint = True    
    '''elif inputList[0] == "look":
        if len(inputList) == 1:
            pass
            suppressRoomPrint = True
        elif inputList[1] in validDirection:
            lookRoom = player.location.getRoomInDirection(inputList[1])
            if lookRoom is not None:
                print(lookRoom.title)
            else:
                 printErrorString("There is nothing in that direction")
            suppressRoomPrint = True'''
        