import os
from room import Room
from player import Player
from item import Item

# Declare the items
items = {
    'jewel': Item("jewel", "glittering jewel. It is a deep red hue and seems to pulse to an unheard rhythm."),
    'locket': Item("locket", "battered silver locket. Opening it reveals a faded photograph of two lovers."),
    'dagger': Item("dagger", "thin dagger. It looks like it could be used to stab somebody.")
}

# Declare the rooms
rooms = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", [items['dagger']]),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", [items['locket']]),
    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),
    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! The only exit is to the south.", [items['jewel']]),
}

# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Player input handling methods
#

def process_command(command):
    command = command.split(" ")
    commands = {
        "n": move,
        "w": move,
        "e": move,
        "s": move,
        "move": move,
        "get": take_item,
        "take": take_item,
        "q": quit_game,
        "quit": quit_game,
        "i": inventory,
        "inventory": inventory,
        "drop": drop_item
    }
    if command[0] in commands:
        commands[command[0]](command)

def move(command):
    room = player.current_room
    directions = {
        "n": room.n_to,
        "north": room.n_to,
        "e": room.e_to,
        "east": room.e_to,
        "s": room.s_to,
        "south": room.s_to,
        "w": room.w_to,
        "west": room.w_to
    }
    dir = command[0] if len(command) is 1 else command[1]
    if dir in directions and directions[dir]:
        player.current_room = directions[dir]
    else:
        print("You cannot go that way")

def quit_game(command):
    print("Thanks for playing!")
    exit()

def take_item(command):
    item = items.get(command[1])
    if item and item in player.current_room.items:
        player.current_room.items.remove(item)
        player.inventory.append(item)
    else:
        print("There are no {}s here to take".format(command[1]))

def drop_item(command):
    item = items.get(command[1])
    if item and item in player.inventory:
        player.inventory.remove(item)
        player.current_room.items.append(item)
    else:
        print("You have no {}s to drop".format(command[1]))

def inventory(command):
    print("{} is carrying:".format(player.playerName))
    for item in player.inventory:
        print("A {}".format(item))

#
# Main loop
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Leon", rooms['outside'])

while True:
    os.system('cls')
    print(player)
    print(player.current_room.description)
    for item in player.current_room.items:
        print("You see a {}".format(item))

    command = input("\nCommands:\nmove (north, east, south, west)\ntake item\ndrop item\ninventory\nquit\nEnter choice: ")
    process_command(command)