from room import Room
from player import Player
from items import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     [Item("map", "map of the Location")]),
 
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[Item("coin", "coin of the Treasure")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
[Item("photo", "photo of the deceased owner")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
[Item("backpack", "backpack belonging to other Adventurers")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
[Item("list", "list of different treasure spots left by the other adventurers")]),
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

# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], [Item("map", "map of the Location")])
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

while True:

    currentRoom = player.currentRoom
    items = player.items

    print("\n")
    currentRoom.printName()
    currentRoom.printDesc()
    currentRoom.printItems()
    print("\n")

    direction = input("--> ").lower().split(" ")

    if len(direction) == 1:
        if direction[0] == 'q':
            print("\nYour Journey has ended")
            break

        elif len(direction) > 1 and (location[0] == "add"):
            itemToAdd = currentRoom.find(direction[1])
            if itemToAdd is not None:
                player.add(itemToAdd)
                print("added")
            else:
                print("No item by that name")
        elif len(direction) > 1 and (location[0] == "remove"):
            itemToRemove = player.items(direction[1])
            if itemToRemove is not None:
                player.remove(itemToRemove)
                print("removed")
        elif direction[0] == 'n':
            if not hasattr(player.currentRoom.n_to, 'name'):
                print('\n Dead End')
            else:
                player.currentRoom = player.currentRoom.n_to 

        elif direction[0] == 's':
            if not hasattr(player.currentRoom.s_to, 'name'):
                print('\n Dead End')
            else:
                player.currentRoom = player.currentRoom.s_to

        elif direction[0] == 'w':
            if not hasattr(player.currentRoom.w_to, 'name'):
                print('\n Dead End')
            else:
                player.currentRoom = player.currentRoom.w_to 

        elif direction[0] == 'e':
            if not hasattr(player.currentRoom.e_to, 'name'):
                print('\n Dead End')
            else:
                player.currentRoom = player.currentRoom.e_to        