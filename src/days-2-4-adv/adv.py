from player import Player
from room import Room

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


# Write a loop that:
#
while True:
    inp = input('<Create your character> with Name, Job, and Location set to outside: ')
    if inp == "q":
        break
    # All logic required to create new character with custom job title and set location to outside default with Player class
    elif inp == "yes":
        charName = input("Please enter your name: ")
        charJob = input("Please create your own job title: ")
        charLocation = input("Set your location to outside: ")
        if charLocation != "outside":
            input('Please set your location to outside" ')
        elif charLocation == "outside":
            newPlayer = Player(charName, charJob, charLocation)
            print("Your character's name is {}, job title is {} and location is {}".format(newPlayer.name, newPlayer.job, newPlayer.location))
        if newPlayer.location == "outside":
            input()
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
