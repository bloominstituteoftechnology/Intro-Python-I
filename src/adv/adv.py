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
name = input("Enter your name:\n")
player = Player(name, 'outside')

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

while (player.room_name != 'exit'):
    print("\n" + player.name + " is at the\n" + room[player.room_name].name + ": " + room[player.room_name].description + "\n")
    instruction = input("Enter North, East, South, or West or q to Quit:\n")
    if (instruction == "q"):
        break
    elif (instruction == "North"):
        try:
            key = [k for k, v in room.items() if v == room[player.room_name].n_to]
            player.room_name = ''.join(key)
        except AttributeError:
            print("\nThis movement is not allowed!")
    elif (instruction == "East"):
        try:
            key = [k for k, v in room.items() if v == room[player.room_name].e_to]
            player.room_name = ''.join(key)
        except AttributeError:
            print("\nThis movement is not allowed!")
    elif (instruction == "South"):
        if (player.room_name == "treasure"):
            break
        try:
            key = [k for k, v in room.items() if v == room[player.room_name].s_to]
            player.room_name = ''.join(key)
        except AttributeError:
            print("\nThis movement is not allowed!")
    elif (instruction == "West"):
        try:
            key = [k for k, v in room.items() if v == room[player.room_name].w_to]
            player.room_name = ''.join(key)
        except AttributeError:
            print("\nThis movement is not allowed!")
    else:
        print("\nThis is not a direction! Go \"North\", \"East\", \"South\", \"West\" or \"q\" to Quit")

print("\nYou are out of the cave and empty handed!\n")
    
    


