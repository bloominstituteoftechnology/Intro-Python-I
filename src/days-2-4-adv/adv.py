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
name = input("What is your name? ")
p = Player(name, room['outside'])


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
    invalid = "You took a wrong turn! Try another direction."

    print(f'Hello, {p.name} – your current location is {p.room}.')

    cmd = input("Please choose a direction (n, s, e, or w): ")
    if cmd == "q":
        break
    elif cmd == "n":
        if hasattr(p.room, 'n_to'):
            p.changeRooms(p.room.n_to)
        else:
            print(invalid)
    elif cmd == "s":
        if hasattr(p.room, 's_to'):
            p.changeRooms(p.room.s_to)
        else:
            print(invalid)
    elif cmd == "e":
        if hasattr(p.room, 'e_to'):
            p.changeRooms(p.room.e_to)
        else:
            print(invalid)
    elif cmd == "w":
        if hasattr(p.room, 'w_to'):
            p.changeRooms(p.room.w_to)
        else:
            print(invalid)
    else:
        print("Please choose a direction (n, s, e, w) or press q to quit")
