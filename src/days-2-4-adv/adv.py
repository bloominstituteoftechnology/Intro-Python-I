from room import Room
from player import Player
from item import Item, Treasure, BlznIt
from monster import Monster
import random
import time
# Declare all the rooms

monster = {
    'spider':   Monster("Big Creepy Spider", "Huge hairy legs that ooze a stick substance")
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [ BlznIt('Rock', 'Ouch! This rock is sharp, but useless.') ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [ Item('Sword', 'Looks strong, but feels weaker than a twig.')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [ Item('Health', 'This can be useful.')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [ Treasure('Amethyst', 'Looks expensive.', 100) ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [ Item('Ultima', 'So... So shiny, and made of a mystery metal.')]),
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

room['outside'].is_lit = True

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# players attribute is the room it is in.
player = Player('Alexis', room['outside'], [])

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

done = False
start = False
battle = False


while not done:

    if player.score >= 200:
        print("You win the game!")
        done = True

    while not start:
            print("\n", player.name, player.room.name, player.room.description)
            player.room.room_items()
            start = True
    choice = input("\nEnter a direction: n, s, e, or w. \nPress i to check inventory, or enter q to quit.\nType score to see your score. \nWhile in a room, you can press g to grab the item, or d to drop an item. ").lower()

    if choice != 'q' and choice != 'i' and choice != 'g' and choice != 'd' and choice != 'score':
        choice += '_to'
        if hasattr(player.room, choice):
            player.room = getattr(player.room, choice)
            if player.room.is_lit:
                print("\n You have entered the" ,player.room.name,",", player.room.description, "\n" )
                player.room.room_items()
            else:
                print("\nIt's pitch black\n")
            for i in player.items:
                if isinstance(i, BlznIt):
                    print("\n You have entered the" ,player.room.name,",", player.room.description, "\n" )
                    player.room.room_items()
        else:
            print("\n This way is not allowed! Go another direction! \n")

    elif choice == 'i':
        player.inv_check( player )
        battle_start = random.randint(0, 10)
        if battle_start <= 3:
            battle = True
        while battle:
            print("\nWhile checking your inventory, a huge monster appeared before you!\n")
            time.sleep(1)
            print("\n", monster['spider'].name, monster['spider'].description)
            time.sleep(2)
            print("... The monster killed you. Sorry for your loss.\n")
            battle = False
            choice = 'q'


    elif choice == 'g':
        grabbing = input("\n Which item would you like to grab? Type the name of the item to put in your inventory...\n")
        for i in player.room.items:
            if grabbing == i.name:
                i.on_grab( player )

    elif choice == 'd':
        print("Items that are in your inventory to drop...: \n")
        
        for item in player.items:
            print("  ", item)

        dropping = input("\n Which item would you like to drop? Type the name of the item to remove from your inventory...\n")
        for i in player.items:
            if dropping == i.name:
                if isinstance(i, BlznIt):
                    print("\nIt's not wise to drop your source of light!\n")
                    print("Dropping...")
                    player.room.items.append(i)
                    player.items.remove(i)
                elif not isinstance(i, BlznIt):
                    print("Dropping...")
                    player.room.items.append(i)
                    player.items.remove(i)

            else:
                print("\n This item is currently not in your inventory... \n")

    elif choice == 'score':
        print("\n You have a score of %d...\n " % player.score)
    if choice == "q":
        print("Game Over.")
        done = True


