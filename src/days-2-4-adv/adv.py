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

player = Player('Samwise', room['foyer'])

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

initialGreeting = print(f"""Welcome {player.name}! You are currently located in the following room:

    {player.curRoom.name}:
    {player.curRoom.description}

    The following Items are available for you to use:
    {player.curRoom.items}

    How would you like to proceed?""")

while True:
    print(initialGreeting)
    userInput = input('>>> ').split(' ')

    if userInput[0] == 'quit':
        print('Thanks for playing, have a nice day!')
        exit()
    elif userInput[0] in ['north', 'east', 'south', 'west']:
        newRoom = player.curRoom.getRoomInDirection(userInput)
        if newRoom == None:
            print('You cannot move in this direction.')
        else:
            player.change_location(newRoom)
    else:
        print('INVALID INPUT: please input a proper command for {}'.format(player.name))