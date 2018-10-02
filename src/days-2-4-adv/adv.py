from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [Item("golden cup", "a shimmering goblet studded with jewels")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    [Item("long sword", "a sharp, heavy blade")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. There is a bookshelf along the north wall. The only exposed 
exit is to the south. """,
                    [Item("leather-bound book", "a mysterious tome with missing pages")]),
    
    'hidden': Room("Hidden Room", """You've found a tiny, musty, hidden room 
    behind a bookshelf. Exits are to the west and south. A bright, revolving 
    light appears west.""",
                    [Item("pile of gold coins", "maybe they're real gold"), 
                    Item("lit candle", "a burning flame to help in the dark night")]),
    
    'lighthouse': Room("Glimmering Lighthouse", """A tall, white-and-red 
    lighthouse stands towering above you. The door is locked. Paths lead 
    east, and west to a beach.""", 
                    [Item("broken mirror", "sharp edges and big cracks")]),
    
    'beach': Room("Sandy Beach", """A broad sandy beach lies before you. 
    Sea shells are scattered around. The ocean looks cold and uninviting. 
    The only exit is east.""", 
                    [Item("conch shell", "a pale shell with an opening")])
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
player = Player('Hanzo', room['outside'], [Item("iron chestplate", "a durable armor piece")])

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
    elif cmd.upper() == 'S' or cmd.upper() == 'SOUTH':
        if hasattr(currentRoom, 's_to'):
            player.currentRoom = currentRoom.s_to
        else:
            printNoMove()
    elif cmd.upper() == 'E' or cmd.upper() == 'EAST':
        if hasattr(currentRoom, 'e_to'):
            player.currentRoom = currentRoom.e_to
        else:
            printNoMove()
    elif cmd.upper() == 'W' or cmd.upper() == 'WEST':
        if hasattr(currentRoom, 'w_to'):
            player.currentRoom = currentRoom.w_to
        else:
            printNoMove()
    elif cmd.upper() == 'INV' or cmd.upper() == 'I':
        if len(player.inventory) > 0:
            print("You have:")
            for item in player.inventory:
                print(item.name)
        else:
            print("You do not have any items besides the shirt on your back.")
    elif "TAKE" in cmd.upper():
        for item in currentRoom.inventory:
            if cmd[5:] in item.name:
                player.inventory.append(item)
                currentRoom.inventory.remove(item)
                print("You have taken the %s" % item.name)
            else:
                print("Sorry, %s, that item is not in this room." % player.name)
    elif "DROP" in cmd.upper():
        for item in player.inventory:
            if cmd[5:] in item.name:
                player.inventory.remove(item)
                currentRoom.inventory.append(item)
                print("You have dropped the %s." % item.name)
            else:
                print("You are not carrying that item.")
    elif cmd.upper() == 'Q' or cmd.upper() == 'QUIT':
        break
    else:
        print("That command is not valid.")