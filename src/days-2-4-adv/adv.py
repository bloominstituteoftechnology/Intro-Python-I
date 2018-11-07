from room import Room
from player import Player
import textwrap

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
stop = False

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
print (player.room)
print (player.room.name)

# Rooms are initiliazed with no items. To add them, use the
# Room.add_items(*items) method. You may pass in a  list,
# individual items, or a combination of both
# e.g. Room.add_items('sword', 'shield', ['treasure, 'crown', 'chalice'])

room['outside'].add_items('rocks', ['skull', 'abandoned armor'])

def action(phrase):
    verb = phrase[0]
    noun = phrase[1]
    if verb in ['get', 'take', 'lift', 'grab', ]:
        if noun in player.room.item_list:
            player.room.remove_items(noun)
            player.add_items(noun)
            print (f'Thou hath picked up one {noun}')
        else:
            print ('The item thou look for is not here')
    elif verb in ['drop', 'leave', 'forget', 'dump', 'discard', 'abandon' ]:
        if noun in player.item_list:
            player.remove_items
            player.room.add_items(noun)
            print (f'Thou hath dropped thy {noun}')
        else:
            print ('Thou hath not the item thou speak of')
    else:
        print ('I understand not thy command. Please choose another one')


def movement_or_inv(move):
    move = move[0]   
    if move in ['n', 'e', 's', 'w', 'q', 'i', 'items', 'inventory', 'quit']:
        if move == 'n':
            try:
                player.room = player.room.n_to
                print ('Thou attemps to move north-ward')
            except AttributeError:
                print('You may not move in that direction. Try again')
        elif move == 'e':
            try:
                player.room = player.room.e_to
                print ('Thou attemps to move east-ward')
            except AttributeError:
                print('You may not move in that direction. Try again')
        elif move == 's':
            try:
                print ('Thou attemps to move south-ward')
                player.room = player.room.s_to
            except AttributeError:
                print('You may not move in that direction. Try again')
        elif move == 'w':
            try:
                print ('Thou attemps to move west-ward')
                player.room = player.room.w_to
            except AttributeError:
                print('You may not move in that direction. Try again')
        elif move in ['inventory', 'i', 'items']:
            print ('~ ~ Thy current inventory ~ ~')
            print (player.item_list if player.item_list else 'Thou hath nothing')
        elif move == 'q' or move == 'quit':
            print ('Farewell, you coward')
            global stop
            stop = True
    else:
        print ('Please enter a cardinal direction or "q" to quit')


while stop == False:
    print (' ')
    print ('Thy current location:', player.room.name)
    print ( textwrap.wrap(player.room.description) )
    print ('~ ~ Items found in this room ~ ~')
    print ( player.room.item_list)
    command = input('What shall thou do next?     ')
    print ()
    try:
       command = command.lower()
    except AttributeError:
        print ('Please enter an english instruction')
        continue
    command = command.split()
    if len(command) == 1:
        movement_or_inv(command)
    elif len(command) == 2:
        action(command)
    else:
        print ('Thy hath not been understood. Tryeth again')


