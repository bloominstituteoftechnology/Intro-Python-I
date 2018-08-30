from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
<<<<<<< HEAD
                     "North of you, the cave mount beckons", ['sword']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['shield']),
=======
                     "North of you, the cave mount beckons",
                     []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),
>>>>>>> efaf676fe5cfe618d0f3f074e776ec0ad2337f54

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
<<<<<<< HEAD
to north. The smell of gold permeates the air.""", ['hookshot']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['fairy']),
}

items = {
    'fairy': Item('Fairy', 'A fairy kept inside a bottle that will restore your health if it hits 0. One time use'),
    'sword': Item('Kokiri Sword', 'A short sword perfect for a short person'),
    'shield': Item('Deku Shield', 'Does not like fire'),
    'hookshot': Item('Hookshot', 'A hook that stretches on a chain, allowing our adventurer to reach items and places normally out of reach')
=======
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
>>>>>>> efaf676fe5cfe618d0f3f074e776ec0ad2337f54
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
player = Player(input("Please enter your name: "), room['outside'], [])
incorrectMessage = '\nThere is no path in that direction'

# print(f"\nHello {player.name}")
print("Hello %s!" % player.name)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
while True:
<<<<<<< HEAD
    print(f'\nLocation: {player.location.name}')
    print(f'{player.location.description}')
    print(f'{player.location.items}')
=======
    # print(f'\nLocation: {player.location.name}')
    print("\nLocation: %s" % player.location.name)
    print("%s\n" % player.location.description)

    # print(f'{player.location.description}')
>>>>>>> efaf676fe5cfe618d0f3f074e776ec0ad2337f54

    direction = str(input('Which direction do you walk?  '))

    if direction == 'q':
        break
    elif direction.lower() == 'n' or direction.lower() == 'north':
        if player.location.n_to:
            player.location = player.location.n_to
            print('You decide to head north')
        else:
            print(incorrectMessage)
    elif direction.lower() == 's' or direction.lower() == 'south':
        if player.location.s_to:
            player.location = player.location.s_to
            print('You decide to head south')
        else:
            print(incorrectMessage)
    elif direction.lower() == 'w' or direction.lower() == 'west':
        if player.location.w_to:
            player.location = player.location.w_to
            print('You decide to head west')
        else:
            print(incorrectMessage)
    elif direction.lower() == 'e' or direction.lower() == 'east':
        if player.location.e_to:
            player.location = player.location.e_to
<<<<<<< HEAD
            print('You decide to head east')
=======
            print('You decide to head west')
>>>>>>> efaf676fe5cfe618d0f3f074e776ec0ad2337f54
        else:
            print(incorrectMessage)
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
