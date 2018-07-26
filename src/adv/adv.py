from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", 
                     "To the East you see a bus stop! North of you, the cave mount beckons"),

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

    'bus stop': Room("bus stop", """You're now waiting at the bus stop, too bad 
there isnt another bus coming until next month! You might as well head back west and explore these rooms!"""),

    'basement': Room("basement", """You're in the basement, its dark, you trip over something on the floor.
do you pick it up?""")
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].e_to = room['bus stop']
room['bus stop'].w_to = room['outside']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].e_to = room['basement']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("yasin", room['outside'])

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

done = False

while not done:
    curRoom = player.room
    print(f'{curRoom.name}\n{curRoom.description}')

    command = input("Command>").strip().lower()

    if command == 'q' or command == 'quit' or command == 'exit':
        done = True

    elif command in ["s", "n", "e", "w"]:
        dirAttr = command + "_to"

        if hasattr(curRoom, dirAttr):
               player.room = getattr(curRoom, dirAttr)
        else:
                    print("you cant go that way homie")

    else:
         print("i dont recognize that, what set you claiming? ")