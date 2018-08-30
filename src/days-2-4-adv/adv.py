from os import system, name
import random
from room import Room
from player import Player
# Declare all the rooms

suppressRoomPrint = False
validDirections = ["n", "s", "e", "w"]

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


def move_check(p_location):
    if p_location:
        system('cls')
        player.change_location(p_location)
        print(player.location.weaponDrop)

    else:
        print("\nCan't go that way!\n")

player = Player((input("What is your name: ")), room['outside'])


while True:
    inp = input("What would you like to do next: ")
    if inp == 'q':
        break
    elif inp == 'n':
        move_check(player.location.n_to)
    elif inp == 'e':
        move_check(player.location.e_to)
    elif inp == 's':
        move_check(player.location.s_to)
    elif inp == 'w':
        move_check(player.location.w_to)
    else:
        print('\nInvalid entry, please type n, e, s, w\n')
