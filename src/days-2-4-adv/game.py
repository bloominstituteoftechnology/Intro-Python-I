#Python Text RPG

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

###### Player Setup ######
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'd2'
        self.game_over = False
myPlayer = player()

###### Title Screen ######
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print["Please enter a valid command."]
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('          — Play —          ')
    print('          — Help —          ')
    print('          — Quit —          ')
    print('    Learning by m4rkh0ng    ')
    title_screen_selections()

def help_menu():
    print('############################')
    print('# Welcome to the Text RPG! #')
    print('############################')
    print('— Use up, down, left, right to move')
    print('— Type your commands to do them')
    print('— Use "look" to inspect something')
    print('— Have fun!')
    title_screen_selections()

###### GAME FUNCTIONALITY ######

###### MAP ######
# """
#  1  2  3  4
# -------------
# |  |  |  |  | a
# -------------
# |  |  |  |  | b
# -------------
# |  |  |  |  | c
# -------------
# |  |  |  |  | d
# -------------
# """

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                }

zonemap = {
    # 'a1': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # },
    # 'a2': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # },
    # 'a3': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # },
    # 'a4': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # },
    # 'b1': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # },
    'b2': {
        ZONENAME: "overlook",
        DESCRIPTION: 'Grand Overlook',
        EXAMINATION: """A steep cliff appears before you, falling into the darkness. 
        \nAhead to the north, a light flickers in the distance, 
        \nbut there is no way across the chasm.""",
        SOLVED: False,
        UP: '',
        DOWN: 'c2',
        LEFT: '',
        RIGHT: ''
    },
    'b3': {
        ZONENAME: "treasure",
        DESCRIPTION: 'Treasure Chamber',
        EXAMINATION: """You've found the long-lost treasure chamber! 
        \nSadly, it has already been completely emptied by earlier adventurers. 
        \n \nThe only exit is to the south.""",
        SOLVED: False,
        UP: '',
        DOWN: 'c3',
        LEFT: '',
        RIGHT: ''
    },
    # 'b4': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # },
    # 'c1': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # },
    'c2': {
        ZONENAME: "foyer",
        DESCRIPTION: 'Foyer',
        EXAMINATION: """Dim light filters in from the south. Dusty passages run north and east.""",
        SOLVED: False,
        UP: 'b2',
        DOWN: 'd2',
        LEFT: '',
        RIGHT: 'c3'
    },
    'c3': {
        ZONENAME: "narrow",
        DESCRIPTION: 'Narrow Passage',
        EXAMINATION: """The narrow passage bends here from west to north.
        \nThe smell of gold permeates the air.""",
        SOLVED: False,
        UP: 'b3',
        DOWN: '',
        LEFT: 'c2',
        RIGHT: ''
    },
    # 'c4': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # },
    # 'd1': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # },
    'd2': {
        ZONENAME: "outside",
        DESCRIPTION: 'Outside Cave Entrance',
        EXAMINATION: """North of you, the cave mount beckons""",
        SOLVED: False,
        UP: 'c2',
        DOWN: '',
        LEFT: '',
        RIGHT: ''
    },
    # 'd3': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # },
    # 'd4': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     UP: 'up', 'north',
    #     DOWN: 'down', 'south',
    #     LEFT: 'left', 'west',
    #     RIGHT: 'right', 'east'
    # }
}

###### GAME INTERACTIVITY ######
def print_location():
    print('\n' + ('#' * (4 + len(zonemap[myPlayer.location][DESCRIPTION]))))
    # print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print(('#' * (4 + len(zonemap[myPlayer.location][DESCRIPTION]))))

def prompt():
    print("\n" + "==============================")
    print("what would you like to do?")
    action = input("> ")
    acceptable_actions = ["move", "go", "travel", "walk", "quit", "examine", "inspect", "interact", "look", "help"]
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again. Not sure of what to do? Use "help" to find out!\n')
        action = input("> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "interact", "look"]:
        player_examine(action.lower())
    elif action.lower() in ["help"]:
        player_help(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)        
    if dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)        
    if dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)        
    if dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)        

def movement_handler(destination):
    if destination is '':
        print("You cannot move there. Try a different direction.")
    elif destination is not '':
        myPlayer.location = destination
        print("\n" + "You have moved to " + zonemap[myPlayer.location][DESCRIPTION] + ".")
        print_location()

def player_examine(action):
    print("You are at " + zonemap[myPlayer.location][DESCRIPTION] + "." + "\n" + zonemap[myPlayer.location][EXAMINATION])

def player_help(action):
    print("You can try to 'move' or 'examine' at this time.")

###### GAME FUNCTIONALITY ######
def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
    # here handle if puzzles have been solved, boss defeated, explored everything, etc.

def start_game():
    os.system('clear')

    ### NAME COLLECTING
    question1 = "Hello, what is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    player_name = input("> ")
    myPlayer.name = player_name

    ### JOB HANDLING
    question2 = "Hello, what role do you want to play as?\n"
    question2added = "(You can play as a warrior, mage, priest, archer, or bard.)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest', 'archer', 'bard']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")
    
    ### PLAYER STATS
    if myPlayer.job is 'warrior':
        self.hp = 120
        self.mp = 20
    elif myPlayer.job is 'mage':
        self.hp = 40
        self.mp = 120
    elif myPlayer.job is 'priest':
        self.hp = 65
        self.mp = 100
    elif myPlayer.job is 'archer':
        self.hp = 100
        self.mp = 60
    elif myPlayer.job is 'bard':
        self.hp = 80
        self.mp = 80

    ### INTRODUCTION

    question3 = "Welcome, " + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    
    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "Safe travels to you, friend!\n"
    speech3 = "If you ever get lost, ask for help!\n"
    speech4 = "[Press Enter to Continue]\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    input("> ")

    os.system('clear')
    print("##########################")
    print("#    Let's start now!    #")
    print("##########################")
    main_game_loop()

title_screen()