# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.
import textwrap
from room import rooms
from player import Player

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(rooms['outside'], 10)
playing = True
# Write a loop that:
while playing is True:
    # desc = TextWrapper(width = 150, initial_indent="    ", fill=player.location['name'])
# * Prints the current room name
    print('\nLocation: %s' % (player.location['name']))
# * Prints the current description (the textwrap module might be useful here).
    print(player.location['description'])
# * Waits for user input and decides what to do.
    direction = str(input('\n\nWhich way will you go? n, s, e, w (q to quit): '))
#
# If the user enters a cardinal direction, attempt to move to the room there.
    try:
        if direction == 'n':
            player.location = rooms[player.location['n_to']]
        elif direction == 's':
            player.location = rooms[player.location['s_to']]
        elif direction == 'e':
            player.location = rooms[player.location['e_to']]
        elif direction == 'w':
            player.location = rooms[player.location['w_to']]
        elif direction == 'q':
            break
    except:
        raise ValueError("That is not an option.")
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
