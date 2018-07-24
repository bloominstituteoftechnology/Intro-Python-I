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
player1 = Player(room['outside'])

# Write a loop that:
#
complete = False

while not complete:

    print(player1.currRoom.room_name)
    print(player1.currRoom.description)
    
    user_action = raw_input("Choose a direction to go (n, e, s, w) ")

    if user_action is 'q':
        print("\n goodbye \n")
        # complete = True
        break
    
    directions = {
        "n": player1.currRoom.n_to,
        "e": player1.currRoom.e_to,
        "s": player1.currRoom.s_to,
        "w": player1.currRoom.w_to
    }


    if directions[user_action] is None:
        print("\nYou cannot go that way\n")

    else:
        player1.setRoom(directions[user_action])

print()


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
