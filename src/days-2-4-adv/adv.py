import sys
import textwrap
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",),

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

name = str(input("What's your name?\n>>>"))

player = Player(name, room['outside'])

coins = Item("coins", "some valuable currency")
room['narrow'].items.append(coins)

sword = Item("sword", "a weapon to vanquish your foes")
player.inventory.append(sword)

print(f"Welcome to Adventure Game, {player.name}!\n")
print(f"You are in {player.location.name}.\n")
print(textwrap.fill(player.location.description, 70))
print("Please choose to continue...\n")
user = str(
    input("[N]orth  [S]outh  [E]ast  [W]est  [I]nventory  [Q]uit\n>>>")).strip().lower()

while not user == "q":
    command = user.split(" ")

    if len(command) == 2:
        if command[0] == "take" or command[0] == "get":
            if not player.location.items:
                print(
                    f"There is no {command[1]} here! In fact, this room is empty!\n")
            else:
                for i in player.location.items:
                    if i.name == command[1]:
                        player.location.items.remove(i)
                        player.inventory.append(i)
                        print(f"You picked up {i}!\n")
                    else:
                        print(f"There is no {command[1]} here!\n")
        elif command[0] == "drop":
            if not player.inventory:
                print(
                    f"There is no {command[1]} in your inventory! In fact, your inventory is empty!\n")
            else:
                for i in player.inventory:
                    if i.name == command[1]:
                        player.inventory.remove(i)
                        player.location.items.append(i)
                        print(f"You dropped {i}!\n")
                    else:
                        print(f"There is no {command[1]} in your inventory!\n")

    else:
        if user == "n":
            try:
                player.location = player.location.n_to
            except AttributeError:
                print("It's too dangerous to go here alone! Please try again.\n")
        elif user == "w":
            try:
                player.location = player.location.w_to
            except AttributeError:
                print("It's too dangerous to go here alone! Please try again.\n")
        elif user == "s":
            try:
                player.location = player.location.s_to
            except AttributeError:
                print("It's too dangerous to go here alone! Please try again.\n")
        elif user == "e":
            try:
                player.location = player.location.e_to
            except AttributeError:
                print("It's too dangerous to go here alone! Please try again.\n")
        elif user == "i":
            if len(player.inventory) == 0:
                print("You're not carrying any items!\n")
            else:
                print("You're carrying:\n")
                for i in player.inventory:
                    print(f" - {i}\n")

        else:
            print("Invalid selection. Please try again.\n")
    print(f"You are in {player.location.name}.\n")
    print(textwrap.fill(player.location.description, 70))
    print("\nPlease choose to continue...\n")
    user = str(
        input("[N]orth  [S]outh  [E]ast  [W]est  [I]nventory  [Q]uit\n>>>")).strip().lower()
