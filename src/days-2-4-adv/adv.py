import textwrap

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


# Declare all items

item = {
    'axe':  Item("Axe", """You may use the axe to cut down trees and brush."""),

    'bow':    Item("Bow and Arrows", """You may use the bow and arrow for hunting."""),

    'compass': Item("Compass", """Use the compass to find your way."""),

    'map':   Item("Map", """The map will guide you to the treasure."""),

    'keys': Item("Keys", """Find which key opens the treasure chest."""),

    'knife': Item("Knife", """The knife is a versatile tool for carving and self-defense."""),

    'scroll': Item("Scroll", """Read the ancient scroll to learn the secrets of the wizards."""),

    'iphone': Item("Iphone", """You now have an iphone, you probably don't want to play this game anymore."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].addItem(item['bow']) #passes a reference to save the value
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("\nWhat is your name? "), room["outside"])

print(f"Welcome, {player.name}\n")

valid_directions = {"n": "north", "s":"south", "e": "east", "w":"west"}

suppressRoomPrint = False

playing = True

while(playing):
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print(player.currentRoom)

    cmds = input("-> ").split(" ") # this allows us to separate commands

    if cmds[0] == "q":
        break

    elif cmds[0] == "n":
        if player.currentRoom.n_to is not None:
            player.currentRoom = player.currentRoom.n_to
        else:  
            print("Your chosen direction is not an option.")
    elif cmds[0] == "s":
        if player.currentRoom.s_to is not None:
            player.currentRoom = player.currentRoom.s_to
        else:  
            print("Your chosen direction is not an option.")
    elif cmds[0] == "e":
        if player.currentRoom.e_to is not None:
            player.currentRoom = player.currentRoom.e_to
        else:  
            print("Your chosen direction is not an option.")
    elif cmds[0] == "w":
        if player.currentRoom.w_to is not None:
            player.currentRoom = player.currentRoom.w_to
        else:  
            print("Your chosen direction is not an option.")

    # elif cmds[0] in valid_directions:
    #     player.travel(valid_directions[cmds[0]])

    elif cmds[0] == "look":
            player.look()

    elif len(cmds) >1 and (cmds[0] == "get" or cmds[0] == "take"):
        itemToGet = player.findItemByName(cmds[1])
        if itemToGet is not None:
            player.addItem(itemToGet)
            room.addItem(itemToGet)
        else:
            print("That item is not in this room.")

    elif len(cmds) >1 and cmds[0] == "drop":
        itemToDrop = player.findItemByName(cmds[1])
        if itemToGet is not None:
            player.removeItem(itemToGet)
            room.addItem(itemToGet)
        else:
            print(f"You have no {cmds[1]}.")
    
    elif cmds[0] == "inventory":
        print(player.getInventoryString())

    else:
        print("Command is not recognized.")



