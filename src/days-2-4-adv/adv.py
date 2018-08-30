import textwrap
from room import Room
from player import Player
from item import Item
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
print(f"\nHello, {player.name}!\n")
print(f"\nOk {player.name} lets create our world")
items = input("\nWhat items would you like outside? ").split(" ") 
room['outside'].create_world(items) 
items = input("\nWhat items would you like in the foyer? ").split(" ") 
room['foyer'].create_world(items) 
items = input("\nWhat items would you like in the overlook? ").split(" ") 
room['overlook'].create_world(items) 
items = input("\nWhat items would you like in the narrow? ").split(" ") 
room['narrow'].create_world(items) 
items = input("\nWhat items would you like in the treasure room? ").split(" ") 
room['treasure'].create_world(items) 


validDirection = ["n", "s", "e", "w", ]
validActions = ["take", "drop", "inventory", "i", "score"]

while True:
    '''if suppressRoomPrint:
        suppressRoomPrint = False
    else:'''
        #print (f"\n  {player.location.title}\n    {player.location.description} \n " )
    print("\n".join(textwrap.wrap(player.location.title)))
    print("\n".join(textwrap.wrap(player.location.description)))
    print("\nI can see ", player.location.items)
    print("\nDo you want to take any items with you, only four allowed")
    inputList = input("\nWhat direction of travel or action will you take? \n").split(" ")
    #print(f"Your command has {len(inputList)} arguments)
    if inputList[0] == "q":
        break
    if (len(inputList) == 2) and inputList[0] not in validActions:
            printErrorString("Invalid command! Your options are take, drop, score, and inventory i")
    if inputList[0] == "take" and len(player.items) < 4:
        if player.location.check_item(inputList[1]) == True:
            print(inputList[1])
            player.add_item(inputList[1])
            player.location.drop_item(inputList[1])
        else:
            printErrorString("\nThat item is not available!")
    if inputList[0] == "inventory" or "i":
        print("\nYour inventory now includes", player.items)
    if inputList[0] == "score":
        print(player.name, " your score is ", player.score)
    if inputList[0] == "drop":
        player.drop_item(inputList[1])
        player.location.add_item(inputList[1])
        print(player.location.items)
        print("\nYour inventory now includes", player.items)
        print("\nYou can see", player.location.items)
    if inputList[0] in validDirection:
        newRoom = player.location.getRoomInDirection(inputList[0])
        if newRoom == None:
            printErrorString("You cannot move in that direction!")
        else:
            player.change_location(newRoom)
    if inputList[0] not in validActions and inputList[0] not in validDirection:
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
        