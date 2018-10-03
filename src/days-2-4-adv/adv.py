from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                [Item("STICK")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),


    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
player = Player(input("What is your name? => "),room["outside"], [])
print(player.currentRoom)
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

validDirections = {"N": "N", "NORTH": "N", "S": "S", "SOUTH": "S", "E": "E", "EAST": "E", "W": "W", "WEST": "W"}

while True: 
    cmds = input("What would you like to do? => ").upper().split(" ")
    if len(cmds) == 1:
        if cmds[0] in validDirections:
            player.travel(validDirections[cmds[0]])
        elif cmds[0] == "LOOK":
            player.look()
        elif cmds[0] == "INV":
            print(f"This is what you have in your inventory: ")
            if len(player.items) > 0:
                for item in player.items:
                    print(item.name)
            else:
                print("Your inventory is empty.")
        elif cmds[0] == "Q" or cmds[0] == "QUIT":
            break
        else:
            print("That doesn't work please try a different command!")
            print('\n')
    else:
        if cmds[0] == "LOOK":
            if cmds[1] in validDirections:
                player.look(validDirections[cmds[1]])
        elif cmds[0] == "TAKE":
            for item in player.currentRoom.items:
                if cmds[1] in item.name:
                    item.takeItem(player)
                    print(f"You have taken {cmds[1]}!\n")
        elif cmds[0] == "DROP":
            for item in player.items:
                if cmds[1] in item.name:
                    item.dropItem(player)
                    print(f"You have dropped {cmds[1]}!\n")
        else:
            print("That doesn't work please try a different command!")
