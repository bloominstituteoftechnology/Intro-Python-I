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

while True:
  new_player = input("Your hero's name? ")
  if len(new_player) == 0:
    print("Please enter your hero's name.\n")
  else:
    player = Player(new_player, room['outside'])
    print(f'\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\nWelcome to Myst...\n{player.name:^40}\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~')
    break
  
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
  choice = input(f'\n========================================\nYou are in {player.room.name.upper()}.\n{player.room.desc}\n\nWhere would you like to go?\n[n]orth, [e]ast, [s]outh, [w]est, or [q]uit\n')
  if len(choice) == 1:
    if choice == "q":
      print(f'\nAye, perhaps another day.')
      break
    elif choice == "n":
      player.move_to(choice)
    elif choice == "e":
      player.move_to(choice)
    elif choice == "s":
      player.move_to(choice)
    elif choice == "w":
      player.move_to(choice)
    else:
      print(f'\nAgain, where would you like to go?')
