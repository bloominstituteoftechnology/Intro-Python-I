from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [ Item('Sharp rock', 'Ouch! This rock is sharp, but useless.') ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
# players attribute is the room it is in.
player = Player('Alexis', room['outside'], ['Mango'] )

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

done = False
start = False

while not done:
    while not start:
        print("\n", player.name, player.room.name, player.room.description)
        start = True
    choice = input("\n Enter a direction: n, s, e, or w. Press i to check inventory, or enter q to quit. ").lower()
    if choice == 'i':
        print("\n ", "Inventory: ")
        for item in player.items:
            print("  ", item)
    if choice != 'q':
        choice += '_to'
        if hasattr(player.room, choice):
            player.room = getattr(player.room, choice)  
            print("\n You have entered the" ,player.room.name,",", player.room.description )
    else:
        break
    # print(choice)
    if choice == "q":
        done = True
    # elif choice in ["n", "s", "e", "w"]:
    #     break
    # done = True


