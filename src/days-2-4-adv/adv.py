from room import Room
from player import Player

# Declare all the rooms
 
room = {
    'outside':  Room('Outside Cave Entrance',
                     'North of you, the cave mount beckons', 'outside'),

    'foyer':    Room('Foyer', '''Dim light filters in from the south. Dusty
passages run north and east.''', 'foyer'),

    'overlook': Room('Grand Overlook', '''A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.''', 'overlook'),

    'narrow':   Room('Narrow Passage', '''The narrow passage bends here from west
to north. The smell of gold permeates the air.''', 'narrow'),

    'treasure': Room('Treasure Chamber', '''You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.''', 'treasure'),
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
class Main:
    def start(self):
# Make a new player object that is currently in the 'outside' room.
        player1 = Player('Das', room['outside'])
        print('Hello ' + player1.name + '!!!!!!')
        player1.getRoom()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters 'q', quit the game.

        move = ''
        while move != 'q':
            move = input('---> What is your next move, ' + player1.name + ': NORTH(n), SOUTH(s), EAST(e) OR WEST(w) or QUIT(q) the game: ')
            if move != 'q':
                keyPress = move + '_to'
                try:
                    print(getattr(player1.room, keyPress).abr)
                    room[getattr(player1.room, keyPress).abr]
                except AttributeError:
                    print('---> Impossible to go to that direction! Choose different one.\n')
                    player1.getRoom()
                except KeyError:
                    print('---> Impossible to go to that direction! Choose different one.\n')
                    player1.getRoom()
                else:
                    player1.room = room[getattr(player1.room, keyPress).abr]
                    player1.getRoom()
            else:
                print('Game over!')

game1 = Main()
game1.start()