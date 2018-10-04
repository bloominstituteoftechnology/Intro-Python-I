from room import Room
from item import Item
from item import LightSource
from item import Treasure
from player import Player

# Declare all the rooms
item = {
    'pickaxe': Item("pickaxe", "A tool used for mining"),
    'lamp': LightSource("lamp", "An old kerosene lantern"),
    'helmet': Item("helmet", "A sturdy helmet"),
    'stone': Item("stone", "a fist sized stone"),
    'nugget': Treasure("nugget", "a golden nugget", 500),
    'coins': Treasure("coins", "bright and shiny golden coins!", 800),
    'rubies': Treasure("rubies", "Bright and shining red rubies!", 1000)
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item["pickaxe"]], False),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item["lamp"], item["helmet"], item["nugget"]], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item["stone"]], False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item["coins"]], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item["rubies"], item['rubies']], False),
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

valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

player = Player(input("What is your name? "), room['outside'])
print(player.currentRoom)

while True:
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        elif cmds[0] == "inventory" or cmds[0] == "i":
            player.checkInventory()
        elif cmds[0] == "score":
            player.checkScore()
        else:
            print("I did not understand that command.")
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "take" or cmds[0] == "get":
            takenItem = player.currentRoom.removeItem(cmds[1])
            player.takeItem(takenItem)
        elif cmds[0] == "drop":
            player.currentRoom.addItem(player.dropItem(cmds[1]))
        else:
            print("I did not understand that command.")