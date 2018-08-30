from room import Room
from player import Player
from items import Items, Food, Treasure, LightSource, Weapon
import os
import sys
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False, True),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),
}

# Declare all the items
item_dict = {
    'apple': Food('apple', 'a small to medium-sized conic apple', 'food', 1, 10),
    'bread': Food('bread', 'a slice of bread', 'food', 1, 10),
    'ring': Treasure('ring', 'a silver ring', 'treasure', 1, 50),
    'lamp': LightSource('lamp', 'a lamp', 'light source', 1, 50),
    'necklace': Treasure('necklace', 'a silver necklace', 'treasure', 1, 50),
    'bracelet': Treasure('bracelet', 'a silver bracelet', 'treasure', 1, 50),
    'largeTreasureChest': Treasure('bracelet', 'a large treasure chest', 'treasure', 1, 500),
    'sword': Weapon('sword', 'a large ninja katana', 'weapon', 10, 10),
    'knife': Weapon('knife', 'a rusty knife', 'weapon', 10, 7)
    # 'shield': None,
    # 'helmet': None,
    # 'boots': None
}

"""where add stuff to the rooms"""
# add an apple to the outside room
# room['outside'].take('apple')
room['outside'].take(item_dict['apple'].name)
room['outside'].take(item_dict['apple'].name)
# room['outside'].take(item_dict['apple'].name)
room['outside'].take(item_dict['bread'].name)
room['outside'].take(item_dict['ring'].name)
room['foyer'].take(item_dict['sword'].name)
room['overlook'].take(item_dict['lamp'].name)
room['overlook'].take(item_dict['necklace'].name)
room['narrow'].take(item_dict['bracelet'].name)
room['treasure'].take(item_dict['largeTreasureChest'].name)


# Link rooms together
room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
monster = Player('Big Monster', 'narrow')
monster.take('knife')

# set up some helper functions


def checkInventory(item):
    inv = player.getInventory()
    if (inv.keys()):
        for key in inv:
            if key == item:
                return True
    return False


def battle(player, monster):
    print("\n\nYou've confronted a monster")
    while player.health > 0:
        action = input('Choose your action: ')
        if action == 'attack':
            player.attack(item_dict['sword'], monster)
            print("MONSTER HEALTH {}".format(monster.health))
            if monster.health < 1:
                print("You have vanquished the monster!!!")
                room[player.location].is_occupied = False
                return True
            monster.attack(item_dict['sword'], player)
            print("PLAYER HEALTH {}".format(player.health))

        elif action == 'q':
            break
    print("You have died:(")
    return False


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


# CLEAR SCREEN
os.system('cls') if sys.platform.startswith('win') else os.system('clear')
print("Welcome to the grand adventure!!  Press 'h' at any time for help.\n\n")
player_name = input("\nEnter your name: ")
player = Player(player_name, 'outside')

while True:
    # what player sees in the room
    # isinstance(variable, LightSource)
    if room[player.location].is_light or checkInventory('lamp'):
        if (room[player.location].is_occupied):
            battleResults = battle(player, monster)
            if not battleResults:
                print("Game over!")
                break
        print("\nYou are at {}.\n{}.".format(
            room[player.location].name, room[player.location].description))
        if len(room[player.location].inventory) > 0:
            print("Items in the room:")
            for key in room[player.location].inventory:
                if room[player.location].inventory[key]:
                    print("\t{} {}".format(
                        room[player.location].inventory[key], key))
                else:
                    print("\tNothing to take here.\n")
    else:
        print("You can't even see the hand in front of your face!")
    # shows items in the room, if there are any
    # input
    inp=input("\nEnter a command: ")

    if inp == 'q' or inp == 'quit':
        print("Thanks for playing!\n")
        break
    elif inp == 'n' or inp == "north":
        try:
            if (room[player.location].n_to):
                player.location=room[player.location].n_to
        except:
            print("Can't continue north\n")
    elif inp == 's' or inp == "south":
        try:
            if (room[player.location].s_to):
                player.location=room[player.location].s_to
        except:
            print("Can't continue south\n")
    elif inp == 'e' or inp == "east":
        try:
            if (room[player.location].e_to):
                player.location=room[player.location].e_to
        except:
            print("Can't continue east\n")
    elif inp == 'w' or inp == "west":
        try:
            if (room[player.location].w_to):
                player.location=room[player.location].w_to
        except:
            print("Can't continue west\n")
    elif inp == 'exits':
        exits='You can exit: '
        try:
            if (room[player.location].n_to):
                exits += "n, "
        except:
            pass
        try:
            if (room[player.location].e_to):
                exits += "e, "
        except:
            pass
        try:
            if (room[player.location].w_to):
                exits += "w, "
        except:
            pass
        try:
            if (room[player.location].s_to):
                exits += "s, "
        except:
            pass
        # print the exits, minus the ", "
        print("{}\n".format(exits[:-2]))
    # PLAYER ACTIONS
    elif inp == "l" or inp == 'look':
        pass
    elif inp.startswith('take') or inp.startswith('get'):
        if (room[player.location].is_light or checkInventory('lamp')):
            try:
                item=inp.split(' ')[1]
                # check to see if the item is in the room
                if (room[player.location].drop(item)):
                    # item is in the room, so player can take it
                    player.take(item)
                    item_dict[item].on_take(player)
                elif item == '':
                    print("You must enter something to take.\n")
                else:
                    print("There is no '{}' for you take!".format(item))
            except:
                print("You must enter something to take.\n")
        else:
            print("Good luck finding that in the dark!")
    elif inp.startswith('drop'):
        try:
            item=inp.split(' ')[1]
            # check to see if the item is in player inventory
            if (player.drop(item)):
                print('Dropping {}\n'.format(item))
                room[player.location].take(item)
        except:
            print("You must enter something to drop.\n")
    elif inp.startswith('eat'):
        try:
            ateItem=False
            inv=player.getInventory()
            item=inp.split(' ')[1]
            if (inv.keys()):
                for key in inv:
                    if key == item:
                        print('Eating {}\n'.format(item))
                        player.eat(item_dict[item])
                        ateItem=True
                        break
            if (not ateItem):
                print("You don't have a {} to eat!\n".format(item))
        except:
            print("You cannot eat that!")
    elif inp == 'i' or inp == "inventory":
        inv=player.getInventory()
        if (inv.keys()):
            print("your stuff:\n")
            for key in inv:
                print("\t{} {}".format(inv[key], key))
            print()
        else:
            print("You aren't carrying anything\n")
    elif inp == 'score':
        # print('{}\n'.format(player.getScore()))
        player.getScore()
    elif inp == 'status':
        player.getStatus()
    elif inp == "h" or inp == "help":
        print("\nCommands: n)orth, e)ast, w)est, s)outh, l)ook, take, get, drop, score, status, exits, i)nventory, q)uit, h)elp\n")
    else:
        print("I don't know that command")
