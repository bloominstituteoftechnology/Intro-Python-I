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

p = Player(input("What is your name? "), room["outside"])

print(p.room) # this comes from the __str__ statement

while True: 
    cmds = input(f'\n-->').lower().split(" ")
    if len(cmds) == 1: 
        cmd = cmds[0]
        if cmd == "q":
            break
        elif cmd == "me":
            p.playerItems()
            # print(f'\n--You currently have {p.object}')
        elif cmd == "room":
            p.room.roomItems()
            # print(f"\n--The room contains {p.room.object}")
        elif cmd == "get":
            p.addObject(p.room.object)
            p.room.removeObject()
        elif cmd == "drop":
            p.dropObject()
        elif cmd == "help":
            print("\nlist of commands:\n'n' to go north\n'e' to go east\n's' to go south\n'w' to go west\n'q' to exit\n'room' list object in room\n 'me' list objects you have \n 'get' pick up object from room \n 'drop' drop object")
        elif cmd in valid_directions: 
            p.changeRoom(valid_directions[cmd])
        else: 
            print('not a valid command')