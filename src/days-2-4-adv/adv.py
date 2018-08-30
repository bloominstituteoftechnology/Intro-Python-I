from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'N'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'S', 'N', 'E'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. There is a chest near the door to the south""", 'S'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'W', 'N'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers, but you might find something if you look around. The only exit is to the south.""", 'S'),
}


# Add items to rooms

room['overlook'].addItem('key' ,"You pick up the key, best to hold on to it, it might come in handy later.")
room['treasure'].addItem('rock', 'You pick up the jagged rock, maybe you can throw it at something?')
room['treasure'].addItem('note', 'You pick up old note, "captivated by the view over the cliff, you never even notice what\'s above you"')

# Link rooms together

def connectRooms(r1, to, r2):
    # r1 goes (N, S, E, W, U, or D) to r2
    r1.connect(r2, to)
    if to is 'N':
        r2.connect(r1, "S")
    elif to is 'E':
        r2.connect(r1, "W")
    elif to is 'S':
        r2.connect(r1, "N")
    elif to is 'W':
        r2.connect(r1, "E")
    elif to is 'U':
        r2.connect(r1, "D")
    elif to is 'D':
        r2.connect(r1, "U")

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']

connectRooms(room['outside'], 'N', room['foyer'])

# room['overlook'].s_to = room['foyer']
# room['foyer'].n_to = room['overlook']

connectRooms(room['overlook'], 'S', room['foyer'])

# room['narrow'].w_to = room['foyer']
# room['foyer'].e_to = room['narrow']

connectRooms(room['narrow'], 'W', room['foyer'])

# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

connectRooms(room['narrow'], 'N', room['treasure'])


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

direction = [ 'N', 'E', 'S', 'W', 'U', 'D' ]
hideRoomDesciption = 'false'

player = Player( input("\nWhat is your name?: ") , room['outside'])

print (f'\nWelcome, {player.name}!\n')

while 'true':
    if hideRoomDesciption is 'true':
        hideRoomDesciption = 'false'
    else:
        print(f'\n{player.roomDescription()}\n')

    inputList = input("\nWhat would you like to do?: ").upper().split(' ')

    if inputList[0] == 'Q':
        break

    elif inputList[0] in direction:
        if player.move(inputList[0]) == 'false':
            hideRoomDesciption = 'true'
            print('\nYou cannot go that way!')

    elif inputList[0] == 'SEARCH' or 'OPEN':
        hideRoomDesciption = 'true'
        if len(player.location.items) == 0:
            print('you don\'t find anything')
        elif len(player.location.items) == 1:
            for item in player.location.items:
                print(f'You find a {item}\n')
        elif len(player.location.items) > 1:
            print('You find some items: ')
            for item in player.location.items:
                print(item)
