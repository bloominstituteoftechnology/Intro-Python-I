from room import Room
from player import Player
from item import Item
import os

# Declare all the rooms
items = {
    'sword':        Item("sword", """Metal bladed weapon used to destory monsters"""),
    'axe':          Item("axe", """A weapon that is used to cut heads off"""),
    'firestick':    Item("firestick", """Created by magic and burns enemy's alive"""),
    'pitch fork':   Item("pitch fork", """Used to poke multiple holes in enemies"""),
    'sickle':       Item("sickle", """A fast medal bladed weapon in the chape of a moon that is useful when fighting multiple monsters at once"""),
    'gun':          Item("gun", """ The gun carries 6 bullets but is an instant kill to enemies"""),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. """),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north.The smell of gold permeates the air. """),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers.The only exit is to the south. """),

    'dunegon': Room("Dungeon Hell", """You are in the worst place in the world and
    should be careful where you step!!! """ ),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['dungeon']
room['dungeon'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to room
room['outside'].inventory.append(item['sword'])
room['foyer'].inventory.append(item['axe'])
room['narrow'].inventory.append(item['firestick'])


# Main
print(room['outside'].s_to)
# Make a new player object that is currently in the 'outside' room.
player = Player('Mark', room['outside'])
direction = None
# Write a loop that:
while(True):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(
        '\n Your are currently here:', player.location.name,
        '\n Description:', player.location.description)
    direction = input('\nWhich way would you like to go?\n(N, E, S, W) pick one:').lower()
    player.move_to(direction)
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
