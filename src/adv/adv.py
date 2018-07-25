from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        [Item("Map", "Looks like a map for the cave. It looks heavily faded."), Item("BrokenSword", "The tip of the sword is broken. It can probably still slay some beasts.")],
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        [],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [],
    ),
}


# Link rooms together
# Player movement direction: N, W, S ,E

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room["outside"])

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


def searchDirect(currentRoom, direction):
    search = direction + "_to"
    if hasattr(currentRoom, search):
        return getattr(currentRoom, search)
    else:
        print("\n" + "Invalid path. Try different direction.")
        return currentRoom


playerExit = False

while playerExit != True:
    # print current room and description
    print("\nCurrent room: {}".format(player.currentRoom.name))
    for line in textwrap.wrap(player.currentRoom.descript):
        print(line)

    # take user input
    # convert to lowercase
    userInput = input("Player> ").strip().lower()

    # quit, search direction, or give error
    if userInput == "q" or userInput == "exit" or userInput == "quit":
        print("\nFarewell, adventurer.\n")
        playerExit = True
    # shows all available actions
    elif userInput == "action" or userInput == "actions" or userInput == "help":
        print("\navailable actions: n, w, s, e, get, item")
    # direction
    elif userInput in {"n", "w", "s", "e"}:
        player.currentRoom = searchDirect(player.currentRoom, userInput)
    # list all items
    elif userInput == "item" or userInput == "items":
        if len(player.currentRoom.itemList) != 0:
            for eachItem in player.currentRoom.itemList:
                print('\nitem:', eachItem.name)
                print(eachItem.descript)
        else:
            print("\nNo items found.")
    else:
        print("Invalid command.")
