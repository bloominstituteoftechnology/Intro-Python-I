from room import Room
from player import Player
from items import Item
import textwrap
from textwrap import fill

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "You don't find anything of significance here."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "You found a Short Sword! Take Item? (Yes/No) "),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "You found a Shield! Take Item? (Yes/No)"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "You found a strange coin... Take Item? (Yes/No)"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "You found a note that reads, 'You're too late fool!'")
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
player = Player(input("Enter your name: "), room['outside'], [])
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
    roomDesc = textwrap.fill(curRoom.description)
    foundItem = curRoom.item

    print("Hello, " + str(player.name))
    
    print("\n{}\n{}\n\n{}\n".format(curRoom.name, roomDesc, foundItem))

    command = input("What do you want to do? >>> ").strip().lower()

    if command == 'q' or command == 'quit' or command == 'exit':
        done = True
    
    elif command in ["s", "n", "e", "w"]:
        dirAttr = command + "_to"

        if hasattr(curRoom, dirAttr):
            player.room = getattr(curRoom, dirAttr)
        else:
            print("That way is blocked")
    
    else:
        print("I'm not sure what you mean...")