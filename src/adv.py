import re
import os
import time
# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        'utils': ['rope', 'another', 'bridge'],
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        'utils': ['util_1'],
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": ("A steep cliff appears before you, falling\n"
                        "into the darkness. Ahead to the north, a light flickers in\n"
                        "the distance, but there is no way across the chasm."),
        'utils': [],
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.",
        'utils': [],
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": ("You've found the long-lost treasure\n"
                        "chamber. Sadly, it has already been completely emptied by\n"
                        "earlier adventurers. The only exit is to the south."),
        'utils': ['rope'],
        "s_to": "narrow",
    },

    "room": {
        "name": "",
        "description": "",
        'utils': [],
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
    },

}
""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        'utils': [],
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
    },
"""

utils = {
    'rope': {
        'toUseWith': ('steep'),
    },
}
''' Utils template
    'util': {
            'toUseWith': [],
    },
'''

# Write a class to hold player information, e.g. what room they are in currently


class Player:
    def __init__(self, name, startingLocation):
        self.location = startingLocation
        self.name = name
        self.bag = ['sleepingBag']
        self.holds = 'bottle'

    def takeUtil(self, index):
        # Room's utils is an List
        newUtil = rooms[self.location]['utils'][int(index)]
        print('Picked up Util: ', newUtil)
        # put it into the bag
        self.bag.append(newUtil)
        print('Player`s bag: ', self.bag)
        # remove from the room
        rooms[self.location]['utils'].remove(newUtil)
        print('Room`s utils: ', rooms[self.location]['utils'])
        time.sleep(5)


#
# Main
#


# Make a new player object that is currently in the 'outside' room.
gertrudiz = Player('gertrudiz', 'outside')

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

gameStates = {
    'correctInput': True,
    'allowedDirections': [],
    'lastDirecton': 'input',
}


def printWrongInput():
    '''Prints a messages warning that the imput is not valid'''

    # Clear the termianl window - It works on Windows (cls) an Unix (clear)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'
          '\n'
          '''ADVENTURE TO THE TREASURE.'''
          '\n'
          f'''{'-'*20}'''
          '\n'
          '\n'
          '''Bad direction,\nPlease, pick one of these: n=north, s=south, w=west, e=east'''
          )

    time.sleep(5)


def printMessage():
    '''Prints game state and details'''
    os.system('cls' if os.name == 'nt' else 'clear')
    print(('\n'
           '\n'
           'ADVENTURE TO THE TREASURE.'
           '\n'
           f'''{'-'*30}'''
           '\n'
           '\n'
           f'''Current location: {rooms[gertrudiz.location]['name']}...'''
           '\n'
           '\n'
           f'''{rooms[gertrudiz.location]['description']}'''
           '\n'
           '\n'
           'Utils in this room: '
           ))
    for i, util in enumerate(rooms[gertrudiz.location]['utils']):
        print('\t*', util, '*\tTo pick this type: ', i)
    print('\n'
          '\n'
          'Utils in your room: '
          )
    for i, util in enumerate(gertrudiz.bag):
        print(f'''\t{i + 1}''', '\t*', util, '*')


validInput = {
}


def processInput(input):
    '''Handle user input'''
    if input == 'q' or input == 'Q':
        gertrudiz.location = None

    if ['n', 's', 'e', 'w'].__contains__(input) and rooms[gertrudiz.location].__contains__(input + '_to'):
        gameStates['correctInput'] = True
        gertrudiz.location = rooms[gertrudiz.location][input + '_to']
    elif input == '0':
        gertrudiz.takeUtil(input)
    else:
        gameStates['correctInput'] = False


def game():
    '''Launch a new game'''
    printMessage()

    while gertrudiz.location:
        newLocation = input(
            '\nWhere to go? (n = north, s = south, w = west, e = east): ')

        processInput(newLocation)

        if not gameStates['correctInput']:
            printWrongInput()

        printMessage()


game()
