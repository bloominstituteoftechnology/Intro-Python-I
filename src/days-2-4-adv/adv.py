import textwrap
from item import Item
from room import Room
from player import Player

# Declare all items

item = {
    'nothing': Item(
                'nothing',
                'no items'
            ),
    'sword': Item(
                'sword',
                'a wooden SWORD'
            ),

    'shield': Item(
                'shield',
                'an iron SHIELD'
            )
}

# Declare all the rooms

room = {
    'outside':  Room(
                    'Outside Cave Entrance',
                    'North of you, the cave mount beckons.',
                    item['nothing']
                ),

    'foyer':    Room(
                    'Foyer',
                    'Dim light filters in from the south. Dusty passages run north and east.',
                    item['shield']
                ),

    'overlook': Room(
                    'Grand Overlook',
                    'A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.',
                    item['sword']
                ),

    'narrow':   Room(
                    'Narrow Passage',
                    'The narrow passage bends here from west to north. The smell of gold permeates the air.',
                    item['nothing']
                ),

    'treasure': Room(
                    'Treasure Chamber',
                    'You\'ve found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.',
                    item['nothing']
                )
}


# Link rooms together

room['outside'].n_to    = room['foyer']
room['foyer'].s_to      = room['outside']
room['foyer'].n_to      = room['overlook']
room['foyer'].e_to      = room['narrow']
room['overlook'].s_to   = room['foyer']
room['narrow'].w_to     = room['foyer']
room['narrow'].n_to     = room['treasure']
room['treasure'].s_to   = room['narrow']

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

p = Player(room['outside'], [])

def print_wrapped_lines(value = ''):
    wrapper = textwrap.TextWrapper(width = 50)
    word_list = wrapper.wrap(text = value)

    for element in word_list:
        print(element)

def start_game():
    valid_moves = ['n', 's', 'e', 'w', 'q']
    currRoom = p.room
    currItems = p.items
    get_item = p.get_item
    text_divider = '\n====================\n'

    print(text_divider)

    while True:
        print_wrapped_lines(f'You are currently in the {currRoom.name}.')
        print_wrapped_lines(currRoom.description)
        print('\n')
        print_wrapped_lines(f'This room has {currRoom.item.description}.')

        print(text_divider)

        if currRoom.item.name != 'nothing':
            next_action = input('What would you like to do? (get <item>/view items/keep moving):')
            if next_action.lower() == f'get {currRoom.item.name}':
                get_item(currRoom.item)
                setattr(currRoom, 'item', item['nothing'])
                next_action = input('What would you like to do? (view items/keep moving):')



        next_move = input('Which direction do you want to go? (n/s/e/w):')

        print(text_divider)

        room_attr = f'{next_move.lower()}_to'

        if next_move.lower() not in valid_moves:
            print_wrapped_lines(f'{next_move} is an invalid move.')
            print('\n')
        elif next_move.lower() == 'q':
            print_wrapped_lines('Do you really want to leave?')
            print(text_divider)
            print('\n')
            confirm_exit = input('Cofirm: (y/n):')
            if (confirm_exit.lower() == 'y'):
                print(text_divider)
                print_wrapped_lines('See ya!')
                print(text_divider)
                return print('/n')
            else:
                print(text_divider)
        elif hasattr(currRoom, room_attr):
            currRoom = getattr(currRoom, room_attr)
        else:
            direction = {'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'}
            print_wrapped_lines(f'There is nothing to the {direction[next_move.lower()]}. Pick another direction.')
            print('\n')

if __name__ == '__main__':
    start_game()
