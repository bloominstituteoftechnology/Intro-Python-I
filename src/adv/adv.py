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

name = input('Enter your name Traveler: ')

defaultRoom = 'outside'

# this creates the player
player1 = Player(name,defaultRoom)


 #currentRoom = Room(name, room[currentRoom.description])

print("Welcome " + player1.name)
print("You are currently in " + player1.room)
#print(currentRoom.description)
print(room[name][description])

#print('You are currently in the ' + room['outside'])

# Write a loop that:
#
# * Prints the current room name
print(currentRoom.name)

# * Prints the current description (the textwrap module might be useful here).
print(currentRoom.description)
# * Waits for user input and decides what to do.
direction = input('Please enter the direction you would like to go: ')
#
# Print an error message if the movement isn't allowed.
if direction == 'north':
    currentRoom.name = 'foyer'

if direction == 'q':
    exit()

#
# If the user enters "q", quit the game.
