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

move = ''
letterToDirection = {'N': 'North', 'S': 'South', 'E': 'East', 'W': 'West'}
flair = "\n***********************************************************\n"
print(flair)
print("\nWelcome to 'let's move around a little bit'!\nThe game where the title really says it all!\n")
print(flair)

name = input("Please choose your hero's name: ")
player = Player(name, room['outside'])


while move != 'Q':
    
    room = player.getRoom()
    room.getDescription()
    validMoves = room.validMoves()
    
    print(flair)
    print(f"\n{str(player)}, Please choose a direction by typing the corresponding letter..\n")
    print(flair)

    # Loop through cardinal directions and get that rooms values
    for key, value in validMoves.items():
        print(f"{letterToDirection[key]} ({key}): {str(value)} \n")
    
    print(f"Q : quit \n")
    

    move = input(": ").upper()

    if move in list(validMoves.keys()):
      newRoom = validMoves[move]
      player.room = newRoom
      print(flair)
      print(newRoom.getDescription())
    elif move == 'Q':
        break
    else:
      print("\nPlease enter a valid letter for the direction you want to go")

print("Goodbye")