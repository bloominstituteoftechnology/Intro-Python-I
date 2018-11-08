from room import Room
from player import Player
from item import Item

# Declare all the rooms_______ Dictionary__________
#We have created an "obj" of "objs" for the Rooms Class (room.py) , it is 'here' in adv.py b/c
#the classes are just blue prints, this here below, is "The Room" content
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "skull"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "pickle"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "trash puppy"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "boot"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "toothpick butterfly"),
}

#__________Item Dictionary___________
items = {"pickle": "pickle", "skull": "skull", "boot": "boot", "trash": "trash","puppy": "puppy",
         "toothpick": "toothpick", "butterfly": "butterfly"}

#__________Direction Dictionary__________Here are the directions that are accepted, 
# we can name this w/e, but it must 
#be consistent through out the Loop
directions = {"n": "n", "e": "e", "s": "s", "w":"w"}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#__________________________________________________________
# Main
# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.
# #_____________________________________________________

#let's get the players name and place them 'outside' to start
nameInput = input("What is your name hero?...")
player = Player(nameInput, room["outside"])
print(f"{player.currentRoom}")

#_______The LOOP_____________________
while True:
    cmds = input("-->").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in directions:
            player.travel(directions[cmds[0]])
            print(f"{player.currentRoom}")
        elif cmds[0] == 'i' or cmds[0] == 'inventory':
            player.lookInventory()
        else:
            print(f'Sorry {player.name}, that command is not recognize, q = quit.')
    else:
        if cmds[0] == 'look':
            if cmds[1] in directions:
                player.lookAround(directions[cmds[1]])
        elif cmds[0] == "get" or cmds[0] == "grab":
            if cmds[1] in items:
                player.grabItem(items[cmds[1]])
        elif cmds[0] == "drop" or cmds[0] == "ditch":
            if cmds[1] in items:
                player.dropItem(items[cmds[1]])
        else:
                print(f'Sorry {player.name}, that command is not recognize, q = quit')

print(f'Thank you {player.name} for playing')
        
