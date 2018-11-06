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
res = '--start of game --'
location = 'outside'

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
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player(input("what is your name hero?"), room["outside"])
current_room = room[player.current_room].description

while not res[0] == 'q':
    command = input("am I working?").lower().split(" ")
    #while player is outside
    if location == 'outside':
        print(current_room)
        res = input('\nwhat will you do?\n').split(" ")
        command(res, player, current_room)

        if res[0] == 'get' or res[0] == 'drop':
            pass
        elif res[0] == 'n':
            current_room = current_room.room_direction(res[0])
            location = 'foyer'
        elif not res[0] == 'q':
            print('try a different input')
    #Foyer
    if location == 'foyer':
        print(current_room)
        res = input('\nwhat will you do?\n').split(" ")
        command(res, player, current_room)

        if res[0] == 'get' or res[0] == 'drop':
            pass
        elif res[0] == 's':
            current_room = current_room.room_direction(res[0])
            location = 'outside'
        elif res[0] == 'e':
            current_room = current_room.room_direction(res[0])
            location = 'narrow'
        elif res[0] == 'n':
            current_room = current_room.room_direction(res[0])
            location = 'overlook'
        elif not res[0] == 'q':
            print('try a different input')
    #Narrow
    if location == 'narrow':
        print(current_room)
        res = input('\nwhat will you do?\n').split(" ")
        command(res, player, current_room)

        if res[0] == 'get' or res[0] == 'drop':
            pass
        elif res[0] == 'w':
            current_room = current_room.room_direction(res[0])
            location = 'foyer'
        elif res[0] == 'n':
            current_room = current_room.room_direction(res[0])
            location = 'treasure'
        elif not res[0] == 'q':
            print('try a different input')
    #Overlook
    if location == 'overlook':
        print(current_room)
        res = input('\nwhat will you do?\n').split(" ")
        command(res, player, current_room)

        if res[0] == 'get' or res[0] == 'drop':
            pass
        elif res[0] == 's':
            current_room = current_room.room_direction(res[0])
            location = 'foyer'
        elif not res[0] == 'q':
            print('try a different input')
    #Treasure
    if location == 'treasure':
        print(current_room)
        res = input('\nwhat will you do?\n').split(" ")
        command(res, player, current_room)

        if res[0] == 'get' or res[0] == 'drop':
            pass
        elif res[0] == 'w':
            current_room = current_room.room_direction(res[0])
            location = 'foyer'
        elif res[0] == 's':
            current_room = current_room.room_direction(res[0])
            location = 'narrow'
        elif not res[0] == 'q':
            print('try a different input')

print('\Thank you for playing')
        
