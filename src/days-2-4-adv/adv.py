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
player = Player(room['outside'])

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
    #     print("You're currently in {player.room.name}")
    #     print(player.room.description)

    # user_input = input("\nCommand> ").strip().lower().split()

    # if len(user_input) > 2 or len(user_input) < 1:
    #     print("No Comprende")
    # continue

    # if len(user_input) == 1:
    #     if user_input[0] == 'quit' or user_input[0] =='q':
    #         done = True
    #     elif user_input[0] [0] in ['n', 's', 'e', 'w']:
    #         player.room = player.move(user_input[0] [0])

    # def start_game():
    #     print(new_player)

    #     print(new_player)

    # start_game()

    # room = Room("Outside", "outside")
    # foyer = Room("Foyer", """Dim light filters in from the south. Dusty
    # passages run north and east.""")
    # room.n_to = foyer
    # foyer.s_to = room

    # p = Player(name="Anthony", room["outside"], description="white male")
    # print(p.room)
    # p.room = room.n_to
    # print(p.room)

    print(' ')
    print('You are standing in the:', player.room.name)
    print(textwrap.wrap(player.room.description))
    move = input('Where will you move next?')
    print()
    try:
        move = move.lower()
    except AttributeError:
        print('Please enter a direction')
        continue
    if move in ['n', 'e', 's', 'w', 'q']:
        d = f"{move}_to"
        print(d)
        print(move)
        if move != 'q':
            #  if hasattr(player.room, d)
            #     print("this is inside hasattr")
            #     player.room = getattr(player.room, d)
                # setattr(player.room, room.d) # player.room = player.room.
             try:
                player.room = getattr(player.room, d)
                # print(f"something in here{player.room.d}")
               
             except AttributeError:
                print('You may not move in that direction. Try again')
        # if move == 'n':
        #     try:
        #         player.room = player.room.n_to
        #     except AttributeError:
        #         print('You may not move in that direction. Try again')
        #         continue
        # elif move == 'e':
        #     try:
        #         player.room = player.room.e_to
        #     except AttributeError:
        #         print('You may not move in that direction. Try again')
        #         continue
        # elif move == 's':
        #     try:
        #         player.room = player.room.s_to
        #     except AttributeError:
        #         print('You may not move in that direction. Try again')
        #         continue
        # elif move == 'w':
        #     try:
        #         player.room = player.room.w_to
        #     except AttributeError:
        #         print('You may not move in that direction. Try again')
        #         continue
        elif move == 'q':
            break
    else:
        print('Please enter a direction or "q" to quit')
