from room import Room
from player import Player
from os import system

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
system("clear")
name = input("Enter your name:\n")
player = Player(name, room['outside'])

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

system("clear")
while (player.room != 'exit'):
    print(player.name + " is at the\n" + player.room.name + ": " + player.room.description + "\n")
    instruction = input("Enter North, East, South, or West or q to Quit:\n")
    direction = {
        "North": player.room.n_to,
        "East": player.room.e_to,
        "South": player.room.s_to,
        "West": player.room.w_to
    }

    new_room = direction.get(instruction, None)
    system("clear")
    if (instruction == "q"):
        break
    elif (new_room):
        if (player.room.name == "Treasure Chamber"):
            break
        player.room = new_room
    elif (instruction in ["North", "East", "South", "West"]):
        print("Nowhere to go\n")
    else:
        print("This is not a direction! Go \"North\", \"East\", \"South\", \"West\" or \"q\" to Quit\n")

system("clear")
print("You are out of the cave and empty handed!\n")