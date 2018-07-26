from room import Room
from rooms import rooms
from player import Player
from item import Item
from items import items
from creature import Creature
from helpfile import listOfCommands

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

# Put items in rooms
rooms['outside'].items.append('treasure')

# Put creatures in rooms
rooms['treasure'].creatures.append('dragon')


#
# Main
#

# Check to see if the user can move in a direction
def tryDirection(direction, currentRoom):
    key = direction + "_to"
    print(key)
    destination = getattr(rooms[currentRoom], key)
    if destination == None:
        print("You can't go that way!")
        return currentRoom
    return destination

# Make a new player object that is currently in the 'outside' room.
player=Player('outside', 'Ellen')

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
    
# GET USER INPUT
    commands = input("\n> ").strip().lower().split(' ')
    if (len(commands) == 1):
        command = commands[0]
    # QUIT THE GAME
        if (command == 'q') or (command == 'quit'):
            done = True
    # DISPLAY A LIST OF COMMANDS
        #if (command == 'h' or 'help'):
            #print("LIST OF COMMANDS:")
            #for cmd in listOfCommands:
                #print(cmd, "\t", listOfCommands[cmd])
    # MOVE THE PLAYER CHARACTER
        if command in ['n', 's', 'e', 'w']:
            destination = tryDirection(command, currentRoom)
            setattr(player, 'currentRoom', destination)
        if command in ['north', 'south', 'east', 'west']:
            destination = tryDirection(command[0], currentRoom)
            setattr(player, 'currentRoom', destination)
    # HANDLE UNRECOGNIZED INPUT
        #else:
            #print("Unknown command {}. Type 'help' for a list of commands.".format(command))
    elif len(commands) == 2:
        verb = commands[0]
        noun = commands[1]
        if verb == 'g' or 'get':
            item = 
            rooms[currentRoom].remove