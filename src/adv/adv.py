import textwrap
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


# I help
def goTo(direction, shipRoom):
    attr = direction + '_to'
    if hasattr(shipRoom, attr):
        return getattr(shipRoom, attr)

    return shipRoom


player1 = Player(room['outside'])
directions = set(['n', 's', 'e''w'])

playerChoice = None
# Write a loop that:
while True:
    # * Prints the current room name
    print(player1.currentRoom.name)
# * Prints the current description (the textwrap module might be useful here).
    print(textwrap.wrap(player1.currentRoom.description))
# * Waits for user input and decides what to do.
    playerChoice = input("Make a Choice\nOptions are n,s,e,w or q to quit.")
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if playerChoice in directions:
        if player1.currentRoom == goTo(playerChoice, player1.currentRoom):
            print('There is nothing in that direction')
        else:
            player1 = Player(goTo(playerChoice, player1.currentRoom))
    elif playerChoice == 'q':
        print('Bye bye')
        break
    else:
        print('Invalid option: pick one of \'n,s,e,w or q\'')
#
# If the user enters "q", quit the game.
