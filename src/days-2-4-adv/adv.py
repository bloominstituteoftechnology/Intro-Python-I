from room import Room
from player import Player
from item import Item

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


# Items
rock = Item("Rock", "This is a rock. ")
rope = Item("Rope", "About 6' long. ")
lighter = Item("Lighter", "Zippo, coool ")



room['outside'].addItem(rock)


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

suppressRoomPrint = False

print("\n ================= Welcome to Python Adventure ================= ")
name = input("\nPlease enter your name: ")
player = Player(name, room['outside'])
print (f"\nWelcome, {player.name}!\n\n  *Enter h at any time to display the help menu\n\nYour current location is:")

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print (f"\n  {player.location.title}\n    {player.location.description}\n")
    inputList = input("What is your command: ").split(" ")
    if inputList[0] == "q":
        break
    if inputList[0] == "h":
        print ("\nHere's a helpful list of controls:\n\nn - move north\ns - move south\ne - move east\nw- move west")
    elif inputList[0] == "l":
        suppressRoomPrint = True
        print (f"\n {player.location.items}\n")
    elif inputList[0] == "i":
        suppressRoomPrint = True
        print (f"\n {player.items}\n")
    elif len(inputList) > 1 and (inputList[0] == "get" or inputList[0] == "take"):
        for item in player.location.items:
            player.items.append(item)
            player.location.items.remove(item)
    elif inputList[0] == "n" or inputList[0] == "s" or inputList[0] == "w" or inputList[0] == "e":
        newRoom = player.location.getRoomInDirection(inputList[0])
        if newRoom == None:
            print ("\nYou cannot move in that direction\n")
            suppressRoomPrint = True
        else:
            player.change_location(newRoom)
