from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Inside the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Inside the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("In a Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """You've found the long-lost treasure
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
p = Player(input("What is your name? "), "outside")


while True: 
    print(p)
    print(f"\nYou, {p.name}, are currently {room[p.room].name}. {room[p.room].description}. What would you like to do?\nType 'help' for list of commands. ")
    cmd = input(f'\n {p.name} ->')
    if cmd == "q":
        break
    elif cmd == "help":
        print("\nlist of commands: \n'n' to go north\n'e' to go east\n's' to go south\n'w' to go west\n'q' to exit\n ")
    else: 
        print('did not understand command')
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
