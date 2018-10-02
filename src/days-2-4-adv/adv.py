from room import Room
from player import Player
import textwrap
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

room['outside'].connecting('n', room['foyer'])
room['foyer'].connecting('s', room['outside'])
room['foyer'].connecting('n', room['overlook'])
room['foyer'].connecting('e', room['narrow'])
room['overlook'].connecting('s', room['foyer'])
room['narrow'].connecting('w', room['foyer'])
room['narrow'].connecting('n', room['treasure'])
room['treasure'].connecting('s', room['narrow'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p=Player(room['outside'].name)

# Write a loop that:

direction = "What direction do you want to move towards?"

while True:
        print(p.room_name())
        print(room[p.room].text)
        print(direction)
        cmd = input("-> ")
        if cmd == "q":
                print('You choose to quit.')
                break
        elif cmd == "n" or cmd == "s" or cmd == "e" or cmd == "w":
                nextroom = room[p.room].next_d
                p.room=nextroom
        else:
                print("I did not understand that command.")        


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
