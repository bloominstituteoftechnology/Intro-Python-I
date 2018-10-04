from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons"""),

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
player = Player(input("What is your name? "), room['outside'])
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

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print(player.currentRoom)
#THIS WILL TO SEE IF TRUE OR FALSE
#IF FALSE WILL PRINT THE CURRENT ROOM AND INFO
#IF TRUE WILL NOT PRINT ROOM AND INFO
    cmds = input("INPUT HERE:").split(" ")
    print(cmds)
#THIS WILL TAKE THE PLAYERS INPUT AFTER THE COLON
#AND THEN IT WILL SPLIT EACH INPUT AFTER SPACES INTO 
#INDIVIDUAL INPUTS
    if len(cmds) == 1:
        if cmds[0] == 'q':
            break
        elif cmds[0] == 'n':
            if player.currentRoom.n_to is not None:
                player.currentRoom = player.currentRoom.n_to
            else:
                print("You cannot move in that direction")
                suppressRoomPrint = True
#IF THERE IS ONLY 1 INPUT AND IT IS ONE OF THESE LETTERS
#IT WILL SET THE CURRENTROOM ATTR TO DIRECTION
#OR ELSE IT WILL PRINT THE YOU CANNOT MSG
        elif cmds[0] == 's':
            if player.currentRoom.s_to is not None:
                player.currentRoom = player.currentRoom.s_to
            else:
                print("You cannot move in that direction")
                suppressRoomPrint = True
        elif cmds[0] == 'w':
            if player.currentRoom.w_to is not None:
                player.currentRoom = player.currentRoom.w_to
            else:
                print("You cannot move in that direction")
                suppressRoomPrint = True
        elif cmds[0] == 'e':
            if player.currentRoom.e_to is not None:
                player.currentRoom = player.currentRoom.e_to
            else:
                print("You cannot move in that direction")
                suppressRoomPrint = True
        else:
            print("need valid command")
            suppressRoomPrint = True
    else:
        if cmds[0] == "look":
            if cmds[1] == "n":
                if player.currentRoom.n_to is not None:
                    print(f"\nin '{cmds[1]}' direction:", player.currentRoom.n_to)
                    suppressRoomPrint = True
                else:
                    print("There is nothing to look at")
                    suppressRoomPrint = True
            elif cmds[1] == "s":
                if player.currentRoom.s_to is not None:
                    print(f"\nin '{cmds[1]}' direction:", player.currentRoom.s_to)
                    suppressRoomPrint = True
                else:
                    print("There is nothing to look at")
                    suppressRoomPrint = True
            elif cmds[1] == "w":
                if player.currentRoom.w_to is not None:
                    print(f"\nin '{cmds[1]}' direction:", player.currentRoom.w_to)
                    suppressRoomPrint = True
                else:
                    print("There is nothing to look at")
                    suppressRoomPrint = True
            elif cmds[1] == "e":
                if player.currentRoom.e_to is not None:
                    print(f"\nin '{cmds[1]}' direction:", player.currentRoom.e_to)
                    suppressRoomPrint = True
                else:
                    print("There is nothing to look at")
                    suppressRoomPrint = True
        else:
            print("need valid commands")
            suppressRoomPrint = True
        
       
       
       
       
       