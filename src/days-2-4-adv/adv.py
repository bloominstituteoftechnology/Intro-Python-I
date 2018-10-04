import os

from room import Room
from player import Player
from item import Item, Treasure

# Declare all the items

sword = Item("sword", "a steely blade of death")

cat = Item("cat", "a clever little creature")

hat = Item("hat", "a work of fine haberdashery")


# Declare all the treasures

ruby = Treasure("ruby", "a beautiful gem", 100)


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

# Setup Arrangement
player_starting_items = [hat]

room['outside'].add_item(sword)
room['foyer'].add_item(cat)

# Make a new player object that is currently in the 'outside' room.


p = Player(input("What is your name? "),
           room['outside'], player_starting_items)
os.system("clear")
print(f'Hello, {p.name} – your journey begins... {p.current_room}')


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


while True:
    cmds = input("enter a command-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            os.system("clear")
            break
        elif cmds[0] == "n" or cmds[0] == "s" or cmds[0] == "e" or cmds[0] == "w":
            os.system("clear")
            p.travel(cmds[0])
        elif cmds[0] == "i" or cmds[0] == "inventory":
            os.system("clear")
            p.print_inventory()
            print(
                f'Hello, {p.name} – you are currently in the {p.current_room}')
        elif cmds[0] == "status":
            os.system("clear")
            p.print_status()
            print(
                f'Hello, {p.name} – you are currently in the {p.current_room}')
        elif cmds[0] == "score":
            os.system("clear")
            p.print_score()
            print(
                f'Hello, {p.name} – you are currently in the {p.current_room}')
        else:
            os.system("clear")
            print("Invalid command, ye dog!")
    else:
        if cmds[0] == "take":
            item_to_take = p.current_room.find_item(" ".join(cmds[1:]))
            if item_to_take is not None:
                p.add_item(item_to_take)
                p.current_room.remove_item(item_to_take)
                print(f"You have picked up {item_to_take.name}")
            else:
                print("You do not see that item.")
        elif cmds[0] == "drop":
            p.drop_item(cmds[1:])
        else:
            print("I did not understand that command.")
