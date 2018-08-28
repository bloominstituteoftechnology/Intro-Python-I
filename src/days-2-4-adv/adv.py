from os import system

from room import Room
from player import Player
from item import Item, Treasure, LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. But after some searching you find a key... """, False),

    'secret': Room("Secret Room", """With all of your knowledge and sheer fortitude
you have found a way into this room and found the treasure. And go east to exit this ride\n\nDon't forget to claim your prize!""", False)
}

# Create Items Dictionary

Items = {
    "Sword" : Item('Sword', 'Shiny'),
    "BronzeCoin" : Treasure('BronzeCoin', 'Bronze', '5'),
    "SilverCoin" : Treasure('SilverCoin', 'Silver', '10'),
    "GoldCoin" : Treasure('GoldCoin', 'Gold', '20'),
    "Lamp" : LightSource('Lamp', 'Illuminator'),
    "Key" : Item('Key', 'Secret Hidden Key'),
    "Pebble" : Item('Pebble', 'Yep, Just A Pebble')
}

# Adding Items to a Room

room['outside'].addItem(Items['Sword'])
room['foyer'].addItem(Items['BronzeCoin'])
room['narrow'].addItem(Items['SilverCoin'])
room['overlook'].addItem(Items['GoldCoin'])
room['outside'].addItem(Items['Lamp'])
room['treasure'].addItem(Items['Key'])
room['secret'].addItem(Items['Pebble'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].e_to = room['secret']

#
# Main
#



    # Single Word Commands

    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    if (len(instruction.split()) == 1):

    # - Quits the game (Quit)

        if (instruction == "Quit" or instruction == "East" and player.room.name == "Secret Room"):
            break

 
# - Display end game message

print("")
if (instruction == "Quit"):
    print("You quit and gained nothing\n")
    