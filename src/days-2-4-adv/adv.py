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
player = Player(room['outside'])

# Write a loop that:
while True:
# * Prints the current room name
    print(player.location.name)

# * Prints the current description (the textwrap module might be useful here).
    print(player.location.description)

# * Waits for user input and decides what to do.
    input = input("Please enter a command: ")

    # If the user enters "q", quit the game.
    if input == "q":
        break

# If the user enters a cardinal direction, attempt to move to the room there.
    if input == "n" or input == "s" or input == "e" or input == "w":
        newRoom = player.location.goToRoomInEnteredDirection(input)
       
        # If the movement isn't allowed, print an error message 
        if newRoom == None:
            print("\n ===That direction is not allowed at this time=== \n")
        else:
            # Else move the user to the room specified
            player.change_location(newRoom)

    # If the user enters a cardinal direction, attempt to move to the room there.
    """elif input == "n":
      player.location = player.location.n_to
    elif input == "s":
      player.location = player.location.s_to
    elif input == "e":
      player.location = player.location.e_to
    elif input == "w":
      player.location = player.location.w_to
    else:"""
    # If the movement isn't allowed, print an error message 
      #print("\n ===That direction is not allowed at this time=== \n") 



