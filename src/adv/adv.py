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



player_name = input('Please enter your name ')
current_room = room['outside']
player = Player(player_name, current_room)
playing = True
while playing:

    print(player)

    choice = input("Which direction would you like to go?(north, west, south, east) ")

    if choice in ['north', 'south', 'west', 'east'] :
        if hasattr(current_room, choice[0] + '_to'):
            player.change_room(getattr(current_room, choice[0] + '_to'))
    
    elif choice == 'q':
        playing = False
    else:
        print('Hmm doesn\'t seem like you can go that way\n')
