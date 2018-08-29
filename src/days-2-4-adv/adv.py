from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     *[Item("Rock", """Who knows how useful this could be!"""),
                     Item("Grass", """A nutritious treat should you get hungry in your travels"""),
                     Item("Key", """Who knows what doors this may open?""")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", *[Item("Umbrella", """This will protect against
suppressive  waterpower""")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", *[Item("Axe",
"""Heeeerrre's Johnny!"""), Item("Native American Artifact", """Legend says this
artifact allows the possessor to communicate telepathically with the ghost of
Scatman Crothers""")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", *[Item("Torch", """Batteries
included"""), Item("Wet Mud", """Gross!""")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", *[Item("Empty Treasure Chest",
"A big box that once held great treasure"), Item("Scribbled Note", """A note
containing a famous director's explanation of a mysterious hotel room...""")]),
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

#print(room['outside'].name)

# Make a new player object that is currently in the 'outside' room.

player1 = Player(room['outside'], [Item('Pen', 'A mighty instrument to influence minds'), Item('Sword', 'Not as mighty...')])

suppressRoomPrint = False

while(True):
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print('\n [{}]...\n'.format(player1.location.name))
        print('...{}\n'.format(player1.location.description))
        inp = input('Which direction will you move?')

    if inp == 'q':
        break
    elif inp == 'n' or inp == 's' or inp == 'e' or inp == 'w':
        newRoom = player1.location.getRoomDirection(inp)
        if newRoom == None:
            print('\n -Thwack! You just hit a brick wall (or fell off a cliff), choose another direction-\n')
        else:
            player1.change_location(newRoom)
    elif inp == 'inventory':
        for item in player1.inventory:
            print('{} {}'.format(item.name, item.description))
    elif inp == "look":
        print('\nThis room contains...')
        for item in player1.location.items:
            print('\n-- {}: {}--\n'.format(item.name, item.description))
    else:
        print('None has traveled catacorner to the three dimensions...invalid input try again...')

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
