#Python Text RPG

import cmd
import textwrap
import sys
import os
import time
import random
from item import Item

screen_width = 100

###### Player Setup ######
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.inventory = []
        self.location = 'd2'
        self.game_over = False
myPlayer = player()

###### Items ######

class Apple(Item):
    def __init__(self):
        super(Apple, self).__init__('Apple', 'A healthy looking fruit.')

apple1 = Apple()

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
        print("[Please enter a valid command.]")
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
    print('— Type your commands to perform actions.')
    print('— Use "move" with north, south, east, west to navigate.')
    print('— Use "look" to inspect something.')
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

ZONENAME = 'zonename'
DESCRIPTION = 'description'
EXAMINATION = 'examination'
SOLVED = 'solved'
ITEMLIST = 'itemlist'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

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
    #     ITEMLIST = []
    #     NORTH: 'north',
    #     SOUTH: south',
    #     WEST: 'west',
    #     EAST: 'east',
    # },
    # 'a2': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     ITEMLIST = [],
    #     NORTH: 'north',
    #     SOUTH: 'south',
    #     EAST: 'east',
    #     WEST: 'west',
    # },
    # 'a3': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     ITEMLIST = [],
    #     NORTH: 'north',
    #     SOUTH: 'south',
    #     EAST: 'east',
    #     WEST: 'west',
    # },
    # 'a4': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     ITEMLIST = [],
    #     NORTH: 'north',
    #     SOUTH: 'south',
    #     EAST: 'east',
    #     WEST: 'west',
    # },
    # 'b1': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     ITEMLIST = [],
    #     NORTH: 'north',
    #     SOUTH: 'south',
    #     EAST: 'east',
    #     WEST: 'west',
    # },
    'b2': {
        ZONENAME: "overlook",
        DESCRIPTION: 'Grand Overlook',
        EXAMINATION: """A steep cliff appears before you, falling into the darkness. 
        \nAhead to the north, a light flickers in the distance, 
        \nbut there is no way across the chasm.""",
        SOLVED: False,
        # ITEMLIST = {"Glass Bead" : {"name": "Glass Bead", "description": "A toy for youngsters that's sort of like a marble. But not really."},
        #            {"Rod of Dreams" : {"name": "Rod of Dreams", "description": "You have yet to understand the mysteries of this wand."}}
        NORTH: '',
        SOUTH: 'c2',
        EAST: '',
        WEST: '',
    },
    'b3': {
        ZONENAME: "treasure",
        DESCRIPTION: 'Treasure Chamber',
        EXAMINATION: """You've found the long-lost treasure chamber! 
        \nSadly, it has already been completely emptied by earlier adventurers. 
        \n \nThe only exit is to the south.""",
        SOLVED: False,
        # ITEMLIST = {"Leather Belt" : {"name": "Leather Belt", "description": "Common leather belt. Sturdy construction."}},
        NORTH: '',
        SOUTH: 'c3',
        EAST: '',
        WEST: '',
    },
    # 'b4': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     ITEMLIST = [],
    #     NORTH: 'north',
    #     SOUTH: 'south',
    #     EAST: 'east',
    #     WEST: 'west',
    # },
    # 'c1': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     ITEMLIST = [],
    #     NORTH: 'north',
    #     SOUTH: 'south',
    #     EAST: 'east',
    #     WEST: 'west',
    # },
    'c2': {
        ZONENAME: "foyer",
        DESCRIPTION: 'Foyer',
        EXAMINATION: """Dim light filters in from the south. Dusty passages run north and east.""",
        SOLVED: False,
        # ITEMLIST = { "Valentinian Coin" : {"name": "Valentinian Coin", "description": "It gleams with an eerie aura about it. You sense a slight chill when you hold it in your hand."}},
        NORTH: 'b2',
        SOUTH: 'd2',
        EAST: 'c3',
        WEST: '',
    },
    'c3': {
        ZONENAME: "narrow",
        DESCRIPTION: 'Narrow Passage',
        EXAMINATION: """The narrow passage bends here from west to north.
        \nThe smell of gold permeates the air.""",
        SOLVED: False,
        # ITEMLIST = {"Big Twig" : {"name": "Big Twig", "description": "Not the sturdiest of branches, but nothing to shake a stick at, either. Or with."}},
        NORTH: 'b3',
        SOUTH: '',
        EAST: '',
        WEST: 'c2',
    },
    # 'c4': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     ITEMLIST = [],
    #     NORTH: 'north',
    #     SOUTH: 'south',
    #     EAST: 'east',
    #     WEST: 'west',
    # },
    # 'd1': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     ITEMLIST = [],
    #     NORTH: 'north',
    #     SOUTH: 'south',
    #     EAST: 'east',
    #     WEST: 'west',
    # },
    'd2': {
        ZONENAME: "outside",
        DESCRIPTION: 'Outside Cave Entrance',
        EXAMINATION: """North of you, the cave mount beckons""",
        SOLVED: False,
        ITEMLIST: [{"name": "Big Twig", "description": "Not the sturdiest of branches, but nothing to shake a stick at, either. Or with."}, apple1],
        NORTH: 'c2',
        SOUTH: '',
        EAST: '',
        WEST: '',
    },
    # 'd3': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     ITEMLIST = [],
    #     NORTH: 'north',
    #     SOUTH: 'south',
    #     EAST: 'east',
    #     WEST: 'west',
    # },
    # 'd4': {
    #     ZONENAME: "",
    #     DESCRIPTION: 'description',
    #     EXAMINATION: 'examine',
    #     SOLVED: False,
    #     ITEMLIST = [],
    #     NORTH: 'north',
    #     SOUTH: 'south',
    #     EAST: 'east'
    #     WEST: 'west',
    # }
}

