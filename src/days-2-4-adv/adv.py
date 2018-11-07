from room import Room
from player import Player
import sys

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


# Link rooms together -- I did not use these...

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room. DONE

# p1 = Player('Brian', room['outside'].room_name, room['outside'].room_description)

p_name = input("Player Name: ")

p1 = Player(p_name)

# Write a loop that:
#
# * Prints the current room name DONE
# * Prints the current description (the textwrap module might be useful here). DONE
# * Waits for user input and decides what to do. DONE


def set_player_direction(player):

    print("___PLAYER_ROOM___: " + player.room_name)
    print("___PLAYER_ROOM DESCRIPTION___: " + player.room_description)

    setting_direction = [True]

    while setting_direction:

        # Get input from user to set as direction to be returned.
        direction = input("Enter a direction [n, s, e, w] or q to quit.").lower()

        if direction == "n":
            return direction

        elif direction == "s":
            return direction

        elif direction == "e":
            return direction

        elif direction == "w":
            return direction

        elif direction == "q":
            print("Thanks for playing. I hope you had fun!")
            sys.exit()
        else:
            print("Invalid choice. Please choose either [n,s,e,w]")



# If the user enters a cardinal direction, attempt to move to the room there. DONE
# Print an error message if the movement isn't allowed. DONE
# If the user enters "q", quit the game. DONE


def play_game():

    playing_game = [True]

    while playing_game:

        # Get Direction from set_player_direction function
        direction = set_player_direction(p1)

        if direction == "q":
            print("Thanks for playing. I hope you had fun!")
            sys.exit()

        # Handle Outside to Foyer
        if p1.room_name == 'Outside Cave Entrance' and direction == 'n':
            p1.room_name = room['foyer'].room_name
            p1.room_description = room['foyer'].room_description

        # Handle Foyer back to Outside
        elif p1.room_name == "Foyer" and direction == "s":
            p1.room_name = room['outside'].room_name
            p1.room_description = room['outside'].room_description

        # Handle Foyer to Overlook
        elif p1.room_name == "Foyer" and direction == "n":
            p1.room_name = room['overlook'].room_name
            p1.room_description = room['overlook'].room_description

        # Handle Overlook back to Foyer
        elif p1.room_name == "Grand Overlook" and direction == "s":
            p1.room_name = room['foyer'].room_name
            p1.room_description = room['foyer'].room_description

        # Handle Foyer to Narrow
        elif p1.room_name == "Foyer" and direction == "e":
            p1.room_name = room['narrow'].room_name
            p1.room_description = room['narrow'].room_description

        # Handle Narrow to Foyer
        elif p1.room_name == "Narrow Passage" and direction == "w":
            p1.room_name = room['foyer'].room_name
            p1.room_description = room['foyer'].room_description

        # Handle Narrow to Treasure
        elif p1.room_name == "Narrow Passage" and direction == "n":
            p1.room_name = room['foyer'].room_name
            p1.room_description = room['foyer'].room_description
            print("CONGRATULATIONS, YOU HAVE REACHED THE TREASURE")

        # Handle Treasure back to Narrow
        elif p1.room_name == "Treasure Chamber" and direction == "s":
            p1.room_name = room['foyer'].room_name
            p1.room_description = room['foyer'].room_description


play_game()
