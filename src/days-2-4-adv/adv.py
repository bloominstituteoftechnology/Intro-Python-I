from room import Room
from player import Player
from item import Item

from colorama import Fore
from colorama import Style

import textwrap
import os
import sys
import time

# TODO: Abstract Rooms and Items to separate file
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

items = {
    'Sword': Item('Sword', 'A simple sword'),
    'Potion': Item('Potion', 'A health potion'),
    'Book': Item('Book', 'A dirty old book')
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

room['outside'].inventory = [items['Sword'], items['Book']]

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

# Global vars
player = Player()


def tprint(str, speed=0.05):
    for character in str:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


# Set the player's name
def set_init_player():
    os.system('clear')
    global player

    # Ask the player for the character name
    question_name = "\nEnter Your Character's Name\n"
    tprint(question_name)
    player_name = input("> ")

    if player_name == '':
        set_init_player()

    # Ask the player if the name is correct
    question_correct = f'\nAre you sure {Fore.BLUE}{player_name}{Style.RESET_ALL} is the right name? [y] ' \
                       f'yes or [n] no?\n'
    tprint(question_correct, 0.01)
    result = input("> ")

    # If the name is right, set the player and continue the game,
    # else, loop this function
    if result.lower() in ['y', 'yes']:
        player.name = player_name
        player.room = room['outside']
        player.game_over = False
    else:
        set_init_player()

    screen_message()
    main_game_loop()


# Gets the player's input and sets it in the global var user
# def player_input():
#     global player_inp
#     player_inp = input("\nWhat do you do?\n").lower()


# Display the screen message
def screen_message():
    # print(f'\n{player.room.name}')
    tprint(f'\n{player.room.name}\n')
    desc = textwrap.wrap(player.room.description, width=70)
    for element in desc:
        tprint(f'{element}\n')


# TODO: Simplify/Abstract this
# Check if the item exists in the Items dict, and if exists,
# Use the player pickup method to pickup the item, if not,
# return a message printing item not found
def item_exists(item):
    bl = False
    for itm in items:
        if itm == item.capitalize():
            bl = True
            return True

    if bl is False:
        return False

# TODO: Simplify/Pretty up the actions
def prompt():
    tprint('\nWhat do you do?\n')
    action = input("> ").split()
    acceptable_actions = ['quit', 'go', 'move', 'examine', 'pickup', 'drop', 'inventory', 'show inventory', 'get',
                          'look', 'look around', 'examine room']
    while action[0].lower() not in acceptable_actions:
        tprint('Unknown action, try again\n')
        action = input("> ").split()
    if action[0].lower() == 'quit':
        sys.exit
    elif action[0].lower() in ['move', 'go']:
        player.movedir(action[1].lower())
        screen_message()
    elif action[0].lower() == 'pickup':
        if item_exists(action[1].capitalize()):
            player.pickup_item(items[action[1].capitalize()])
        else:
            print(f'You looked for a {action[1]}, but did not find anything')
    elif action[0].lower() == 'drop':
        if item_exists(action[1].capitalize()):
            player.drop_item(items[action[1].capitalize()])
        else:
            print(f'You tried to drop {action[1]}, but it\'s not in your inventory')
    elif action[0].lower() in ['look', 'look around', 'examine room']:
        player.look_around()
    elif action[0].lower() in ['inventory', 'show inventory']:
        player.show_inventory()


def title_screen_selections():
    option = input('> ')
    if option.lower() == 'play':
        set_init_player()
    elif option.lower() == 'help':
        help_menu()
    elif option.lower() == 'quit':
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        tprint("Not a recognized input.\n")
        option = input('> ')
        if option.lower() == 'play':
            set_init_player()
        elif option.lower() == 'help':
            help_menu()
        elif option.lower() == 'quit':
            sys.exit()


def title_screen():
    os.system('clear')
    print(f'{Fore.GREEN}')
    print(f''.center(70, '#'))
    print(f'Tale of Tacronora'.center(70, ' '))
    print(f''.center(70, '#'))
    print(f'Play'.center(70, ' '))
    print(f'Help'.center(70, ' '))
    print(f'Quit'.center(70, ' '))
    print(f'MIT 2018'.center(70, ' '))
    print(f''.center(70, '#'))
    print(f'{Style.RESET_ALL}')
    title_screen_selections()


def help_menu():
    os.system('clear')
    print(f'{Fore.BLUE}')
    print(f''.center(70, '#'))
    print(f'Tale of Tacronora - Help'.center(70, ' '))
    print(f''.center(70, '#'))
    print(f'Type go/move <direction> to move direction'.center(70, ' '))
    print(f'Use "look/examine" to look around the room'.center(70, ' '))
    print(f'And last of all, have fun!'.center(70, ' '))
    print(f''.center(70, '#'))
    print(f'{Style.RESET_ALL}')
    title_screen_selections()


# START GAME
# Initialize the character input, display the room message and initialize the player's input
# These three functions run once then the while loop takes over


# set_init_player()
# screen_message()
# player_input()


def main_game_loop():
    while player.game_over is False:

        prompt()


title_screen()


# TODO: Get rid of this
# TODO: Simplify the main game logic
# While the input is not q, keep get game going
# while not player_inp == 'q':
#
#     # TODO: Abstract the command handler
#     # if player chooses North
#     if player_inp == 'n':
#         player.movedir('north')
#     elif player_inp == 's':
#         player.movedir('south')
#     elif player_inp == 'e':
#         player.movedir('east')
#     elif player_inp == 'w':
#         player.movedir('west')
#     elif player_inp == 'look around':
#         player.look_around()
#     elif player_inp[:6] == 'pickup':
#         if item_exists(player_inp[7:]):
#             player.pickup_item(items[player_inp[7:].capitalize()])
#         else:
#             print(f'You looked for a {player_inp[7:]}, but did not find anything')
#     elif player_inp[:4] == 'drop':
#         if item_exists(player_inp[5:]):
#             player.drop_item(items[player_inp[5:].capitalize()])
#         else:
#             print(f"{player_inp[5:]} is not in inventory")
#     elif player_inp == 'inventory':
#         player.show_inventory()
#     else:
#         print("Invalid selection. Please try again.\n")
#
#     screen_message()
#     player_input()
