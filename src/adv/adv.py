from os import system # for system clear on game play
from room import Room
from player import Player
from item import Item
import textwrap # or from textwrap import fill

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Lantern", "A Lantern to light your way")]),

    'foyer':    Room("\nFoyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("\nGrand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("\nNarrow Passage", """The narrow passage bends here from west
to north and south. The smell of gold permeates the air."""),

    'treasure': Room("\nTreasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south, but you smell something from the North.""", [Item("Shield", "A shield made of sturdy steel")])),
    # Rm I added on for fun
    'dungeon': Room("\nThe Dungeon", """You've entered the dark, smelly dungeon of doom!
Now you are cursed for 10 million years and forever the
caregiver for these smelly pugs. Exit to the east.""", [Item("Satchel", "A satchel made of pig skin to carry your loot")])),
    # Rm I added on for fun
    'pugcave': Room("\nPugs Cave", """Oh No!!! You've awoken the pug beasts... RUN for your lives to the only exit north!""", [Item("Fang", "A smelly pug fang for goodluck")])),
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
room['dungeon'].e_to = room['narrow']
room['narrow'].s_to = room['dungeon']
room['pugcave'].n_to = room['treasure']
room['treasure'].n_to = room['pugcave']

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
    cmd = input("\nWhich Direction Would You Like To Go? \n(n, s, e, w or q to quit):")
    if cmd == "q": # Q = quit
        break
    elif cmd in ["n", "e", "s", "w"]:
        dircheck(cmd + "_to")
    # elif cmd == "N": # N = North
    #     dircheck("n_to")
    # elif cmd == "E": # E = East
    #     dircheck("e_to")
    # elif cmd == "S": # S = South
    #     dircheck("s_to")
    # elif cmd == "W": # W = West
    #     dircheck("w_to")
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