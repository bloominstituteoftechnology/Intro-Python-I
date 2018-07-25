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


newPlayer = Player('john', 'outside')


# Write a loop that:
while True:
    print(' ====> game is here...........')

    c = input('please type the cardial direction where u need to Go:')

    cardial = ['n', 'e', 'w', 's']
    if c.lower() not in cardial:
        print('there is no such direction...')
        continue

    if c:
        if c.lower() == 'n':
            c = "n_to"

        elif c.lower() == 's':
            c = "s_to"

        elif c.lower() == 'e':
            c = "e_to"

        elif c.lower() == 'w':
            c = "w_to"
        elif c == "q":
            break

    if hasattr(room[newPlayer.room], c) == False:
        print('====> there is no such direction...')
        continue

    nextRoom = getattr(room[newPlayer.room], c)

    if(nextRoom == None):
        print('====> there is no room here ')
        continue

    if(nextRoom != None):
        print('great job you are  in new room ====>:', nextRoom.name)
        print(f"....{nextRoom.description}...")
    ################################################################

    ##################################################################
    while(True):
        print('keep going .....')
        d = input('please type the 2nd  cardial direction where u need to Go:')

        bill = ['n', 'e', 'w', 's']
        if d.lower() not in bill:
            print('there is no such direction...')
            continue
        if d:
            if d.lower() == 'n':
                d = "n_to"

            elif d.lower() == 's':
                d = "s_to"

            elif d.lower() == 'e':
                d = "e_to"

            elif d.lower() == 'w':
                d = "w_to"

        if hasattr(nextRoom, d) == False:
            print('=====> there is no such direction...')
            continue

        roomAfter = getattr(nextRoom, d)

        if(roomAfter == None):
            print('====> there is no room here ...')
            continue

        if(roomAfter != None):
            print('## GREAT JOB ##  you are  in new room ====>:', roomAfter.name)
            print(f"....{roomAfter.description}...")

        nextRoom = roomAfter


# break

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
