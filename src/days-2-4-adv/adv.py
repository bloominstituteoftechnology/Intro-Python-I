from room import Room
from player import Player
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

room['outside'].connectRoom('n', room['foyer'])
room['foyer'].connectRoom('n',room['overlook'])
room['foyer'].connectRoom('e',room['narrow'])
room['narrow'].connectRoom('n',room['treasure'])
room['treasure'].connectRoom('e',room['narrow'])


# player.set_location(room['foyer'])
# player.get_current_location()
# player.go_direction('n')

# player.get_current_location()

# name, age, height, weight, hp, attack, defense, inventory
player = Player('John', 14, 1, 180, 12, 5, 4, {})
player.set_location(room['foyer'])

directions = ['n','s','w','e']
import os
while(True):
    command = input("""
    Type in a command:

    Directions[n,s,e,w]

    Get Room info: [room info]

    Other commands: [q: quit]
    
    """)
    os.system('cls' if os.name == 'nt' else 'clear')
    for direction in directions:
        if command == direction:
            player.go_direction(command)
    
    if command == 'room info':
        player.get_current_location()
    
    elif command == 'q':
        quit()
       
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
