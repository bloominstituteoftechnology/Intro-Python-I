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
rock = Item('rock', 'I am a rock')
suppressRoomPrint = False
player = Player(input("What is your name? "), room['outside'], [rock])
while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print(player.currentRoom)
    commands = input("-> ").split(" ")
    if len(commands) == 1:
        if commands[0] == "q":
            break
        elif commands[0] == "n":
            if player.currentRoom.n_to is not None:
                player.currentRoom = player.currentRoom.n_to
                
            else:
                print("You cannot move in that direction")
                suppressRoomPrint = True
        elif commands[0] == "s":
            if player.currentRoom.s_to is not None:
                player.currentRoom = player.currentRoom.s_to
                
            else:
                print("You cannot move in that direction")
                suppressRoomPrint = True
        elif commands[0] == "e":
            if player.currentRoom.e_to is not None:
                player.currentRoom = player.currentRoom.e_to
                
            else:
                print("You cannot move in that direction")
                suppressRoomPrint = True
        elif commands[0] == "w":
            if player.currentRoom.w_to is not None:
                player.currentRoom = player.currentRoom.w_to
                
            else:
                print("You cannot move in that direction")
                suppressRoomPrint = True
        elif commands[0] == "i" or commands[0] == "inventory":
            player.printInventory()
    else:
        if commands[0] == "look":
            if commands[1] == "n" or commands[1] == "s" or commands[1] == "e" or commands[1] == "w":
                player.look(commands[1])
            else:
                print("I did not understand that command")
