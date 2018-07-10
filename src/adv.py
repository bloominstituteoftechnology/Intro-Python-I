# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
    },

}

""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
    },
"""
current_room = 'outside'

# Write a class to hold player information, e.g. what room they are in currently
class player_information:
    def __init__(self, room):
        self.name = room[current_room]['name']
        self.description = room[current_room]['description']

location = player_information(rooms)
print(location.name)
print(location.description)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = {
    "description": location.name,
    "location": location.description
}


while True:
    choice = input('Chose your direction venturer: ')
    # O U T S I D E   L O C A T I O N
    if current_room == 'outside':
        if choice in ('n'):
            current_room = 'foyer'
            location = player_information(rooms)
            print("Current location: " + location.name +"\nYou see: " + location.description + "\n\n")
        elif choice == 'q':
            break
        else:
            print('you cannot go that way, please use w,s,n,e for directions or q for quit')
    # F O Y E R
    elif current_room == 'foyer':
        if choice in ('n'):
            current_room = 'overlook'
            location = player_information(rooms)
            print("Current location: " + location.name +"\nYou see: " + location.description + "\n\n")
        elif choice == 's':
            current_room = 'outside'
            location = player_information(rooms)
            print("Current location: " + location.name +"\nYou see: " + location.description + "\n\n")
        elif choice == 'e':
            current_room = 'narrow'
            location = player_information(rooms)
            print("Current location: " + location.name +"\nYou see: " + location.description + "\n\n")
        elif choice == 'q':
            break
        else:
            print('you cannot go that way, please use w,s,n,e or q for quit')
    # O V E R L O O K
    elif current_room == 'overlook':
        if  choice == 's':
            current_room = 'foyer'
            location = player_information(rooms)
            print("Current location: " + location.name +"\nYou see: " + location.description + "\n\n")
        elif choice == 'q':
            break
        else:
            print('you cannot go that way, please use w,s,n,e or q for quit')
    # N A R R O W
    elif current_room == 'narrow':
        if choice in ('w'):
            current_room = 'foyer'
            location = player_information(rooms)
            print("Current location: " + location.name +"\nYou see: " + location.description + "\n\n")
        elif choice == 'n':
            current_room = 'treasure'
            location = player_information(rooms)
            print("Current location: " + location.name +"\nYou see: \n\n" + location.description + "\n\n")
        elif choice == 'q':
            break
        else:
            print('you cannot go that way, please use w,s,n,e or q for quit')
    # T R E A S U R E
    elif current_room == 'treasure':
        print('CONGRATULATION YOU FOUND THE TREASURE')
        if choice in ('s'):
            current_room = 'narrow'
            location = player_information(rooms)
            print("Current location: " + location.name +"\nYou see: " + location.description + "\n\n")
        elif choice == 'q':
            break
        else:
            print('you cannot go that way, please use w,s,n,e or q for quit')
        


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
