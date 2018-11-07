from room import Room
from player import Player
from item import Item

import textwrap

# TODO: Abstract Rooms and Items to separate file
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

items = {
    'Sword': Item('Sword', 'A simple sword'),
    'Potion': Item('Potion', 'A health potion'),
    'Book': Item('Book', 'A dirty old book')
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

room['outside'].inventory = [items['Sword'], items['Book']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


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

# Global vars
player = Player("Nicocchi", room['outside'])
player_inp = ''


# Set the player's name
def set_init_player():
    global player

    # Ask the player for the character name
    user_input = input("\nEnter Your Character's Name\n")

    if user_input == '':
        set_init_player()

    # Ask the player if the name is correct
    result = input(f'\nAre you sure {user_input} is the right name? [y] yes or [n] no?\n')

    # If the name is right, set the player and continue the game,
    # else, loop this function
    if result == 'y':
        player = Player(user_input, room['outside'])
    else:
        set_init_player()


# Gets the player's input and sets it in the global var user
def player_input():
    global player_inp
    player_inp = input("\nWhat do you do?\n").lower()


# Display the screen message
def screen_message():
    print(f'\n{player.room.name}')
    desc = textwrap.wrap(player.room.description, width=70)
    for element in desc:
        print(element)


# TODO: Simplify/Abstract this
# Check if the item exists in the Items dict, and if exists,
# Use the player pickup method to pickup the item, if not,
# return a message printing item not found
def item_exists(item):
    bl = False
    for itm in items:
        if itm == item.capitalize():
            bl = True
            return True

    if bl is False:
        return False


# START GAME
# Initialize the character input, display the room message and initialize the player's input
# These three functions run once then the while loop takes over


set_init_player()
screen_message()
player_input()

# While the input is not q, keep get game going
while not player_inp == 'q':

    # TODO: Abstract the command handler
    # if player chooses North
    if player_inp == 'n':
        player.movedir('north')
    elif player_inp == 's':
        player.movedir('south')
    elif player_inp == 'e':
        player.movedir('east')
    elif player_inp == 'w':
        player.movedir('west')
    elif player_inp == 'look around':
        player.look_around()
    elif player_inp[:6] == 'pickup':
        if item_exists(player_inp[7:]):
            player.pickup_item(items[player_inp[7:].capitalize()])
        else:
            print(f"{player_inp[7:]} is not in the room")
    elif player_inp[:4] == 'drop':
        if item_exists(player_inp[5:]):
            player.drop_item(items[player_inp[5:].capitalize()])
        else:
            print(f"{player_inp[5:]} is not in inventory")
    elif player_inp == 'show inventory' or 'inventory':
        player.show_inventory()
    else:
        print("Invalid selection. Please try again.\n")

    # TODO: Get rid of legacy code
    # if the player has a room, continue to display the
    # room message, else, display input message to avoid infinite loop of same room
    # if player.room and player.previous_room is not player.room:
    #     screen_message()
    # else:
    #     print(f'\n{player.name} tried to move to {player.direction} but was blocked. Try another direction.\n')

    screen_message()
    player_input()
