import textwrap
from room import Room
from player import Player
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

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('outside')

# Write a loop that:


# * Prints the current room name
currentRoom = player.currentRoom
print(room[currentRoom].name)
    
# * Prints the current description (the textwrap module might be useful here).
print(room[currentRoom].description)
    
# * Waits for user input and decides what to do.
    

def one():
    player.moveTo('foyer')
    print(room['foyer'].name)
    print(room['foyer'].description)
    n = True
    s = True
    e = True
    w = False

def two():
    player.moveTo('overlook')
    print(room['overlook'].name)
    print(room['overlook'].description)
    
def three():
    player.moveTo('foyer')
    print(room['foyer'].name)
    print(room['foyer'].description)

def four():
    player.moveTo('foyer')
    print(room['foyer'].name)
    print(room['foyer'].description)

def five():
    player.moveTo('foyer')
    print(room['foyer'].name)
    print(room['foyer'].description)

while True:
def SwitchE(a):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five 
    }
    func = switcher.get(a, lambda: "nothing")
    func()   

    userInput = input("Please Progress- ")
    if userInput == 'q':
        break
    elif userInput == 'n':
        a = 1
        SwitchE(a)    
    
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
