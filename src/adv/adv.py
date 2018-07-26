from room import Room
from player import Player

# Declare all the rooms

rooms = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mouth beckons"),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'chasm': Room("The Chasm of Despair", "You step off solid ground into the Chasm of Despair and tumble endlessly into the void, never to be seen again. What were you thinking?"),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


# Link rooms together

rooms['outside'].n_to = 'foyer'
rooms['foyer'].s_to = 'outside'
rooms['foyer'].n_to = 'overlook'
rooms['foyer'].e_to = 'narrow'
rooms['overlook'].s_to = 'foyer'
rooms['overlook'].n_to = 'chasm'
rooms['narrow'].w_to = 'foyer'
rooms['narrow'].n_to = 'treasure'
rooms['treasure'].s_to = 'narrow'

rooms['treasure'].items.append('treasure')
#
# Main
#

# Check to see if the user can move in a direction
def tryDirection(direction, currentRoom):
    key = direction + "_to"
    destination = getattr(rooms[currentRoom], key)
    if destination == None:
        print("You can't go that way!")
        return currentRoom
    return destination

# Make a new player object that is currently in the 'outside' room.
player=Player('outside')

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

done = False

while not done:
    currentRoom = getattr(player, 'currentRoom')
    print("\n{}".format(getattr(rooms[currentRoom], 'name')))
    print("{}".format(getattr(rooms[currentRoom], 'description')))
    if (getattr(rooms[currentRoom], 'items') != []):
        print("Here, you see:")
    for item in getattr(rooms[currentRoom], 'items'):
        print("{}".format(item))
    command = input("\n> ").strip().lower()
    if (command == 'q') or (command == 'quit'):
        done = True
    #elif (command == 'h' or 'help'):
        #print("LIST OF COMMANDS:")
        #for command in commands:
            #print(command, "\t", commands[command])
    elif command in ['n', 's', 'e', 'w']:
        destination = tryDirection(command, currentRoom)
        setattr(player, 'currentRoom', destination)
    else:
        print("Unknown command {}".format(command))
