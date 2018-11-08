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
    print(f''.center(75, '#'))
    print(f'Tale of Tacronora'.center(75, ' '))
    print(f''.center(75, '#'))
    print(f'Play'.center(75, ' '))
    print(f'Help'.center(75, ' '))
    print(f'Quit'.center(75, ' '))
    print(f'Copyright Jeremy Boggs MIT 2018'.center(75, ' '))
    print(f''.center(75, '#'))
    print(f'{Style.RESET_ALL}')
    title_screen_selections()


# Display the help screen
def help_menu():
    os.system('clear')
    print(f'{Fore.BLUE}')
    print(f''.center(75, '#'))
    print(f'Tale of Tacronora - Help'.center(75, ' '))
    print(f''.center(75, '#'))
    print(f'Type go/move <direction> to move direction'.center(75, ' '))
    print(f'Use "look/examine" to look around the room'.center(75, ' '))
    print(f'And last of all, have fun!'.center(75, ' '))
    print(f''.center(75, '#'))
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
        tprint('Play again!\n', 0.03)
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
    question_name = "\n Enter Your Character's Name\n"
    tprint(question_name)
    player_name = input("> ")

    if player_name == '':
        set_init_player()

    # TODO: Refactor the next two questions to be DRY

    # Ask the player's gender
    question_gender = '\n Are you male or female?\n'
    os.system('clear')
    tprint(question_gender)

    player_gender = input("> ")
    genders = ['male', 'female']

    if player_gender.lower() in genders:
        player.sex = player_gender.capitalize()
    while player_gender.lower() not in genders:
        player_gender = input("> ")
        if player_gender.lower() in genders:
            player.sex = player_gender.capitalize()

    # Ask the player for their preferred class
    question_class = "\n Pick your class:\n" \
                     " Warrior\n" \
                     " Mage\n" \
                     " Thief\n"

    os.system('clear')
    tprint(question_class, 0.05)

    job = input("> ")
    all_jobs = ['warrior', 'mage', 'thief']

    if job.lower() in all_jobs:
        player.job = jobs[job.capitalize()]
    while job.lower() not in all_jobs:
        job = input("> ")
        if job in all_jobs:
            player.job = jobs[job.capitalize()]

    # Ask the player if the name is correct
    question_correct = f'\n {Fore.BLUE}{player_name.title()}{Style.RESET_ALL}, {Fore.BLUE}{player.sex}{Style.RESET_ALL}, ' \
                       f'{Fore.BLUE}{player.job.name}{Style.RESET_ALL} is correct? [y] ' \
                       f'yes or [n] no?\n'
    os.system('clear')
    tprint(question_correct, 0.03)
    result = input("> ")

    # If the name is right, set the player and continue the game,
    # else, loop this function
    if result.lower() in ['y', 'yes']:
        player.name = player_name.title()
        player.room = room['outside']
        player.weapon = items['EmptyW']
        player.armour = items['EmptyA']
        player.shield = items['EmptyS']
        player.game_over = False
    else:
        set_init_player()

    room_message()
    main_game_loop()


# Display the room message
def room_message():
    os.system('clear')
    tprint(f'\n {player.room.name}\n', 0.03)
    desc = textwrap.wrap(player.room.description, width=70)
    for element in desc:
        tprint(f' {element}\n', 0.03)


# TODO: Simplify/Abstract this
""" Check if the item exists in the Items dict, and if exists,
    Use the player pickup method to pickup the item, if not,
    return a message printing item not found """


def item_exists(item):
    bl = False
    for itm in items:
        if itm == item.title():
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
    tprint(f'\n {Fore.CYAN}What do you do?{Style.RESET_ALL}', 0.03)

    # Input for the action to be taken - split into list
    action = input(" > ").split()
    combined_action = ' '.join(action[:2])

    # Complete list of all the actions to be done
    valid_actions = ['quit', 'character', 'char', 'i', 'inventory', 'get', 'take', 'pickup', 'drop', 'go', 'move',
                     'look around', 'examine room', 'equip', 'unequip']

    # If the action is not a valid action
    while action[0].lower() not in valid_actions:
        # Break the loop if combined_action is in it
        # This makes the parsing of double-texted actions workable
        if combined_action in valid_actions:
            break

        tprint('Unknown action, try again\n')
        prompt()

    if combined_action.lower() in ['look around', 'examine room']:
        player.look_around()

    if action[0].lower() == 'quit':
        tprint('Play again!\n', 0.03)
        os.system('clear')
        sys.exit()

    elif action[0].lower() in ['go', 'move']:
        player.movedir(action[1].lower())
        room_message()

    elif action[0].lower() in ['get', 'take', 'pickup']:
        item = ' '.join(action[1:])
        if item_exists(item):
            player.pickup_item(items[item.title()])
        else:
            print(f'You looked for a {item}, but did not find anything')

    elif action[0].lower() == 'drop':
        item = ' '.join(action[1:])
        if item_exists(item):
            player.drop_item(items[item.title()])
        else:
            print(f'You tried to drop {item}, but it\'s not in your inventory')

    elif action[0].lower() in ['character', 'i', 'inventory']:
        player.player_info()

    elif action[0].lower() in ['equip']:
        item = ' '.join(action[1:])
        if item_exists(item):
            player.equip_weapon(items[item.title()])
        else:
            print(f'You tried to equip {item}, but it\'s not in your inventory')

    elif action[0].lower() in ['unequip']:
        item = ' '.join(action[1:])
        if item_exists(item.title()):
            player.unequip_weapon(items[item.title()])
        else:
            print(f'You tried to un-equip {item}, but it\'s not equipped')


# Keep the game going until the player gets a game over
def main_game_loop():
    while player.game_over is False:
        prompt()


# Start the game
title_screen()
