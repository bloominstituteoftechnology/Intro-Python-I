from room import Room
from player import Player
from  item  import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
    [Item("Jar of Fairies","Each fairy is used to guide you North, South, East and West")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[Item("Magic Roomba","Removes the dust so you can see better")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
[Item("A golden septor", "to protect you from danger")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    [ ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
[]),
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

# Make a new player object that is currently in the 'outside' 
# room.
# name = input("\nWhat's your name?:")
player = Player(input("\nWhat's your name?:"),room['outside'],[])


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
    error = 'Halt!'

    print(f'\nRoom: {player.currentRoom.name}')
    print(f'{player.currentRoom.description}')
    print(f'{player.currentRoom.inventory}')

    answer = input("\nWhere to now? \n Or will you quit like a chicken? Press q to quit\n")
    
    if answer == "q":
        print("Get outta here!!")
        break

    if answer == "n":
        if not hasattr(player.currentRoom,'n_to'):
            print(error)
        else:
            player.currentRoom = player.currentRoom.n_to

    
    if answer == "s":
        if not hasattr(player.currentRoom,'s_to'):
            print(error)
        else:
            player.currentRoom = player.currentRoom.s_to

    

    if answer == "e":
        if not hasattr(player.currentRoom,'e_to'):
            print(error)
        else:
            player.currentRoom = player.currentRoom.e_to

    
    if answer == "w":
        if not hasattr(player.currentRoom,'w_to'):
            print(error)
        else:
            player.currentRoom = player.currentRoom.w_to


   


