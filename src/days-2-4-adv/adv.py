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
    'axe':  Item("Axe", """You may use the axe to cut down trees and brush.""", 20),

    'bow':    Item("Bow", """You may use the bow and arrow for hunting.""", 10),

    'compass': Item("Compass", """Use the compass to find your way.""", 30),

    'map':   Item("Map", """The map will guide you to the treasure.""", 40),

    'keys': Item("Keys", """Find which key opens the treasure chest.""", 10),

    'knife': Item("Knife", """The knife is a versatile tool for carving and self-defense.""", 20),

    'scroll': Item("Scroll", """Read the ancient scroll to learn the secrets of the wizards.""", 30),

    'iphone': Item("Iphone", """You now have an iphone, you probably don't want to play this game anymore.""", 50),
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


#Add some items to the rooms

room['outside'].addItem(item['bow']) 
room['foyer'].addItem(item['axe']) 
room['foyer'].addItem(item['map']) 
room['overlook'].addItem(item['scroll']) 
room['overlook'].addItem(item['keys']) 
room['narrow'].addItem(item['knife']) 
room['narrow'].addItem(item['compass']) 
room['treasure'].addItem(item['iphone']) 


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("\nWhat is your name? "), room["outside"])

print(f"Welcome, {player.name}\n")

valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w"}

print(player.currentRoom)

playing = True

while(playing):

    cmds = input("-> ").split(" ") # this allows us to separate commands

    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        elif cmds[0] == "i" or cmds[0] == "inventory":
            player.printInventory()
        elif cmds[0] == "status":
            player.printStatus()
        else:
            print("That command is not recognized by this program.")

    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "take" or cmds[0] == "get":
            itemToTake = player.currentRoom.findItemByName(" ".join(cmds[1:]))
            if itemToTake is not None:
                player.addItem(itemToTake)
                player.tallyScore(itemToTake)
                player.currentRoom.removeItem(itemToTake)
                print(f"You have collected the {itemToTake.name}")
            else:
                print("That item is not here.")
        elif cmds[0] == "drop":
            player.dropItem(cmds[1:])
        else:
            print("Command is not recognized.")



