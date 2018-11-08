from room import Room
from player import Player
from mage import Mage
from weapon import Weapon
from armor import Armor

# Declare all Weapons


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
player1 = Player()

# ----- testing to see if items inv worked -----
# killer = Mage()
# print(killer.items)

while True:
    print(
        f"You are now in {player1.current_room.name}. {player1.current_room.description}")
    dir = input("Where would you like to go?")
    if dir == "n":
        player1.enter(player1.current_room.n_to)
    elif dir == "e":
        player1.enter(player1.current_room.e_to)
    elif dir == "w":
        player1.enter(player1.current_room.w_to)
    elif dir == "s":
        player1.enter(player1.current_room.s_to)
    elif dir == "exit":
        break


# ----- too much code!!! -----

# while True:
#     print(f"Welcome, you are at the {player1.current_room.name}")
#     print(f"{player1.current_room.description}")
#     if player1.current_room.name == "Outside Cave Entrance":
#         answer = input('Do you want to head North, into the cave? Y/N')
#         if answer == "Y":
#             player1.current_room = player1.current_room.n_to
#         elif answer == "N":
#             print("Coward")
#             break
#         else:
#             print("Please enter Y or N")
#     keepgoing = input(
#         "Are you able to keep going? \nIf not, you can get out now by heading south, where you came from. \nIf so, you must push ahead north to the overlook. North/South?").upper()
#     if player1.current_room.name == "Foyer":
#         if keepgoing == "SOUTH":
#             player1.current_room = player1.current_room.s_to
#             print("Figures, come back when you have some courage")
#         elif keepgoing == "NORTH":
#             player1.current_room = player1.current_room.n_to
#             print(
#                 f"Welcome to {player1.current_room}, {player1.current_room.description}")
#         else:
#             print("Pick a real direction!")
    # if player1.current_room.name == "Overlook":

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
