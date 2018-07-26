from room import Room
from player import Player
from item import Item, Treasure

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("flashlight", "light up dar areas")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Treasure("sword", "fight enemies", "500 crowns")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("rope", "rope for climing or tying")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Treasure("Diamonds", "Valuable assets", "50 million crowns")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Treasure("Gold", "Valuable assets", "200 million crowns")]),
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
newPlayer = Player("Bob", room["outside"], [], 0)
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

    roomItems = []

    if len(newPlayer.room.items) != 0:
        for item in newPlayer.room.items:
            roomItems.append(item.name)
    
    print(f"Loot: {roomItems}")
    print(newPlayer.room.summary)

    newInput = input("Give a one letter direction (NESW): \n \n \n")
    newInput = newInput.lower()
    newInput = newInput.split(" ")

    if len(newInput) < 2:

        if newInput[0] == "n":
            newPlayer.room = newPlayer.room.n_to
        if newInput[0] == "e":
            newPlayer.room = newPlayer.room.e_to

        if newInput[0] == "s":
            newPlayer.room = newPlayer.room.s_to

        if newInput[0] == "w":
            newPlayer.room = newPlayer.room.w_to
        
        if newInput[0] == "i" or newInput[0] == "inventory":
            print(f"Player inventory: {newPlayer.inventory}")

        if newInput[0] == "score":
            print(f"Player score:  {newPlayer.score}")

    if len(newInput) >= 2:
        if newInput[0] == "get" or newInput[0] == "take":
            newPlayer.inventory.append(newInput[1])
            newPlayer.room.items.remove(newInput[1])

        if newInput[0] == "drop" or newInput[0] == "remove":
            newPlayer.inventory.remove(newInput[1])
            newPlayer.room.items.append(newInput[1])
            