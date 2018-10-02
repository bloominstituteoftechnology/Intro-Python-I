from room import Room

# Declare all the rooms

room = {
    'laboratory':  Room("Gnarly Laboratory",
                     "The lab has a faint smell of iron and ammonia. Flickering light overhead half-illuminates a gnarly scene."),

    'office':    Room("C-Suite Office", """The executive offices, of course, are empty.  Everyone in C-Suite managed to escape."""),

    'incinerator': Room("Grand Incinerator", """A hot, dark room barely lit by flame peaking out of the incinerator."""),

    'chapel':   Room("The Passage Chapel", """Idols and iconography cover every inch of the chapel."""),

    'pendulum': Room("The Pendulum", """You've reached the Pendulum. Conditioned air envelopes you.  The doors lock behind you.  You see the key-switch ahead and you know what you must do."""),
}


# Link rooms together

room['laboratory'].f_to = room['office']
room['office'].b_to = room['laboratory']
room['office'].f_to = room['incinerator']
room['office'].r_to = room['chapel']
room['incinerator'].b_to = room['office']
room['chapel'].l_to = room['office']
room['chapel'].f_to = room['pendulum']
room['pendulum'].b_to = room['chapel']

#
# Main
#

# Make a new player object that is currently in the 'laboratory' room.

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
