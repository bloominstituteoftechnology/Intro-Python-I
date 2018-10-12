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

rock = Item("Rock", "This is a rock")

room['outside'].addItem(rock)

room['outside'].light = True
room['foyer'].light = True

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

validDirections = {"n": "n", "s": "s", "e": "e", "w": "w", "north": "n", "south": "s", "east": "e", "west": "w"}

player = Player(input("What is your name?"), room['outside'])
print(player.currentRoom)

while True:
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in validDirections:
            player.travel(validDirections[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        elif cmds[0] == "i" or cmds[0] == "inventory":
            player.printInventory()
        else:
            print("I did not understand that command.")    
    else:
        if cmds[0] == "look":
            if cmds[1] in validDirections:
                player.look(validDirections[cmds[1]])
        elif cmds[0] == "take":
            itemToTake = player.currentRoom.findItembyName(cmds[1])
            if itemToTake is not None:
                player.addItem(itemToTake)
                player.currentRoom.removeItem(itemToTake)
            else:
                print("You do not see that item.")
        elif cmds[0] == "drop":
            itemToTake = player.findItembyName(cmds[1])
            if itemToTake is not None:
                player.removeItem(itemToTake)
                player.currentRoom.addItem(itemToTake)
            else:
                print("You are not holding that item.")
        else:
            print("I did not understand that command.")  