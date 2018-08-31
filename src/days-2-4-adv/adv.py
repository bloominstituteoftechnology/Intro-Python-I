from os import system, name
import random

from room import Room
from item import Item
from item import Weapon
from item import LightSource
from item import Food
from player import Player

validDirections = ["n", "s", "e", "w"]

items = {
    'sword': Weapon("Sword", "A rusty but useful sword", 15),
    'refined_sword': Weapon("Sharpened Sword", "A big, brutish sword that has a red tint reflecting off the blade", 50),
    'torch': LightSource("Torch", "A torch that has been lit recently...", 20),
    'bread': Food("Bread", "A half eaten loaf", 2, 20),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items['bread']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items['sword']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items['torch']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers, except for one item. The only exit is to the south.""", items['refined_sword']),
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


def item_check(p_location):
    if p_location.itemDrop:
        inp = input("\nTheres an item in this room:\n{} \nWould you like to pick it up?: ".format(
            p_location.itemDrop))

        if inp == 'y' or inp == 'yes':
            player.addItem(p_location.itemDrop)
            p_location.itemDrop = None
        else:
            print("\nYou get ready to make your next move...\n")

    if p_location.droppedItem:
        inp = input("\nThe {} you dropped earlier is in here, did you want to pick it up?: ".format(
            p_location.droppedItem.name))
        if inp == 'y' or inp == 'yes':
            player.addItem(p_location.droppedItem)
            p_location.droppedItem = None
        else:
            print("\nYou get ready to make your next move...\n")

    elif not p_location.itemDrop and not p_location.droppedItem:
        print("\nRoom looks empty...\n")


def move_check(p_location):
    if p_location:
        system('cls')
        player.change_location(p_location)

    else:
        print("\nCan't go that way!\n")


def drop_item(item):
    item_grab = player.getItem(item)
    if item_grab:
        player.removeItem(item_grab)
        player.location.droppedItem = item_grab
    else:
        print("\nThat item isn't in your inventory\n")


system('cls')
player = Player((input("What is your name: ")), room['outside'])

while True:

    inputList = input(">>> ").split(" ")

    if inputList[0] == 'q':
        break
    elif inputList[0] == 'look':
        item_check(player.location)

    elif inputList[0] == 'inv':
        player.listInventory()

    elif inputList[0] == 'stats':
        player.playerInfo()

    elif inputList[0] == 'eat':
        if len(inputList) is 1:
            print('\nChoose an item to eat\n')
        elif player.getItem(inputList[1]) is not None:
            food = player.getItem(inputList[1])
            player.eatItem(food)
        else:
            print("\nThats not in inventory\n")

    elif inputList[0] == 'drop':
        if len(inputList) is 1:
            print('\nChoose an item to drop\n')
        else:
            drop_item(inputList[1])

    elif inputList[0] == 'move':
        if len(inputList) is 1:
            print('\nPick a location to move to\n')
        elif inputList[1] == 'n':
            move_check(player.location.n_to)
        elif inputList[1] == 'e':
            move_check(player.location.e_to)
        elif inputList[1] == 's':
            move_check(player.location.s_to)
        elif inputList[1] == 'w':
            move_check(player.location.w_to)
    else:
        print('\nInvalid entry, please type: move (n, e, s, w,) look, eat (item), drop (item), stats, inv, q to quit\n')
