from room import Room
from player import Player

# Declare all the rooms

room = {
    'roadside':  Room("Outside a Lonely Service Station in the Desert",
"To the north the station door is open, a light is on, but it seems empty inside"),

    'doorway':    Room("Just inside the doorway of the Service Station, a light flickers overhead", """To the south is only the desert, 
your busted old car, and the sinking sun. Further north are some ailes with food, much of it on the ground. To the east is the counter
and a door partially open."""),

    'ailes': Room("Rows of food and candy", """Some bag of chips and candy indicate that it was once neatly arranged, strangely
much of the items are now strewn on the floor, among muddy bootprints, and a strange black substance.  To the south is the doorway,
and the humming noise gets louder"""),

    'counter':   Room("A cash register, cigarettes, and a lone pair of eyeglasses", """In front of the counter the register is closed, behind
the counter a door creaks open invitingly to the north. Back west the humming dies down, but you need to find help."""),

    'breakroom': Room("Staff Break Room", """Everything here indicates a normal break room.  Coffee machine, old magazines, a half-broken
old television.   On the couch is a harmonica, finely engraved with the word Veritas.  For some reason, you feel the urge to pick it up.
To the north you see a mirror, which reflects the same room you are in, only with a gaping hole in the floor.  South is where you came from, safe and useless."""),
}

# Link rooms together

# room['roadside'].n_to = room['doorway']
# room['doorway'].s_to = room['roadside']
# room['doorway'].n_to = room['ailes']
# room['doorway'].e_to = room['counter']
# room['ailes'].s_to = room['doorway']
# room['counter'].w_to = room['doorway']
# room['counter'].n_to = room['breakroom']
# room['breakroom'].s_to = room['counter']

room['roadside'].connect(room['doorway'], 'n')
room['doorway'].connect(room['ailes'], 'n')
room['doorway'].connect(room['counter'], 'e')
room['counter'].connect(room['breakroom'], 'n')

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

player = Player(input("What is your name?"), room['roadside'])

print("Hello, %s!" % player.name)

while True:
    inp = input("> ")
    if inp == "q":
        print("You have quit the game")
        break
    print(inp)