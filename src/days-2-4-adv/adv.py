from player import Player
from item import Treasure, LightSource
from world_gen import world_gen

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player(world_gen())

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
