from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["Flashlight"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["Coins", "Sword"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["Rope"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["Gold", "Golden knife"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["Treasure box", "Gold", "Diamonds"]),
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
newPlayer = Player("Bob", room["outside"], [])
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

newInput = None

while newInput != "q":
    print(newPlayer.room.summary)
    print(f"Items in room: {newPlayer.room.items}")

    newInput = input("Give a one letter direction (NESW): \n \n \n")

    newInput = newInput.split(" ")

    if len(newInput) < 2:

        if newInput[0] is "n" or newInput[0] is "N":
            newPlayer.room = newPlayer.room.n_to
        if newInput[0] is "e" or newInput[0] is "E":
            newPlayer.room = newPlayer.room.e_to

        if newInput[0] is "s" or newInput[0] is "S":
            newPlayer.room = newPlayer.room.s_to

        if newInput[0] is "w" or newInput[0] is "W":
            newPlayer.room = newPlayer.room.w_to
        
        if newInput[0] is "i" or newInput[0] is "inventory" or newInput[0] is "I" or newInput[0] is "Inventory":
            print(f"Player inventory: {newPlayer.inventory}")

    if len(newInput) >= 2:
        if newInput[0] == "get" or newInput[0] == "take" or newInput[0] is "Get" or newInput[0] is "Take":
            newPlayer.inventory.append(newInput[1])
            newPlayer.room.items.remove(newInput[1])

        if newInput[0] == "drop" or newInput[0] == "remove" or newInput[0] is "Drop" or newInput[0] is "Remove":
            newPlayer.inventory.remove(newInput[1])
            newPlayer.room.items.append(newInput[1])
            