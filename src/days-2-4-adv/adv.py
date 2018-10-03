from room import Room
from player import Player
from item import Treasure, LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", True),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", True),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].add_item(LightSource('Lantern', 'A source of light in the dark'))

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']

room['overlook'].s_to = room['foyer']
room['overlook'].add_item(Treasure('Sword', 'A very shiny sword', 500))

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']

room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player(room['outside'])

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

valid_directions = {"n": "n", "e": "e", "s": "s", "w": "w",
                    "north": "n", "east": "east", "west": "west", "south": "south"}

print(p.c_room)

while True:
  command = input('Command: ').lower().split(' ')
  if len(command) == 1:
    if command[0] == 'q' or command[0] == 'quit':
      break
    elif command[0] in valid_directions:
      p.update_room(valid_directions[command[0]])
    elif command[0] == 'look':
      p.look()
    elif command[0] == 'i' or command[0] == 'inventory':
      p.list_items()
    elif command[0] == 'exits':
      p.c_room.list_exits(p.has_light_item())
    elif command[0] == 'score':
      print(f'Your current score is: {p.score}')
    else:
      print("I don't understand that command")
  elif len(command) == 2:
    if command[0] == 'take' or command[0] == 'get':
      p.take_item(command[1])
    elif command[0] == 'drop':
      p.drop_item(command[1])
    else:
      print("I don't understand that command")
  else:
    print("I don't understand that command")
