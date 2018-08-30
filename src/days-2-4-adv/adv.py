from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["rock", "log", "rope"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["lamp", "chair", "table"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["bird's nest", "hiking pole"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["empty treasure chest", "shovel"]),
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

# print(room['foyer'].n_to.name)
# print(room['foyer'])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
from player import Player
player1 = Player(input('Enter player name: '), room['outside'])

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.

from item import Item
# item1 = Item('box', 'a small cardboard box')
# print(item1.name)

while True:
    print(player1.location.name + '\n'+ player1.location.description)
    print("Items in the room: ", player1.location.items)

    command = input('Next move: ')
    validCommands = ['n', 's', 'e', 'w','q']

    if command == 'q':
        print('GAME OVER')
        break

    if command in validCommands:
        dirAttr = command + '_to'

        if hasattr(player1.location, dirAttr): #The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not.
            player1.location = getattr(player1.location, dirAttr)
        else:
            print('Can\'t go that way! Please choose a different direction.')
    
    else:
        print('Invalid command.')
    
        


    

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']






# ##FIRST ATTEMPT 
# # Make a new player object that is currently in the 'outside' room.
# from player import Player
# player1 = Player('Bob', 'treasure')

# # Write a loop that:
# #
# # * Prints the current room name
# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.

# for key in player_1.__dict__:
#     if key == 'location': 
#         for key in room:
#             if key == player_1.location:
#                 print(room[player_1.location].name)
#                 print(room[player_1.location].description)
#         nextMove = input("Enter next move: ")

        
# # If the user enters a cardinal direction, attempt to move to the room there.
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.


# # if nextMove == 'n':
# #     if player_1.location == room[player_1.location].n_to.name:
# #     # player_1.location = room['foyer']
# #         print(player_1.location)
# #     else:
# #         print(player_1.location)

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# if nextMove == 'n':
#     if player_1.location == 'outside' or player_1.location == 'foyer' or player_1.location == 'narrow':
#         player_1.location = room[player_1.location].n_to.name
#         print(player_1.location)
#     else:
#         print('Movement not allowed!')
#         # nextMove = input("Enter next move: ")


# if nextMove == 's':
#     if player_1.location == 'foyer' or player_1.location == 'overlook' or player_1.location == 'treasure':
#         player_1.location = room[player_1.location].s_to.name
#         print(player_1.location)
#     else:
#         print('Movement not allowed!')
#         # nextMove = input("Enter next move: ")

# if nextMove == 'e':
#     if player_1.location == 'foyer':
#         player_1.location = room[player_1.location].s_to.name
#         print(player_1.location)
#     else:
#         print('Movement not allowed!')
#         # nextMove = input("Enter next move: ")

# if nextMove == 'w':
#     if player_1.location == 'narrow':
#         player_1.location = room[player_1.location].s_to.name
#         print(player_1.location)
#     else:
#         print('Movement not allowed!')
#         # nextMove = input("Enter next move: ")

# if nextMove == 'g': 
#     print('GAME OVER')