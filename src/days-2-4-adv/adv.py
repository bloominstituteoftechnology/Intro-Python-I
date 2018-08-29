from room import Room
from player import Player
from dialogue import Dialogue
import os
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

room['outside'].connect_rooms('e', room['foyer'])
room['foyer'].connect_rooms('n',room['overlook'])
room['overlook'].connect_rooms('w',room['narrow'])
room['narrow'].connect_rooms('s',room['treasure'])
room['treasure'].connect_one_way('s',room['outside'])

def displayHelp():
    print("""
    Type in a command:

    Directions[n,s,e,w]

    Get info: [se: scan enemies]

    Battle: [a [Enemy]: attack [Enemy]]

    Other commands: [q: quit]
    """)

def printErrorString(errorString):
    print(f'\x1b[1;31;40m\n{errorString}\x1b[0m\n')

Dialogue.intro()
player = Player.create_player()
player.set_location(room['outside'])
Dialogue.greet_player(player.name)

playerCommands = {
    'directions': ['n','s','w','e'],
    'help': displayHelp,
    'hp': player.check_hp,
    'q': quit
}


while(True):
    player.get_current_location()
    
    command = input(">>>")
    
    os.system('cls' if os.name == 'nt' else 'clear')

    
    for direction in playerCommands['directions']:
        if command == direction:
            player.go_direction(command)
    
    if command in playerCommands:
        playerCommands[command]()
    else:
        printErrorString('Invalid command')

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
