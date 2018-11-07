from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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
player_name = input("\nEnter your name: ") 
player = Player(player_name, "outside")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

# def moving():
#     print("Move around using north, south, east, & west")
#     room = 'outside'

while True:
    print("Move around using north, south, east, & west")
    room = 'outside'    
    direction = input('input your direction: ')
    if direction == 'q' or direction == 'quit':
        print("Thanks for playing!\n")
        break
    
    # try:
    #     direction = str(direction)
    # except ValueError:
    #     print("please enter a cardinal direction (n,e,w,s)")
    #     continue
    if room == 'outside' and direction == 'n':
        # room[player.location] = room.player.location
        # print(room)
        if (room[player.location].n_to):
            player.location = room[player.location].n_to
        print('you\'re in the foyer')
    elif room == 'outside':
        if direction == 's' or direction == 'e' or direction == 'w':
            print('cannot go that way')
            continue
        else:
            print('not a direction')
            continue
    if room == 'foyer' and direction == 's':
        room == 'outside'
        print(room)
    elif room == 'foyer':
        if direction == 'n':
            room == 'overlook'
            print(room)
            if direction == 'e':
                room == 'narrow'
                print(room)
            if direction == 'w':
                print('cannot go that way')
                continue
        else:
            print('not a direction')
            continue
        if room == 'overlook':
            if direction == 's':
                room == 'foyer'
                print(room)
        elif direction == 'n' or direction == 'e' or direction == 'w':
            print('cannot go that way')
            continue
    if room == 'narrow':
        if direction == 'w':
            room == 'foyer'
            print(room)
        if direction == 'n':
            room == 'treasure'
            print(room)
        elif direction == 's' or direction == 'e':
            print('cannot go that way')
            continue
    if room == 'treasure':
        if direction == 's':
            room == 'narrow'
            print(room)
        elif direction == 'n' or direction == 'e' or direction == 'w':
            print('cannot go that way')
            continue
            
# if __name__ == '__main__':
#     moving()

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
