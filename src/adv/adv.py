from os import system
from room import Room
from player import Player
import textwrap # or from textwrap import fill

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

    'dungeon': Room("The Dungeon", """You've entered the dark, smelly dungeon of doom!
now you are cursed for 10 million years and forever the
caregiver for these smelly pugs. Exit to the east."""),

    'pugs': Room("Pugs Dungeon", """You've awoken the beasts!"""),
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
room['dungeon'].w_to = room['pugs']
room['pugs'].e_to = room['dungeon']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
system("clear") # clears console before you start your game (be sure to add os import system)

player_name = input("Enter a player name: ") # Welcomes player by asking them for their name

player = Player(player_name, room['outside'])

print("\nWelcome, %s!" % (player.playerName)) # Welcomes player by name they entered above

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

def dircheck(attr):
    if(hasattr(player.room, attr)):
        player.room = getattr(player.room, attr)
    else:
        print("\nYou Shall Not Pass\n")

while True:
    print(player.room.name)
    print(textwrap.fill(player.room.description, 50))
    cmd = input("Which Direction Would You Like To Go? (q for quit):")
    if cmd == "q": # q = quit
        break
    elif cmd == "n": # n = North
        dircheck("n_to")
    elif cmd == "e": # e = East
        dircheck("e_to")
    elif cmd == "s": # s = South
        dircheck("s_to")
    elif cmd == "w": # w = West
        dircheck("w_to")
    else:
        print("\nWrong Way - Try Again\n")


# Instructor Solve------------------------------------
# done = False

# while not done:
#     curRoom = player.room

#     prettyDesc = textwrap.fill(curRoom.description)

#     print(f'{curRoom.name}\n{prettyDesc}')

#     command = input("Command> ").strip().lower()

#     if command == 'q' or command == 'quit' or command == 'exit':
#         done = True

#     elif command in ["s", "n", "e", "w"]:
#         dirAttr = command + "_to"

#         if hasattr(curRoom, dirAttr):
#             player.room = getattr(curRoom, dirAttr)

#         else:
#             print("You can't go that way.")

#     else:
#         print("I don't understand that!")