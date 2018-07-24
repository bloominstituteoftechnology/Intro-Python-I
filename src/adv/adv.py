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

new_player = Player('outside')


# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

for key,value in room.iteritems():
   # print(value, key)
   if key == new_player.location:
       print("YOUR CURRENT LOCATION: " + value.name)

# If the user enters a cardinal direction, attempt to move to the room there.
North = "n_to"
South = "s_to"
East = "e_to"
West = "w_to"

print("\nPlease enter North to move north, South to move south East to move east, West to move west... ")


direction_input = 'hey'
while direction_input != 'q':
    direction_input = raw_input(
    "Please enter directions: e east, w west, n north, s south, to quit q \n")

    direction_input = str(direction_input) + '_to'
# print(direction_input)
    new_direction = "start"
    if direction_input == "n_to":
        try:
            new_direction = room[str(new_player.location)].n_to
        except AttributeError, message:
            print "FAIL FAIL:", message
            exit(1)
        # break
    elif direction_input == "s_to":
        try:
            new_direction = room[str(new_player.location)].s_to
        except AttributeError, message:
            print "FAIL FAIL:", message
            exit(1)
        # break
    elif direction_input == "e_to":
        try:
            new_direction = room[str(new_player.location)].e_to
        except AttributeError, message:
            print "FAIL FAIL:", message
            exit(1)
        # break
    else:
        try:
            new_direction = room[str(new_player.location)].w_to
        except AttributeError, message:
            print "FAIL FAIL:", message
            exit(1)
    new_player = Player(new_direction.name)
    print(new_direction.name)
    print(new_player.location)



# If the user enters "q", quit the game.
