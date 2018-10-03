from room import Room
from player import Player
from item import Item, Treasure, Lightsource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "   North of you, the cave mount beckons",
                    [Treasure("golden cup", "a shimmering goblet studded with jewels", 100)], False),

    'foyer':    Room("Foyer", 
    """    Dim light filters in from the south. 
    Dusty passages run north and east.""",
                    [Lightsource("lamp", "looks like it has a genie inside")], True),

    'overlook': Room("Grand Overlook", 
    """    A steep cliff appears before you, 
    falling into the darkness. Ahead to the north, 
    a light flickers in the distance, but there 
    is no way across the chasm.""",
                    [Item("long sword", "a sharp, heavy blade")], False),

    'narrow':   Room("Narrow Passage", 
    """    The narrow passage bends here from west
    to north. The smell of gold permeates the air.""",
                    [], False),

    'treasure': Room("Treasure Chamber", 
    """    You've found the long-lost treasure
    chamber! Sadly, it has already been completely 
    emptied by earlier adventurers. There is a 
    bookshelf along the north wall. The only exposed 
    exit is to the south. """,
                    [Item("leather-bound book", "a mysterious tome with missing pages")], True),
    
    'hidden': Room("Hidden Room", 
    """    You've found a tiny, musty, hidden room 
    behind a bookshelf. Exits are to the west 
    and south. A bright, revolving light appears west.""",
                    [Treasure("pile of silver coins", "maybe they're real silver", 100), 
                    Lightsource("lit candle", "a burning flame to help in the dark night")], False),
    
    'lighthouse': Room("Glimmering Lighthouse", 
    """    A tall, white-and-red lighthouse 
    stands towering above you. The door is 
    locked. Paths lead east, and west to a beach.""", 
                    [Item("broken mirror", "sharp edges and big cracks"),
                    Treasure("shiny ruby", "a deep red precious stone", 200)], True),
    
    'beach': Room("Sandy Beach", 
    """    A broad sandy beach lies before you. 
    Sea shells are scattered around. 
    The ocean looks cold and uninviting. 
    the only exit is east.""", 
                    [Item("conch shell", "a pale shell with an opening")], False)
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


# initialize player
playerName = input("""================================================
What is your name? """)
player = Player(playerName, room['outside'], [Item("iron chestplate", "a durable armor piece")])

suppressRoomPrint = False
# Input loop
while True:
    def printNoMove():
        print('\nSorry, %s, you cannot move in that direction.' % player.name)
        print()

    def treasureOnTake(treasure):
        if not treasure.takenAlready:
            player.increaseScore(treasure.value)

    currentRoom = player.currentRoom

    for item in player.inventory:
        if isinstance(item, Lightsource):
            currentRoom.is_light = True
    for item in currentRoom.inventory:
        if isinstance(item, Lightsource):
            currentRoom.is_light = True

    if suppressRoomPrint:
        suppressRoomPrint = False
    elif currentRoom.is_light:
        print("------------------------------------------------")
        currentRoom.printName()
        currentRoom.printDesc()
        print()
        currentRoom.printInv()
        print()
    else:
        print("It's pitch black!")

    cmd = input("""================================================
What would you like to do, %s? """ % player.name)

    if cmd.upper() == 'N' or cmd.upper() == 'NORTH':
        if hasattr(currentRoom, 'n_to'):
            player.currentRoom = currentRoom.n_to
        else:
            printNoMove()
            suppressRoomPrint = True
    elif cmd.upper() == 'S' or cmd.upper() == 'SOUTH':
        if hasattr(currentRoom, 's_to'):
            player.currentRoom = currentRoom.s_to
        else:
            printNoMove()
            suppressRoomPrint = True
    elif cmd.upper() == 'E' or cmd.upper() == 'EAST':
        if hasattr(currentRoom, 'e_to'):
            player.currentRoom = currentRoom.e_to
        else:
            printNoMove()
            suppressRoomPrint = True
    elif cmd.upper() == 'W' or cmd.upper() == 'WEST':
        if hasattr(currentRoom, 'w_to'):
            player.currentRoom = currentRoom.w_to
        else:
            printNoMove()
            suppressRoomPrint = True
    elif cmd.upper() == 'INV' or cmd.upper() == 'I':
        player.printInv()
    elif "TAKE" in cmd.upper():
        isInInv = False
        for item in currentRoom.inventory:
            if cmd[5:] in item.name:
                isInInv = True

                if isinstance(item, Treasure):
                    treasureOnTake(item)
                    item.on_take(player, currentRoom)
                else:
                    item.on_take(player, currentRoom)
        if not isInInv:
            print("Sorry, %s, that item is not in this room." % player.name)
    elif "DROP" in cmd.upper():
        isInInv = False
        for item in player.inventory:
            if cmd[5:] in item.name:
                isInInv = True
                item.on_drop(player, currentRoom)
        if not isInInv:
            print("You are not carrying that item.")
    elif cmd.upper() == "SCORE":
        print("Your score: %s" % player.score)
    elif cmd.upper() == 'Q' or cmd.upper() == 'QUIT':
        print("\nThanks for playing.\n")
        break
    elif cmd.upper() == 'H' or cmd.upper() == 'HELP':
        print("""Commands:
    'n' or 'north' to move north
    's' or 'south' to move south
    'e' or 'east' to move east
    'w' or 'west' to move west
    'i' or 'inv' to look in inventory
    'score' for score
    'take <item>' to take
    'drop <item>' to drop
    'q' or 'quit' to quit
    'h' or 'help' for help""")
    else:
        print("That command is not valid.")