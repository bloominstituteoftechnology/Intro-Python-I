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

# print('check attribute', room['outside'].n_to.place)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
play = True
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


def currentLocation():
    print(f"""
    ~~~~~~~ You Have Entered ~~~~~~~ 
    {player.room.place}
    """)

    print(f"""
    ~~~~~~~ Hint ~~~~~~~ 
    {player.room.description}

    """)


def inputError():
    print(f"""

    ~~~~~~~ You Hit A Wall ~~~~~~~ 
    Nowhere To Go, Try Another Direction

    """)


def lookAhead():
    print(f"""

    ~~~~~~~ What Lies Ahead ~~~~~~~ 
    {player.nextRoom}

    """)



while play:

    cmd = input('Where Shall You Go? -> ').lower().split(" ")

    if len(cmd) == 1:
        if cmd[0] == 'q':
            break
        elif cmd[0] == 'n':
            if player.room.n_to is not None:
                player.updateRoom(player.room.n_to)
                currentLocation()
            else:
                inputError()
        elif cmd[0] == 's':
            if player.room.s_to is not None:
                player.updateRoom(player.room.s_to)
                currentLocation()
            else:
                inputError()
        elif cmd[0] == 'e':
            if player.room.e_to is not None:
                player.updateRoom(player.room.e_to)
                currentLocation()
            else:
                inputError()
        elif cmd[0] == 'w':
            if player.room.w_to is not None:
                player.updateRoom(player.room.w_to)
                currentLocation()
            else:
                inputError()
        else:
            if cmd[0] == "ln":
                if player.room.n_to is not None:
                    player.lookNextRoom(player.room.n_to)
                    lookAhead()
                else:
                    inputError()
            elif cmd[0] == "ls":
                if player.room.s_to is not None:
                    player.lookNextRoom(player.room.s_to)
                    lookAhead()
                else:
                    inputError()
            elif cmd[0] == "le":
                if player.room.e_to is not None:
                    player.lookNextRoom(player.room.e_to)
                    lookAhead()
                else:
                    inputError()
            elif cmd[0] == "lw":
                if player.room.w_to is not None:
                    player.lookNextRoom(player.room.w_to)
                    lookAhead()
                else:
                    inputError()
            else:
                print('Movement Not Allowed')
