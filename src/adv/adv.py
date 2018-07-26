from item import Item
from player import Player
from room import Room

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

def takeItem(self, target):
    print(f'\n{target} in takeItem')
    item = currentLocation.item_found(target)
    if item:
        character.pick_up(item)
        print(f"\n{item} has been picked up!")
    else:
        print('\nInvalid Input')

def dropItem(self, target):
    item = character.drop(target)
    if item:
        currentLocation.item_dropped(item)
        print(f"\n{item} has been dropped!")
    else:
        print('\nInvalid Input')

def viewItem(self, target):
    descript = character.inspect(target)
    if descript:
        print(f'\n{descript}')
    else:
        print('\nInvalid Input')


movements = ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west']
# actions = ['t', 'take', 'd', 'drop', 'ins', 'inspect']
actions = {
    't': takeItem,
    'take': takeItem,
    'd': dropItem,
    'drop': dropItem,
    'ins': viewItem,
    'inspect': viewItem
}

def executeAction(command, target):
    print(f'\n{command} {target} in execution')
    actions[command](target)

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

        elif request[0] == 'i' or request[0] == 'inv' or request[0] == 'inventory':
            print(f'\nCurrent Inventory: {character.print_inv()}')

        else:

            if request[0] in movements:
                attr = request[0][0] + '_to'

                if hasattr(currentLocation, attr):
                    currentLocation = getattr(currentLocation, attr)
                    character.change_location(currentLocation)
                else:
                    print('\nInvalid Input')

            else:
                print('\nInvalid Input')

    elif len(request) == 2:
        action = request[0]
        target = request[1]
        if request[0] in actions:
            print(f'\n{action} {target} in loop')
            executeAction(action, target)
        # if request[0] == 'take' or request[0] == 't':
        #     taken_item = currentLocation.item_found(request[1])
        #     if taken_item:
        #     else:
        #         print('\nInvalid Input')
        # elif request[0] == 'drop' or request[0] == 'd':
        #     dropped_item = character.drop(request[1])
        #     if dropped_item:
        #         currentLocation.item_dropped(dropped_item)
        #         print(f"\n{dropped_item} has been dropped!")
        #     else:
        #         print('\nInvalid Input')
        # elif request[0] == 'inspect' or request[0] == 'ins':
        #     descript = character.inspect(request[1])
        #     if descript:
        #         print(f'\n{descript}')
        #     else:
        #         print('\nInvalid Input')
        # else:
        #     print('\nInvalid Input')
    else:
        print('\nInvalid Input')