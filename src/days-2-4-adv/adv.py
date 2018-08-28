from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('DaBoss')

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
while True:
    print("DESC: {}".format(room[player.location].description))
    inp = input("\nEnter a command: ")
    if inp == 'q' or inp == 'quit':
        break
    elif inp == "l" or inp == 'look':
        print()
    #     print(room[player.location].description)
    elif inp =='n':
        try:
            if (room[player.location].n_to):
                player.location = room[player.location].n_to
                # print(room)
                # player.location = room[player.location].n_to.name.lower()
                # print(room.keys())
        except:
            print("Can't continue north")
    elif inp =='s':
        try:
            if (room[player.location].s_to):
                player.location = room[player.location].s_to
        except:
            print("Can't continue south")
    elif inp =='e':
        try:
            if (room[player.location].e_to):
                player.location = room[player.location].e_to
        except:
            print("Can't continue east")
    elif inp =='w':
        try:
            if (room[player.location].w_to):
                player.location = room[player.location].w_to
        except:
            print("Can't continue west")
    else:
        print("I don't know that command")