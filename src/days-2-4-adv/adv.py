from room import Room
from player import Player
from item import Item, Treasure, LightSource

# Declare all the rooms

room = {
    'outside':  
        Room("Outside Cave Entrance","North of you, the cave mount beckons",
        [Item("STICK","It's a stick and it's awesome!"),
        LightSource("LAMP", "A kerosene lamp that lights up the immediate area")], 
        True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty 
    passages run north and east.""", 
    [Treasure("COINS", "It's money!", 10, False),], False),


    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm.""", 
    [Treasure("Locket", "A precious keepsake obviously dropped by a previous adventurer.", 200, False)], True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air.""", [], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south.""", 
    [Treasure("Golden Chest", "A fairly large chest made of gold.", 1337, False)], False),
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
player = Player(input("What is your name adventurer? => "),room["outside"], [], 0)
print("-----------------------------------------------------")
print(player.currentRoom)
print("-----------------------------------------------------")
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
    cmds = input(f"What would you like to do {player.name}? => ").upper().split(" ")
    if len(cmds) == 1:
        if cmds[0] in validDirections:
            player.travel(validDirections[cmds[0]])
        elif cmds[0] == "LOOK":
            player.look()
        elif cmds[0] == "INV" or cmds[0] == "I":
            print("\n-----------------------------------------------------")
            print(f"\n    This is what you have in your inventory: ")
            if len(player.items) > 0:
                for item in player.items:
                    print(f"\n    {item.name}")
                    print("\n-----------------------------------------------------")
            else:
                print("\n    Your inventory is empty.")
                print("\n-----------------------------------------------------")
        elif cmds[0] == "SCORE":
            print(f"    {player.name}'s current score is: {player.score} ")
        elif cmds[0] == "Q" or cmds[0] == "QUIT":
            break
        else:
            print("\n-----------------------------------------------------")
            print("\n    That doesn't work please try a different command!")
            print("\n-----------------------------------------------------")
    else:
        if cmds[0] == "LOOK":
            if cmds[1] in validDirections:
                player.look(validDirections[cmds[1]])
        elif cmds[0] == "TAKE":
            for item in player.currentRoom.items:
                if cmds[1] in item.name:
                    item.takeItem(player)
                    print("\n-----------------------------------------------------")
                    print(f"\n    You have taken the {cmds[1]}!")
                    print("\n-----------------------------------------------------")
        elif cmds[0] == "DROP":
            for item in player.items:
                if cmds[1] in item.name:
                    item.dropItem(player)
                    print("\n-----------------------------------------------------")
                    print(f"\n    You have dropped the {cmds[1]}!")
                    print("\n---------------------------------------------------")
        else:
            print("That doesn't work please try a different command!")