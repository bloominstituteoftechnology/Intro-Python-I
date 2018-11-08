import textwrap
from room import Room
from player import Player
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
player = Player(room['outside'])

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
wrapper = textwrap.TextWrapper(width=50)
done = False

while not done:
    print(f"you are currently in {player.current_room.name}")
    print(wrapper.wrap(text=player.current_room.description)[0])

    user_input = input("\ncommand>").strip().lower().split()
    print(user_input)

    if len(user_input) > 2 or len(user_input) < 1:
        print("i dont understand that?")
        continue

    if len(user_input) == 1:

        if user_input[0] == 'quit' or user_input[0] == 'q':
            done = True

        elif user_input[0] in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west', ]:
            player.current_room = player. try_move(user_input[0][0])