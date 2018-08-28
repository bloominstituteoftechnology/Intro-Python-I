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

# Main

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Schpilkus', room['overlook'])

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

while True:
    print(f'\nCurrent location:  {player1.location.name}.')
    print(player1.location.description + '\n')

    direction = input('Where to (N,S,E,W)?')

    if direction.lower() == 'q':
        print('\nUntil next time...\n')
    else:
        if Room(player1.location, direction):
          if direction.lower() == 'n':
            player1.location = player1.location.n_to
          if direction.lower() == 's':
            player1.location = player1.location.s_to
          if direction.lower() == 'e':
            player1.location = player1.location.w_to
          if direction.lower() == 'w':
            player1.location = player1.location.e_to
        else:
          print('\nImpossible, try again.\n') 

