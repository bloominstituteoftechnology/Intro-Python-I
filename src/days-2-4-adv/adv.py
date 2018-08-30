from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [], True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['coin', 'hat'], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['coin', 'coin', 'lamp'], True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['coin', 'shovel'], True),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""", ['coin', 'coin', 'treasure'], False),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Treasures are worht 10 pts. The only exit is to the south.""", ['coin', 'coin', 'treasure'], False),
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

# Error and Win functions
def printErrorString(errorString):
    print(f'\x1b[1;31;40m{errorString}\x1b[0m')
def printWinString(winString):
    print(f'\033[92m{winString}\033[0m')

# Valid items to pick up and drop
scoreItems = ['coin', 'treasure']
userItems = ['hat', 'shovel', 'lamp']

# User creates their player
p1 = Player((input('What is your name? ')), room['outside'], [])
# 
# Welcome message and instructions
print(f'\nWelcome {p1.name} to the text adventure game!\nTo win you need a score over 10 pts')
print('\nFollow prompts on screen.\n  ~Enter \'q\' to quit\n  ~Enter \'inventory\' to view inventory\n  ~Enter \'score\' to view score\n  ~Enter \'grab/drop <item>\' to grab/drop items\n')
# Loops starts
while True:
    # Prints the current room name, description, and items if is_light
    print('\n ====================================================================================')
    if p1.location.is_light or 'lamp' in p1.inventory:
        print(f'\033[95m\n{p1.location.name}\033[0m\n{p1.location.description}')
        print(f'\033[1m\nRoom contains: {p1.location.itemList}\033[0m') if len(p1.location.itemList) > 0 else None
    else: print('\nIt\'s pitch black! A light source is needed.')
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
        # Error if only 'grab'
        if len(inputList) == 1:
            printErrorString('\nSpecify an item to grab')
        # If item is a userItem
        elif (inputList[1] in userItems):
            if inputList[1] in p1.location.itemList:
                p1.inventory.append(inputList[1])
                print(f'\nGrabbed: {inputList[1]}')
                p1.location.itemList.remove(inputList[1])
            else:
                printErrorString('\nThat item doesn\'t exist here')
        # If item is a scoreItem
        elif (inputList[1] in scoreItems):
            if inputList[1] in p1.location.itemList:
                if inputList[1] == 'coin':
                    p1.score += 1
                    print(f'Grabbed: {inputList[1]}')
                    p1.location.itemList.remove(inputList[1])
                elif inputList[1] == 'treasure':
                    p1.score += 10
                    p1.inventory.append(inputList[1])
                    print(f'Grabbed: {inputList[1]}')
                    p1.location.itemList.remove(inputList[1])
            else:
                printErrorString('\nThat item doesn\'t exist here')
        else:
            printErrorString('\nInvalid entry, try again')
    # Response 'drop' + item
    elif inputList[0] == 'drop':
        if len(inputList) == 1:
            printErrorString('\nSpecify an item to dop')
        elif (inputList[1] in userItems):
            if inputList[1] in p1.inventory:
                if (inputList[1] == 'lamp'):
                    printErrorString('\nIts not wise to drop your light source.')
                p1.location.itemList.append(inputList[1])
                print(f'Dropped: {inputList[1]}')
                p1.inventory.remove(inputList[1])
            else:
                printErrorString('\nThat item doesn\'t exist in your inventory')
        else:
            printErrorString('\nInvalid entry, try again')
    # Response 'inventory'
    elif inputList[0] == 'inventory':
        print(f'\nInventory: {p1.inventory}')
    # Response 'score'
    elif inputList[0] == 'score':
        print(f'\nScore: {p1.score}')
    # Catch all error
    else:
        printErrorString('\nInvalid entry, try again')
    # Checks if player has 'treasure' in inventory
    if p1.score > 10:
        printWinString(f'\n{p1.name} you have won the game!')
        printWinString(f'\nYour final score was {p1.score}!\n')
        break
