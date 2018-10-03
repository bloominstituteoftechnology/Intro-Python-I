from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside a Cave Entrance",
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
name = input('What do ye call yourself? \n')
plyr = Player(name, room['outside'])
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
#
def err_catch():
    print('You are filled with an overwhelming sense of dread and quickly reconsider your decision.')

print(f'You find yourself just {plyr.current_room.location} with no memory of how you got here. {plyr.current_room.description} ')
while True:
    cmd = input('How should we proceed? \n')
    if cmd ==  'q':
        print('\n Knew you didnt have the constitution for this...')
        break
    elif cmd == 'n':
        if hasattr(plyr.current_room.n_to, 'location'):
            plyr.current_room = plyr.current_room.n_to
            print(f'You have entered the {plyr.current_room.location}. \n{plyr.current_room.description} ')
        else:
            err_catch()
    elif cmd == 's':
        if hasattr(plyr.current_room.s_to, 'location'):
            plyr.current_room = plyr.current_room.s_to
            print(f'You have entered the {plyr.current_room.location}. \n{plyr.current_room.description} ')
        else:
            err_catch()
    elif cmd == 'e':
        if hasattr(plyr.current_room.e_to, 'location'):
            plyr.current_room = plyr.current_room.e_to
            print(f'You have entered the {plyr.current_room.location}. \n{plyr.current_room.description} ')
        else:
            err_catch()
    elif cmd == 'w':
        if hasattr(plyr.current_room.w_to, 'location'):
            plyr.current_room = plyr.current_room.w_to
            print(f'You have entered the {plyr.current_room.location}. \n{plyr.current_room.description} ')
        else:
            err_catch()