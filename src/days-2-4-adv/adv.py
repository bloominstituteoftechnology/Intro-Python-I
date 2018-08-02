from room import Room
from player import Player
import textwrap
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
current_room = 'outside'
player = Player(room[current_room])
# Write a loop that:
#
while True:
    moved = False
    print("Player Room: {}".format(player.room.name))

    wrapper = textwrap.TextWrapper(width=50)
    description_list = wrapper.wrap(text=player.room.description)

    print("Description: ")
    for desc in description_list:
        print(desc)

    user_input = input("Enter cardinal direction n, e, w, s or q to quit  -> ")

    if user_input == 'q':
        break

    direction_to = user_input + "_to"
    print(direction_to)

    for r_name in room.keys():
        if hasattr(room[r_name], direction_to):
            if getattr(room[r_name], direction_to) == room[current_room]:
                player.room = room[r_name]
                current_room = r_name
                moved = True
                break

    if moved:
        print("Moved to room {}".format(current_room))
    else:
        print("Movement is not allowed")

