from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Inside the Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Inside the Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("In a Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

# room['outside'].object = 'a compass'
room['outside'].items = ['a compass', 'grass']
# room['treasure'].object = 'a note'

valid_directions = {
    "n": "n", 
    "north": "n", 
    "e": "e", 
    "east": "e", 
    "s": "s", 
    "south": "s", 
    "w": "w", 
    "west": "w" 
}

valid_commands = {
    "me": "me",
    "room": "room",
    "get": "get",
    "drop": "drop",
    "look": "look",
}

commands_help = [
    {"command": "does this action"},
    {"n": "moves to the north"},
    {"e": "moves to the east"},
    {"s": "moves to the south"},
    {"w": "moves to the west"},
    {"look <direction>": "preview move to <direction>"},
    {"me": "returns the items that you have"},
    {"room": "returns item in the room"},
    {"get <item>": "picks up item in the room"},
    {"drop <item>": "drops item in the room"},
    {"back": "exits help menu"},
    {"q": "exits program"}
]

p = Player(input("What is your name? "), room["outside"])

print(f'\nYou are currently: \n{p.room}') # this comes from the __str__ statement

while True: 
    cmds = input(f'\n-->').lower().split(" ")
    if len(cmds) == 1: 
        cmd = cmds[0]
        if cmd in valid_directions: 
            p.changeRoom(valid_directions[cmd])
        elif cmd == "me":
            p.playerItems()
        elif cmd == "room":
            p.room.roomItems()
        elif cmd == "get":
            p.addObject(p.room.object)
            p.room.removeObject()
        elif cmd == "drop":
            p.dropObject()
        elif cmd == "help":
            for c in commands_help:
                print(dict(c))            
        elif cmd == "command":
            print('command is not a command it is a header')
        elif cmd == "q":
            break
        elif cmd == "back" || cmd == "look":
            print(p.room)
        else: 
            print('not a valid command')
    else: 
        if cmds[0] == "look": 
            if cmds[1] in valid_directions:
                p.lookRoom(valid_directions[cmds[1]])
        if cmds[0] == "get":
            if cmds[1] in p.room.items:
                p.addItem(cmds[1])
                p.room.dropItem(cmds[1])
                print(p.room)
        if cmds[0] == "drop":
            if cmds[1] in p.items:
                p.dropItem(cmds[1])
                p.room.addItem(cmds[1])