from room import Room
from player import Player
import textwrap
import time

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

# player = Player(room['outside'])
# print(player.currentRoom.description)

p = Player(input('\n\n\n\n\nWhat is your name?'), room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    time.sleep(1)
    cmd = input('\n\n\n\n\nYou are in the main menu. Are you ready? \n=>')

    if cmd.upper() == 'YES':
        while True:
            currentRoom = p.currentRoom
            def error():
                time.sleep(2)
                print('\nYou cannot go in that direction! Try another direction!')
            time.sleep(2)
            print('\n\n\nYour location is: ') 
            time.sleep(1)
            print(currentRoom)
            time.sleep(1)
            cmd = input('\n\n\nWhere do you want to go?\n=>')

            if cmd.upper() == 'N':
                if hasattr(currentRoom, 'n_to'):
                    p.currentRoom = currentRoom.n_to
                else:
                    error()
            elif cmd.upper() == 'S':
                if hasattr(currentRoom, 's_to'):
                    p.currentRoom = currentRoom.s_to
                else:
                    error()
            elif cmd.upper() == 'W':
                if hasattr(currentRoom, 'w_to'):
                    p.currentRoom = currentRoom.w_to
                else:
                    error()
            elif cmd.upper() == 'E':
                if hasattr(currentRoom, 'e_to'):
                    p.currentRoom = currentRoom.e_to
                else:
                    error()
            elif cmd.upper() == 'Q':
                time.sleep(1)
                cmd = input('\n\n\nAre you sure you want to quit the game?\n=>')
                if cmd.upper() == 'YES':
                    time.sleep(1)
                    print('Goodbye!')
                    break
                elif cmd.upper() == 'NO':
                    continue
                else:
                    time.sleep(1)
                    print('\nI cannot understand. Let\'s continue!')
            else:
                time.sleep(1)
                print('You can only go north, south, east or west! Try going somewhere!')

    elif cmd.upper() == 'NO':
        time.sleep(2)
        print('Are you afraid?')
        time.sleep(1) 
    elif cmd.upper() == 'Q':
        time.sleep(2)
        print('\n\n\nGoodbye')
        time.sleep(2) 
        print('coward...\n\n\n\n\n')
        time.sleep(1) 
        break
    else:
        time.sleep(2) 
        print('\nI cannot understand you!')
        time.sleep(1) 
        print('\Yes or no?')
        time.sleep(2) 
