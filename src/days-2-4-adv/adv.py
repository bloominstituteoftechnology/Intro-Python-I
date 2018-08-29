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

player = {'default_character': Player('JJ', room['outside'], 'brown', 'blue', 'male', 'slender'),}


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
current_room = room['outside']
user_character = player['default_character']
print("Welcome to the game!")
player_name = input("Enter your name:")
inp = input("Type 'JJ' to play as JJ, or Type 'C' to create a character:")
if inp == 'JJ':
  user_character == player['default_character']
  print(user_character)
else:
  char = inp("Please enter your characters info (name, hair color, eye color, gender, build)")  
  player[player_name] = Player(name = char.name, in_room = room['outside'], hair_color = char.hair_color, eye_color = char.eye_color, gender = char.gender, build = char.build )
  print(player[player_name])
while True:
  print("You are at the {}.".format(current_room.name))
  inp = input("What is your input: ")
  if inp == 'q':
    print("See ya!")
    break
  elif inp == 'n' and current_room == room['outside']:
    current_room = room['outside'].n_to
  elif inp == 's' and current_room == room['outside']:
    print("Can not go any further South.")
  elif inp == 'e' and current_room == room['outside']:
    current_room = room['outside'].s_to
  elif inp == 'me':
    print(player[player_name])
    

    


#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
