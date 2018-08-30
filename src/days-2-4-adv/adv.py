from room import Room
from player import Player
from item import Item, Treasure

# Declare all the rooms and items
items = {
    'sword': Item('Sword', '+10 Attack'),
    'shield': Item('Shield', '+5 Defense'),
    'armor': Item('Armor', '+3 Defense'),
    'pants': Item('Pants', '+2 Defense'),
    'dagger': Item('Dagger', '+5 Attack'),
    'bracers': Item('Bracers', '+1 Defense'),
    'potion': Item('Potion', 'Restore 5hp'),
    'bandage': Item('Bandage', 'Restore 2hp'),
    'diamond': Item('Diamond', 'can be traded for 1000 gold'),
    'revivepotion': Item('RevivePotion', 'can revive player 1 time'),
    'excalibur': Treasure('Excalibur', 'The Legendary Sword', 10),
    'aegis': Treasure('Aegis', "Lord of Olympia Zeus' shield", 10),
    'mjolnir': Treasure('Mjolnir', 'The hammer of Thor', 10)
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons""",
                     [items['sword'], items['bandage']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [items['shield'], items['pants']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [items['armor'], items['dagger']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [items['bracers'], items['potion']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [items['diamond'], items['revivepotion'], items['excalibur'], items['aegis'], items['mjolnir']]),
}
# Game variables
suppressRoomPrint = False
validDirections = ["n", "s", "e", "w"]

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#######
# Util
#######

def printErrorString(errorString):
    print(f'=== {errorString} ===')
    global suppressRoomPrint
    suppressRoomPrint = True


#
# Main
#

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#('Which direction to do you want to go to (N,S,W,E)?')
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player = Player( input("\nWhat is your name?: ") , room['outside'])
print (f"Welcome, {player.name}!\n")
while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print(f'\nCurrent location:  {player.location.name}.')
        print(player.location.description + '\n')
        print(f'Items found: {", ".join(player.location.getLoots())}\n')

    inputList = input('>>>').split()

    if inputList[0] == 'q':
        print('\nGoodbye! Please come again.\n')
        break
    elif inputList[0] == 'n':
        if player.location.getRoomInDirection('n') is None:
            print('There is no room in this direction, please choose again.')
            suppressRoomPrint=True
        else:
            player.location = player.location.getRoomInDirection('n')
    elif inputList[0] == 's':
        if player.location.getRoomInDirection('s') is None:
            print('There is no room in this direction, please choose again.')
            suppressRoomPrint=True
        else:
            player.location = player.location.getRoomInDirection('s')
    elif inputList[0] == 'e':
        if player.location.getRoomInDirection('e') is None:
            print('There is no room in this direction, please choose again.')
            suppressRoomPrint=True
        else:
            player.location = player.location.getRoomInDirection('e')
    elif inputList[0] == 'w':
        if player.location.getRoomInDirection('w') is None:
            print('There is no room in this direction, please choose again.')
            suppressRoomPrint=True
        else:
            player.location = player.location.getRoomInDirection('w')

    #Player inventory
    elif inputList[0] == 'i'  and len(inputList)==1:
        if player.getInventory() is None:
            print('You have no item in your inventory.')
        else:
            print(', '.join(player.getInventory()))
        suppressRoomPrint=True

    #Room loot list
    elif inputList[0] == 'loots' and len(inputList)==1:
        if player.location.getLoots() is None:
            print('There is no item in this room')
        else:
            print(', '.join(player.location.getLoots()))
        suppressRoomPrint=True

    #Get item
    elif inputList[0] == 'get' and inputList[1]:
        itemList = player.location.getLoots()
        if (inputList[1] not in itemList):
            print('There is no such item in this room')
        else:
            index = itemList.index(inputList[1])
            player.getItem(player.location.items[index])
            player.location.removeItem(index)
        suppressRoomPrint=True

    #Drop item
    elif inputList[0] == 'drop' and inputList[1]:
        itemList = player.getInventory()
        if (inputList[1] not in itemList):
            print('There is no such item in your inventory')
        else:
            index = itemList.index(inputList[1])
            player.location.receiveItem(player.inventory[index])
            player.dropItem(index)
        suppressRoomPrint=True
    else:
        printErrorString("I do not understand that command")


# if inputList[0] == 'look':
#     if inputList[1] and inputList[1] == 'n':
#         print('look north')
#     else:
#         print('look')