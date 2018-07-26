from item import Item
from player import Player
from room import Room
from random import randint

# Declare all the rooms

item = {
    'torch': Item('torch', "Stick with tallow soaked cloth burning on one end"),
    'flower': Item('flower', "Resembles hydrangea"),
    'stick': Item('stick', "Made of wood"),
    'rope': Item('rope', "Very rough, long enough to tie something"),
    'plank': Item('plank', "Long but thin... wouldnt support my weight"),
    'coin': Item('coin', "Doesnt look valuable, but has some mysterious etchings on it"),
    'sword': Item('sword', "Highly damaged, will probably break soon")
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. 
Dusty passages run north and east. """, [item["flower"], item["stick"], item['torch']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, 
falling into the darkness. Ahead to the north, a light flickers in the distance, 
but there is no way across the chasm.""", [item["rope"], item["plank"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by earlier adventurers. 
The only exit is to the south.""", [item["coin"], item["sword"]]),
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
currentLocation = room['outside']
character = Player(currentLocation)

def takeItem(target='default'):
    loot = currentLocation.item_found(target) #item found in room
    if loot:
        character.pick_up(loot) #character picks up found item
        print(f"\n{loot} has been picked up!")
        if character.score == len(item):
            character.win_condition = True
            print('\nYou found every item!')
    else:
        print('\nInvalid Input')  #customize error message for invalid action

def dropItem(target='default'):
    item = character.drop(target)  #character drops item
    if item:
        currentLocation.item_dropped(item)  #room gains dropped item
        print(f"\n{item} has been dropped!")
    else:
        print('\nInvalid Input')  #customize error message for invalid action

def viewItem(target='default'):
    descript = character.inspect(target)  #gets the description of the item in character's inv
    if descript:
        print(f'\n{descript}')
    else:
        print('\nInvalid Input')  #customize error message for invalid action


movements = ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west'] #list of possible movement commands

actions = {   #dict of possible action commands
    't': takeItem,
    'take': takeItem,
    'd': dropItem,
    'drop': dropItem,
    'ins': viewItem,
    'inspect': viewItem
}

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

def movement_error():  #will generate an error based on incorrect movement command
    if currentLocation == room['outside']:
        count = 0
    if currentLocation == room['foyer']:
        count = 1
    if currentLocation == room['overlook']:
        count = 2
    if currentLocation == room['narrow']:
        count = 3
    if currentLocation == room['treasure']:
        count = 4
    errors = [{
        1: 'Nope cant do that',     #errors for movement outside
        2: 'Not possible',
        3: 'Try something else',
        4: 'Why would you try that here?',
        5: 'You\'re outside, this isnt the place for that',
        6: 'How about you try entering the cave?',
        7: 'You seem to have forgotten what you\'re capable of',
        8: 'How about no'

    },
    {
        1: 'Nope cant do that',     #errors for movement in the foyer
        2: 'Not possible',
        3: 'Try something else',
        4: 'Why would you try that here?',
        5: 'This is merely the foyer, stop making mistakes here',
        6: 'How is it you dont remember where to go from here',
        7: 'Not many places you can go from here...',
        8: 'You seem to have forgotten what you\'re capable of',
        9: 'How about no'

    },
    {
        1: 'Nope cant do that',     #errors for movement at the voerlook
        2: 'Not possible',
        3: 'Try something else',
        4: 'Why would you try that here?',
        5: 'Can\'t do that here',
        6: 'You seem to have forgotten what you\'re capable of',
        7: 'How about no',
        8: 'Are you trying to jump off the cliff?'
    },
    {
        1: 'Nope cant do that',     #errors for movement in the narrow
        2: 'Not possible',
        3: 'Try something else',
        4: 'Why would you try that here?',
        5: 'Literally one 2 directions here, how did u mess that up',
        6: 'You failed on a 50/50'

    },
    {
        2: 'Not possible',
        1: 'Nope cant do that',     #errors for movement by the treasure
        4: 'Why would you try that here?',
        3: 'Try something else',
        5: 'Are you doing this because you missed out on treasure?',
        6: 'Dont go walking into walls',
        7: 'Nothing in that direction',
        8: 'You seem to have forgotten what you\'re capable of',
        9: 'How about no'

    }]
    return errors[count][randint(1, len(errors[count]))]

playing = True
print('Loading...')
print('Now Playing: \'Room Explorer.txt\'')
print('You will be starting out outside. In order to move around type in (n)orth (s)outh (e)ast or (w)est.')
print('Typing info will allow you to see what items are in the room.')
print('If you wish to pick up or drop an item, type (t)ake or (d)rop followed by item name.')
print('To keep track of your current items, typing (i)nventory will remind you what you have.')
print('Once an item is in your inventory, typing (ins)pect will read you its description')
print('When you are done exploring, type q to exit.')
while(playing):
    print(f"\n{character}")
    request = input("What would you like to do?\n\n").lower().split(' ')

    if len(request) == 1:
        if request[0] == 'q' or request[0] == 'quit':
            print('\nSee you again!')
            playing = False

        elif request[0] == 'info':
            print(f'\nItems in Room: {currentLocation.print_items()}')

        elif request[0] == 'score':
            print(f'\nCurrent Score: {character.score}')

        elif request[0] == 'i' or request[0] == 'inv' or request[0] == 'inventory':
            print(f'\nCurrent Inventory: {character.print_inv()}')

        else:
            if request[0] in movements:
                attr = request[0][0] + '_to'   #takes on the first letter of the command so n s e or w

                if hasattr(currentLocation, attr):
                    currentLocation = getattr(currentLocation, attr)
                    character.change_location(currentLocation)

                else:
                    print(f'\n{movement_error()}')  #prints a random movement error based on room

            else:
                print('\nSorry I dont know how to do that yet :(')  #incorrect 1 word statement

    elif len(request) == 2:
        if request[0] in actions:  #if valid action command
            actions[request[0]](request[1])     #in action, command at request[0] on target at request[1]

    else:
        print('\nToo many commands will confuse me D:')  #if more than 2 commands, invalid error

    if character.win_condition and character.score == len(item) and character.location == room['outside']:
        print('Congrats on finding all the items and making it out!')
        playing = False