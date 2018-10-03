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
Minion1 = Player(room['outside'])
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

while True:
    print(f'Current room: {Minion1.roomLocation.name}...')
    print(f'{Minion1.roomLocation.description}\n')
    cmd = input("Where would you like to go next?\n ->")
    if cmd == 'q':
        break
    elif cmd == 'n':
        if Minion1.roomLocation is not None:
            Minion1.roomLocation = Minion1.roomLocation.n_to
        else: print(Minion1.cannotMove)
    elif cmd == 's':
        if Minion1.roomLocation.s_to is not None:
            Minion1.roomLocation = Minion1.roomLocation.s_to
        else: print(Minion1.cannotMove)
    elif cmd == 'e':
        if Minion1.roomLocation.e_to is not None:
            Minion1.roomLocation = Minion1.roomLocation.e_to
        else: print(Minion1.cannotMove)
    elif cmd == 'w':
        if Minion1.roomLocation.w_to is not None:
            Minion1.roomLocation = Minion1.roomLocation.w_to
        else: print(Minion1.cannotMove)
    else:
        print("Your request was not recognized.")