from room import Room
from player import Player
import sys

# Declare all the rooms

room = {
    'outside': Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        ),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room['outside'].add_item({None: None})

#
# Main
#

# Make a new player object that is currently in the 'outside' room. DONE

# p2 = Player('John')
# print(p2)

p_name = "Brian"

p1 = Player(p_name)


# Write a loop that:
#
# * Prints the current room name DONE
# * Prints the current description (the textwrap module might be useful here). DONE
# * Waits for user input and decides what to do. DONE


def set_player_choice(player):
    print("__PLAYER_ROOM__: " + player.room_name)
    print("__PLAYER_ROOM DESCRIPTION__: " + player.room_description)
    print(player.get_items())

# Get input from user to set as choice to be returned.

    choice = input("Enter a choice [n, s, e, w] or q to quit.").strip().lower()

    if choice == "n":
        return choice

    elif choice == "s":
        return choice

    elif choice == "e":
        return choice

    elif choice == "w":
        return choice

    elif choice == "r":
        return choice

    elif choice == "q":
        print("Thanks for playing. I hope you had fun!")
        sys.exit()

    elif choice == "p":
        return choice

    else:
        print("Invalid choice. Please choose either [n,s,e,w]")


# If the user enters a cardinal choice, attempt to move to the room there. DONE
# Print an error message if the movement isn't allowed. DONE
# If the user enters "q", quit the game. DONE


def play_game():

    while True:

        # Get choice from set_player_choice function
        choice = set_player_choice(p1)

        if choice == "r":
            p1.get_items()

        if choice == "p":
            "Your items " + str(p1.pick_up_items_in_room())

        # Handle Outside to Foyer
        if p1.room_name == 'Outside Cave Entrance' and choice == 'n':
            p1.room_name = room['foyer'].room_name
            p1.room_description = room['foyer'].room_description
            p1.items_list = room['foyer'].add_item({'Wand': "Useful for many things..."})

        # Handle Foyer back to Outside
        elif p1.room_name == "Foyer" and choice == "s":
            p1.room_name = room['outside'].room_name
            p1.room_description = room['outside'].room_description

        # Handle Foyer to Overlook
        elif p1.room_name == "Foyer" and choice == "n":
            p1.room_name = room['overlook'].room_name
            p1.room_description = room['overlook'].room_description

        # Handle Overlook back to Foyer
        elif p1.room_name == "Grand Overlook" and choice == "s":
            p1.room_name = room['foyer'].room_name
            p1.room_description = room['foyer'].room_description

        # Handle Foyer to Narrow
        elif p1.room_name == "Foyer" and choice == "e":
            p1.room_name = room['narrow'].room_name
            p1.room_description = room['narrow'].room_description

        # Handle Narrow to Foyer
        elif p1.room_name == "Narrow Passage" and choice == "w":
            p1.room_name = room['foyer'].room_name
            p1.room_description = room['foyer'].room_description

        # Handle Narrow to Treasure
        elif p1.room_name == "Narrow Passage" and choice == "n":
            p1.room_name = room['foyer'].room_name
            p1.room_description = room['foyer'].room_description
            print("CONGRATULATIONS, YOU HAVE REACHED THE TREASURE")

        # Handle Treasure back to Narrow
        elif p1.room_name == "Treasure Chamber" and choice == "s":
            p1.room_name = room['foyer'].room_name
            p1.room_description = room['foyer'].room_description



play_game()
