from room import Room
from player import Player
# import textwrap
# Declare all the rooms
# oh my what do we have here...

# okay so up at the top we're importing the room class

# and here we're creating a Python dictionary  
# inside this dictionary each key is just a string
# each value is an instance of Room class, with a name and a description
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
# now this is a little weird perhaps I should stop right here and draw a map 
# of all the rooms. Yeah that should help; visualize the layout of the game map first
# before tackling anything else...

# so those .n_to, .s_to, etc appear to be methods that I haven't defined yet.
# I think I have to define those methods in the room class...
# aha! now I see something new after playing around with super simple on-the-fly classes
# in the console I see that I can add attributes to an instance of a class
# these attributes can be...anything I want! In the case below each of the attributes added are
# other instances of the Room class
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
# so after mapping out the rooms I've decided that I don't like this implementation
# There has to be a better way...My intuition tells me there's a better way to implement this
# but I'll go with the way it is for now...
# okay if I think of this game as an app then this would be my top-level file
# this is where the main loop of the game is called...
# Main  
# Make a new player object that is currently in the 'outside' room.
new_player_message = """
    Greetings player 1. Welcome to the Super Adventure Game. 
    Please enter a name for your hero: """
name = input(new_player_message)

player = Player(name, room['outside'])
# print(player.room.name)
# player.room = player.room.n_to
# print(player.room.name)
# Write a loop that:
boolean = player.room['outside'].w_to
print(boolean)
invalid = "You can't go in that direction."
while True:

    print(player.room.name)
    print('\n')
    print(player.room.description)

    message = """
    Which direction do you go? 
    Enter n, w, e, s for North,
    West, East, or South: """

    action = input(message)

    if action == 'n':
        if player.room.n_to != None:
            player.room = player.room.n_to
        else:
            print(invalid)
    elif action == 'w':
        if player.room.w_to != None:
            player.room = player.room.n_to
        else: 
            print(invalid)
    elif action == 's':
        if player.room.s_to != None:
            player.room = player.room.s_to
        else:
            print(invalid)
    elif action == 'e':
        if player.room.e_to != None:
            player.room = player.room.e_to
        else: 
            print(invalid)
    elif action == 'q':
        print("Goodbye!")
        break
    

    
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
