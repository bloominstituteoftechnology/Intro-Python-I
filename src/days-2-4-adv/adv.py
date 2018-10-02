from room import Room
from player import Player

class Player():
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def __str__(self):
        return f"\n{self.name}\n{self.location}"

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"\n{self.name}\n{self.description}"


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

# player = Player(room['outside'])
# print(player.currentRoom.description)
players = {
    'player 1': Player("Francis", "outside")
}

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

def current(location):
    for key in room:
        if key == location:
            print("Current location: " + room[key].name)
            print (room[key].description)

location = players['player 1'].location
current(location)
cmd =input("where are you going? ->")
while True:
    cmd = input("-> ")
    if cmd == "q":
        break
    if (location == 'outside'):
        if cmd == "n":
            location = 'foyer'
            current(location)
            cmd =input("where are you going? ->")
        else:
            print('You cannot go there! Try again!')
    else:
        print("I did not understand that command.")
