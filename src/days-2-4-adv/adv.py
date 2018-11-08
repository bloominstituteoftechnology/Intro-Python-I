import textwrap
import time
from room import Room
from player import Player
from item import Item

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

# Created items for certain rooms
book = Item("a book", "dusty and old")
room['foyer'].contents.append(book)

coin = Item("a rare gold coin", "worth a fortune")
room['narrow'].contents.append(coin)


# Make a new player object that is currently in the 'outside' room.

while True:
    print("\n\nHello,")
    time.sleep(1)
    new_player = input("\nType in player's name: ")
    if len(new_player) == 0:
        print("Please enter player's name.\n")
    else:
        player = Player(new_player, room['outside'])
        time.sleep(1)
        print("\nWelcome,")
        print(f"{player.name}")
        time.sleep(1)
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
    print("\nYou can NOT go that way")
    time.sleep(1)

    return current

def search(name, current):
    # Search the current room for items.
    for item in current.contents:
        if item.name == name:
            return item

    return None

done = False

while not done:
# list of items in room
  items = [item for item in player.contents + player.current.contents]
  s = input("\n\nYou can 'search' or change direction (N, S, E, W)\n").strip().lower().split()

  if s[0] in ["n", "s", "w", "e"]:
    player.current = direction(s[0], player.current)
    time.sleep(1)
    print("\nCurrent room: {}".format(player.current.name))
    time.sleep(1)
    print(player.current.desc)
    time.sleep(2)

  elif s[0] == "search":
    time.sleep(1)
    print("\nYou found:\n")
    time.sleep(1)
    for item in player.current.contents:
        print("     " + str(item))
        time.sleep(1)
    # If the user enters "q", quit the game.
  elif s[0] == "quit" or s[0] == "q":
            done = True
  else:
    print("Unknown command {}".format(' '.join(s)))

