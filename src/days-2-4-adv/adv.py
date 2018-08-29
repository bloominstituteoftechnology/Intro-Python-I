from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['coin',]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['coin', 'coin']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['coin',]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['treasure', 'coin', 'coin']),
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

# Error function and Win Function
def printErrorString(errorString):
    print(f'\x1b[1;31;40m\n{errorString}\x1b[0m\n')
def printWinString(winString):
    print(f'\033[92m\n{winString}\033[0m\n')

validItems = ['coin', 'treasure']

# User creates their player
p1 = Player((input('What is your name? ')), room['outside'], ['flashlight'])
# 
# Welcome message and instructions
print(f'\nWelcome {p1.name} to the text adventure game!')
print('\nFollow prompts on screen.\n  ~Enter \'q\' to quit\n  ~Enter \'player\' for account info\n  ~You start with a flashlight')
# Loops starts
while True:
    # Prints the current room name, description, and items
    print('\n ====================================================================================')
    print(f'\033[95m\n{p1.location.name}\033[0m\n{p1.location.description}')
    print(f'\033[1m\nRoom contains: {p1.location.itemList}\033[0m') if len(p1.location.itemList) > 0 else None
    # User input is received below
    inputList = input('\nWhich direction (n/s/e/w): ').split(' ')
    # Response 'q'
    if inputList[0] == 'q':
        printErrorString('\nQuitting application...\n')
        break
    # Response 'n', 's', 'e', 'w'
    elif (inputList[0] in ['n', 's', 'e', 'w']):
        if hasattr(p1.location, inputList[0] + '_to'):
            p1.location = getattr(p1.location, inputList[0] + '_to')
        else:
            printErrorString('\nThis move is not allowed')
    # Response 'grab' + item
    elif inputList[0] == 'grab':
        if len(inputList) == 1:
            printErrorString('\nSpecify an item to grab')
        elif (inputList[1] in validItems):
            if inputList[1] in p1.location.itemList:
                p1.inventory.append(inputList[1])
                print(f'Grabbed: {inputList[1]}')
                p1.location.itemList.remove(inputList[1])
            else:
                printErrorString('\nThat item doesn\'t exist here')
        else:
            printErrorString('\nInvalid entry, try again')
    # Response 'player'
    elif inputList[0] == 'player':
        print(f'\nName: {p1.name} Inventory: {p1.inventory}')
    # Catch all error
    else:
        printErrorString('\nInvalid entry, try again')
    # Checks if player has 'treasure' in inventory
    if 'treasure' in p1.inventory:
        printWinString(f'\n{p1.name} you found the treasure and won the game!')
        break
