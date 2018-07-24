from room import Room
from player import Player

# Declare all the rooms

room = {
    'cell_1':  Room("Your cell",
                     """You wake up on a cold, stone floor, your head pounding.
You take a few deep breaths, willing the pain to go away, and it finally recedes enough
for you to look around and get your bearings.  You find yourself in some sort of cell.
The cell door to the North... is open?""", """This is the cell you woke up in.  Still stone, still cold.  The cell door to the North is open."""),

    'cell_2': Room("Empty Cell", """It's an empty cell.  The floor is just as stone, and just as cold as your's was.
    To the North is the hallway you came in from."""),

    'cell_3': Room("Girl's Cell", """This is the cell where you found Eliza.  The floor is just as stone, and just as cold as your's was.
    To the North is the hallway you came in from."""),

    'hall_1': Room("Hallway", """You find yourself in a stone hallway.
    To the North, you hear the sound of voices filtering down the hallway.
    To the South is the cell you woke up in.
    To the East look like more cells.
    To the West you also hear the sound of voices filtering down the hallway."""),

    'hall_2': Room("Hallway", """In this part of the hallway, a cell door is swung halfway open to an empty cell.
    To the East looks to be another cell."""),

    'hall_3': Room("Hallway", """As you step in front of the cell, a grungy young woman scrambles up to the bars.
    \"Help me!\" she says.  \"You've got to help me!  Get me out of here!  Go and find the key, and get this door open!\"
    The hallway ends here.  You must turn around and head West back where you came from.""",
    """The girl looks at you pleadingly. \"Please!  Find the key!\"
    The hallway ends here.  You must turn around and head West back where you came from."""),

    'hall_4': Room("Hallway", """Description""", """VDescription"""),

    'hall_5': Room("Hallway", """Description""", """VDescription"""),
}


# Link rooms together

room['cell_1'].n_to = room['hall_1']
room['hall_1'].s_to = room['cell_1']
room['hall_1'].n_to = room['hall_4']
room['hall_1'].e_to = room['hall_2']
room['hall_1'].w_to = room['hall_5']
room['hall_2'].s_to = room['cell_2']
room['hall_2'].e_to = room['hall_3']
room['hall_2'].w_to = room['hall_1']
room['hall_3'].w_to = room['hall_2']


# room[''].n_to = room['']
# room[''].s_to = room['']
# room[''].e_to = room['']
# room[''].w_to = room['']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room["cell_1"], 10)
playing = True

# Write a loop that:
while playing is True:
# * Prints the current room name
    print('\nLocation: %s' % (player.location.name))
# * Prints the current description (the textwrap module might be useful here).
    if player.location.visited == True and player.location.vDescription is not None:
        print(player.location.vDescription)
    else:
        print(player.location.description)
    player.location.visited = True
# * Waits for user input and decides what to do.
    direction = str(input('\n\nWhich way will you go? N, S, E, W (Q to quit):'))
    print('\n____________________________________________\n')
#
# If the user enters a cardinal direction, attempt to move to the room there.
    try:
        if direction == 'n' or direction == 'N':
            player.location = player.location.n_to
        elif direction == 's' or direction == 'S':
            player.location = player.location.s_to
        elif direction == 'e' or direction == 'E':
            player.location = player.location.e_to
        elif direction == 'w' or direction == 'W':
            player.location = player.location.w_to
        elif direction == 'q' or direction == 'Q':
            break
    except:
        raise ValueError("That is not an option.")
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
