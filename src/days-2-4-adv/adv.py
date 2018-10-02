from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    ["golden cup"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    ["long sword"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. There is a bookshelf along the north wall. The only exposed 
exit is to the south. """,
                    ['leather-bound book']),
    
    'hidden': Room("Hidden Room", """You've found a tiny, musty, hidden room 
    behind a bookshelf. Exits are to the west and south. A bright, revolving 
    light appears west.""",
                    ["pile of gold coins", "lit candle"]),
    
    'lighthouse': Room("Glimmering Lighthouse", """A tall, white-and-red 
    lighthouse stands towering above you. The door is locked. Paths lead 
    east, and west to a beach.""", 
                    ["broken mirror"]),
    
    'beach': Room("Sandy Beach", """A broad sandy beach lies before you. 
    Sea shells are scattered around. The ocean looks cold and uninviting. 
    The only exit is east.""", 
                    ["conch shell"])
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

room['treasure'].n_to = room['hidden']
room['hidden'].s_to = room['treasure']
room['hidden'].w_to = room['lighthouse']
room['lighthouse'].e_to = room['hidden']
room['lighthouse'].w_to = room['beach']
room['beach'].e_to = room['lighthouse']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

# Player init
player = Player('Hanzo', room['outside'], ["iron chestplate"])

# Input loop
while True:
    def printNoMove():
        print('\nSorry, %s, you cannot move in that direction.' % player.name)

    currentRoom = player.currentRoom

    print('\n')
    currentRoom.printName()
    currentRoom.printDesc()
    currentRoom.printInv()
    print('\n')

    cmd = input("What would you like to do, %s? " % player.name)

    if cmd.upper() == 'N' or cmd.upper() == 'NORTH':
        if hasattr(currentRoom, 'n_to'):
            player.currentRoom = currentRoom.n_to
        else:
            printNoMove()
    if cmd.upper() == 'S' or cmd.upper() == 'SOUTH':
        if hasattr(currentRoom, 's_to'):
            player.currentRoom = currentRoom.s_to
        else:
            printNoMove()
    if cmd.upper() == 'E' or cmd.upper() == 'EAST':
        if hasattr(currentRoom, 'e_to'):
            player.currentRoom = currentRoom.e_to
        else:
            printNoMove()
    if cmd.upper() == 'W' or cmd.upper() == 'WEST':
        if hasattr(currentRoom, 'w_to'):
            player.currentRoom = currentRoom.w_to
        else:
            printNoMove()
    if cmd.upper() == 'INV' or cmd.upper() == 'I':
        if len(player.inventory) > 0:
            print("You have: ", player.inventory)
        else:
            print("You do not have any items besides the shirt on your back.")
    if "TAKE" in cmd.upper():
        if cmd[5:] in currentRoom.inventory:
            player.inventory.append(cmd[5:])
            currentRoom.inventory.remove(cmd[5:])
            print("You have taken the %s" % cmd[5:])
        else:
            print("Sorry, %s, that item is not in this room." % player.name)
    if "DROP" in cmd.upper():
        player.inventory.remove(cmd[5:])
        currentRoom.inventory.append(cmd[5:])
        print("You have dropped the %s." % cmd[5:])
    if cmd.upper() == 'Q':
        break