# two_word_movement = ["move north", "move n", "move south", "move s", "move east", "move e", "move west", "move w"]

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

    acceptable_actions = ["quit", "q", "move", "look", "help", "search", "move north", "move n", "move south", "move s", "move east", "move e", "move west", "move w", "pickup", "search", "s", "h", "l", "m", "p", "m n", "m s", "m e", "m w", "check", "c"]
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again. Not sure of what to do? Use "help" to find out!\n')
        action = input("> ")
    if action.lower() in ["quit", "q"]:
        sys.exit()
    elif action.lower() in ["move", "m"]:
        player_move(action.lower())
    elif action.lower() in ["move north", "move n", "m n"]:
        destination = zonemap[myPlayer.location][NORTH]
        movement_handler(destination)    
    elif action.lower() in ["move south", "move s", "m s"]:
        destination = zonemap[myPlayer.location][SOUTH]
        movement_handler(destination)    
    elif action.lower() in ["move east", "move e", "m e"]:
        destination = zonemap[myPlayer.location][EAST]
        movement_handler(destination)    
    elif action.lower() in ["move west", "move w", "m w"]:
        destination = zonemap[myPlayer.location][WEST]
        movement_handler(destination)
    elif action.lower() in ["look", "l"]:
        player_examine(action.lower())
    elif action.lower() in ["help", "h"]:
        player_help(action.lower())
    elif action.lower() in ["search", "s"]:
        player_search(action.lower())
    elif action.lower() in ["pickup", "p"]:
        player_pickup(action.lower())
    elif action.lower() in ["check", "c"]:
        player_check(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask + "> ")
    if dest in ['north', 'n']:
        destination = zonemap[myPlayer.location][NORTH]
        movement_handler(destination)        
    if dest in ['south', 's']:
        destination = zonemap[myPlayer.location][SOUTH]
        movement_handler(destination)        
    if dest in ['east', 'e']:
        destination = zonemap[myPlayer.location][EAST]
        movement_handler(destination)        
    if dest in ['west', 'w']:
        destination = zonemap[myPlayer.location][WEST]
        movement_handler(destination)        

def movement_handler(destination):
    if destination is '':
        print("You cannot move there. Try a different direction.")
    elif destination is not '':
        myPlayer.location = destination
        print("\n" + "You have moved to " + zonemap[myPlayer.location][DESCRIPTION] + ".")
        print_location()

def player_examine(action):
    print("\nYou are at " + zonemap[myPlayer.location][DESCRIPTION] + "." + "\n" + zonemap[myPlayer.location][EXAMINATION])

def player_help(action):
    print("You can try to '[m]ove' or '[l]ook' at this time.")

def player_search(action):
    # if item is in room,
        # print(len(str(zonemap[myPlayer.location][ITEMLIST].items())))
        print(str(zonemap[myPlayer.location]["itemlist"]))
    # else print no items are in this area

def player_pickup(action):
    if len(str(zonemap[myPlayer.location]["itemlist"])) < 3:
        print("Doesn't look like there's anything to pick up.")
    elif len(str(zonemap[myPlayer.location]["itemlist"][-1])) > 3:
        item = str(zonemap[myPlayer.location]["itemlist"][-1])
        myPlayer.inventory.append(zonemap[myPlayer.location]["itemlist"].pop())
        print("Acquired " + item)
        # print("Acquired " + item[name])

def player_check(action):
    print(str(myPlayer.inventory))

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
        time.sleep(0.002)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.002)
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
        time.sleep(0.005)
    
    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "Safe travels to you, friend!\n"
    speech3 = "If you ever get lost, ask for help!\n"
    speech4 = "[Press Enter to Continue]\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.002)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.002)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.002)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.002)
    input("> ")

    os.system('clear')
    print("##########################")
    print("#    Let's start now!    #")
    print("##########################")
    main_game_loop()

title_screen()