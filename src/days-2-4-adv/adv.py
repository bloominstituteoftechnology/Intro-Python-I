from room import Room
from player import Player
from items import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     [Item("map", "map of the Location", 100)]),
 
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[Item("coin", "coin of the Treasure", 150)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
[Item("photo", "photo of the deceased owner", 100)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
[Item("backpack", "backpack belonging to other Adventurers", 300)]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
[Item("list", "list of different treasure spots left by the other adventurers", 500)]),
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
player = Player(room['outside'])
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
    inv = player
    print("\n")
    print("=====================================================")
    currentRoom.printName()
    currentRoom.printDesc()
    print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
    currentRoom.printItems()
    print("=====================================================")
    print("=====================================================")
    print("inventory: ")
    inv.menu()
    inv.playerScore()
    print("\n")
    print("What direction will you choose?")

    # items.menu()
    # print("\n")

    direction = input("--> ").lower().split(" ")

    if len(direction) > 1:
    
        if len(direction) > 1 and (direction[0] == "add"):
            itemToAdd = currentRoom.find(direction[1])
            if itemToAdd == None:
                print("No item by that name")
            else:
                pointsEarned = int(itemToAdd.pointsIn() / 1)
                player.score += pointsEarned
                player.add(itemToAdd)
                print(f"You have picked up {itemToAdd.name}, which held {pointsEarned} points")

        if len(direction) > 1 and (direction[0] == "remove"):
            print(player.items)
            itemToRemove = player.find(direction[1])
            if itemToRemove == None:
                print("No item to remove")
            else:
                player.removeItem(itemToRemove)
    else:

        if direction[0] == 'q':
            print("\nYour Journey has ended")
            break

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