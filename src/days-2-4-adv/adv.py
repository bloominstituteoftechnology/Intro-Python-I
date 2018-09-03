import textwrap
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

# Add items to room
room['outside'].items = [
  Item('shoes', 'A pair of ostrich shoes.'), Item('slippers', 'A pair of Local Motion slippers.')]

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
my_player = Player(room['outside'])

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

WORD_WRAP_LIMIT = 30
is_hiding_room_description = False

while True:
    current_room = my_player.room
    if is_hiding_room_description == False:
      locationText = "\n\n".join(["", textwrap.fill(f"You are now in the {current_room.name}.", WORD_WRAP_LIMIT), textwrap.fill(current_room.description, WORD_WRAP_LIMIT)])
      is_hiding_room_description = True
      print(locationText)

    inp = input("\nWhere do you want to go? ")
    if inp == "q":
        break
    elif inp == "n" or inp == "e" or inp == "s" or inp == "w":
        next_room = current_room[f"{inp}_to"]
        if isinstance(next_room, Room):
            my_player.set_room(next_room)
            is_hiding_room_description = False
        else:
            print("\n\nYOU CANNOT GO THERE, so...")
    elif inp == "look":
        if (len(current_room.items) == 0):
            print("\n\nYou see nothing here.")
        else:
            print("\n\nYou see the following items:")
            for item in current_room.items:
                print(f"{item.name.upper()} - {item.description}")
            is_hiding_room_description = True
    else:
      print("Please enter a direction (n/e/s/w). Or enter q to QUIT.")
