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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player(room['outside'])
playing = True
show_description = True
error = False
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
def handle_error():
    global error
    if error:
        print(error)
        error = None
        global show_description
        show_description = False

def handle_simple_command(word):
    if str(word).upper() == 'N' and hasattr(p.c_room, 'n_to'):
        p.update_room(p.c_room.n_to)
    elif str(word).upper() == 'E' and hasattr(p.c_room, 'e_to'):
        p.update_room(p.c_room.e_to)
    elif str(word).upper() == 'S' and hasattr(p.c_room, 's_to'):
        p.update_room(p.c_room.s_to)
    elif str(word).upper() == 'W' and hasattr(p.c_room, 'w_to'):
        p.update_room(p.c_room.w_to)
    elif str(word).upper() == 'Q':
        print("Better luck next time!")
        global playing
        playing = False
    else:
        global error
        error = "That is not a valid direction or command"

def handle_complex_command(words):
    global error
    global rooms
    global p
    if words[0].upper() == 'TAKE' or words[0].upper() == 'GET':
        item = list(filter(lambda i: i.name.upper() == words[1].upper(), p.c_room.items))[0]
        if item:
            p.items.get_item(item)
            p.c_room.items.remove(item)
        else:
            error = "There is no such item"
    else:
        error = "That command is invalid. please try again"


while playing:
    if show_description:
        print(p.c_room.location)
        print(p.c_room.description)
        p.c_room.list_items()
    show_description = True
    direction = input('Enter a command: ')
    words = direction.split()
    if len(words) == 1:
        handle_simple_command(words[0])
    else:
        handle_complex_command(words)
    handle_error()
