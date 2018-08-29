from room import Room
from player import Player
# Declare all the rooms

room = {
    'cargo':  Room("Cargo Bay",
                     "You are inside a the cargo hold of an abandonded space station. The only door is to the north."),

    'corridor':    Room("Corridor", """Dim lights flicker in the corridor. Derelict
passages run north and east."""),

    'holodeck': Room("Holodeck", """The doors to the holodeck slide open. You enter, and an old program seems to
    be playing in a loop. 'Get ooouuuutt' a phantom voice seems to whisper quietly in the air. 
    The only exit is to the south"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of ash permeates the air."""),

    'incinerator': Room("Incinerator room", """You've found the incinerator
room! All that remains is ash. The only exit is to the south."""),
}


# Link rooms together

room['cargo'].n_to = room['corridor']
room['corridor'].s_to = room['cargo']
room['corridor'].n_to = room['holodeck']
room['corridor'].e_to = room['narrow']
room['holodeck'].s_to = room['corridor']
room['narrow'].w_to = room['corridor']
room['narrow'].n_to = room['incinerator']
room['incinerator'].s_to = room['narrow']


player = Player(room['cargo'])
#
# Main
#

# Make a new player object that is currently in the 'cargo' room.

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
    print (f"\n  {player.location.title}\n    {player.location.description}\n" )
    inp = input("What is your command: ")
    if inp == "q":
        break
    if inp == "n" or inp == "s" or inp == "w" or inp == "e":
        newRoom = player.location.getRoomInDirection(inp)
        if newRoom == None:
            print("You cannot move in that direction")
        else:
            player.change_location(newRoom)