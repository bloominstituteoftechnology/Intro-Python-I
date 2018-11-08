import textwrap
import os
import sys
import time

from player import Player
from rooms import room
from rooms import items
from jobs import jobs

from colorama import Fore
from colorama import Style

# TODO: Abstract Rooms and Items to separate file
# Declare all the rooms


# Global vars
player = Player()


# Displays each character of the string in intervals, produces
# a typewriter effect
def tprint(string, speed=0.05):
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


# Display the title screen
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


# Display the help screen
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


# The menu selections of the title screen
def title_screen_selections():
    option = input('> ')

    # Display the menu commands
    if option.lower() == 'play':
        set_init_player()
    elif option.lower() == 'help':
        help_menu()
    elif option.lower() == 'quit':
        sys.exit()
    elif option.lower() == 'back':
        title_screen()

    # Keep the menu going if not a recognized input
    while option.lower() not in ['play', 'help', 'quit']:
        tprint("Not a recognized input.\n")
        title_screen_selections()


# Setup the Player
def set_init_player():
    os.system('clear')
    global player

    # Ask the player for the character name
    question_name = "\nEnter Your Character's Name\n"
    tprint(question_name)
    player_name = input("> ")

    if player_name == '':
        set_init_player()

    # Ask the player for their preferred class
    question_class = "\nPick your class:\n" \
                     "Warrior\n" \
                     "Mage\n" \
                     "Thief\n"

    tprint(question_class, 0.05)
    job = input("> ")
    all_jobs = ['warrior', 'mage', 'thief']
    if job in all_jobs:
        player.job = jobs[job.capitalize()]
    while job not in all_jobs:
        job = input("> ")
        if job in all_jobs:
            player.job = jobs[job.capitalize()]

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

    room_message()
    main_game_loop()


# Display the room message
def room_message():
    os.system('clear')
    tprint(f'\n{player.room.name}\n', 0.03)
    desc = textwrap.wrap(player.room.description, width=70)
    for element in desc:
        tprint(f'{element}\n', 0.03)


# TODO: Simplify/Abstract this
""" Check if the item exists in the Items dict, and if exists,
    Use the player pickup method to pickup the item, if not,
    return a message printing item not found """


def item_exists(item):
    bl = False
    for itm in items:
        if itm == item.capitalize():
            bl = True
            return True

    if bl is False:
        return False


# TODO: Simplify/Pretty up the actions
""" Where the action happens
    Ask's the player what to do next and
    then handles the command that the player
    has given it.
"""


def prompt():
    tprint('\nWhat do you do?\n')
    action = input("> ").split()
    acceptable_actions = ['quit', 'go', 'move', 'examine', 'pickup', 'drop', 'inventory', 'get',
                          'look', 'look around', 'examine room']
    while action[0].lower() not in acceptable_actions:
        tprint('Unknown action, try again\n')
        action = input("> ").split()
    if action[0].lower() == 'quit':
        sys.exit()
    elif action[0].lower() in ['move', 'go']:
        player.movedir(action[1].lower())
        room_message()
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
    elif action[0].lower() in ['inventory']:
        player.player_info()
    elif action[0].lower() in ['equip']:
        if item_exists(action[1].capitalize()):
            player.equip_weapon(action[1])
        else:
            print(f'You tried to equip {action[1]}, but it\'s not in your inventory')


# Keep the game going until the player gets a game over
def main_game_loop():
    while player.game_over is False:
        prompt()


# Start the game
title_screen()
