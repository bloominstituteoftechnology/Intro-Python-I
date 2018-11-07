import textwrap
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

# Main


# Make a new player object that is currently in the 'outside' room.

while True:
  new_player = input("\n\nType in your player's name: ")
  if len(new_player) == 0:
    print("Please enter your hero's name.\n")
  else:
    player = Player(new_player, room['outside'])
    print(f"\nWelcome, {player.name}")
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

# DIRECTION

def direction(direction, current):
    # Try to move a direction, or print error if player can't go that way.
    # Returns room the player moved to or same room if player didn't move.
    attrib = direction + '_to'
    # See if the room has the destination attribute
    if hasattr(current, attrib):
        # If so, return its value (the next room)
        return getattr(current, attrib)
    # Otherwise print an error and stay in the same room
    print("You can NOT go that way")
    return current

done = False

while not done:
  s = input("\n\nWhich way would you like to go? (N, S, E, W)\n").strip().lower().split()
  if s[0] in ["n", "s", "w", "e"]:
    player.current = direction(s[0], player.current)
    print("\nCurrent room: {}".format(player.current.name))
    print(player.current.desc)
  elif s[0] == "quit" or s[0] == "q":
            done = True
  else:
    print("Unknown command {}".format(' '.join(s)))

