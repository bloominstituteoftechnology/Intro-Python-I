from room import Room
from player import Player
from item import Item
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
#Declare items
item={
    'sword':Item('sword',"""Just a basic sword to hack at monsters with ... nothing fancy."""),
    'candle':Item('candle',"""Useful for keeping the Boogeyman at bay."""),
    'rock':Item('rock',"""A big rock ... not useful at all."""),
    'sandwich':Item('sandwich',"""Sustenance for when you get hungry later."""),
    'lasso':Item('lasso', """Not sure if it makes people tell the truth or makes one go Indiana Jones.""")
}
room['outside'].inventory.append(item['sword'])
room['foyer'].inventory.append(item['candle'])
room['overlook'].inventory.append(item['rock'])
room['narrow'].inventory.append(item['sandwich'])
room['treasure'].inventory.append(item['lasso'])
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
def game():
    player=Player(input('What is your name?\n'),room['outside'])
    print(f'Hello, {player.name}\n{player.current_location}')
    while True:
        cmd=input('-->').lower().split()
        if len(cmd)==2:
            if cmd[0]=='get':
                print(player.pickup(cmd[1]))
            elif cmd[0]=='drop':
                print(player.drop(cmd[1]))
            else:
                print('Invalid command.')
        elif len(cmd)==1:
            if cmd[0]=='n' or cmd[0]=='e' or cmd[0]=='s' or cmd[0]=='w':
                print(player.travel(cmd[0]))
            elif cmd[0]=='q':
                break
            elif cmd[0]=='i':
                print(player.i())
            elif cmd[0]=='inventory':
                print(player.inventory())
            else:
                print('Invalid command.')
        else:
            print('Invalid command')
game()