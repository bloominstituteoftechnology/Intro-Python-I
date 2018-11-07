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
    valid_moves = {'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'}
    currRoom = p.room
    inventory = p.items
    get_item = p.get_item
    view_inventory = p.view_inventory
    text_divider = '\n====================\n'

    def try_get_item(item_name):
        if item_name == currRoom.item.name:
            get_item(currRoom.item)
            print(text_divider)
            print_wrapped_lines(f'Player has picked up {currRoom.item.description}.')
            print('\n')
            setattr(currRoom, 'item', item['nothing'])
        else:
            print(text_divider)
            print_wrapped_lines(f'This room does not have a {item_name}')
            print('\n')

    def try_drop_item(item_name):
        for index, item in enumerate(inventory):
            if item.name == item_name:
                del inventory[index]
                setattr(currRoom, 'item', item)
                print(text_divider)
                print_wrapped_lines(f'Player has dropped the {item_name}.')
                print('\n')
                return view_inventory()
        print(text_divider)
        print(f'Your inventory does not contain: {item_name}.')
        return print('\n')

    print(text_divider)

    while True:
        print_wrapped_lines(f'You are currently in the {currRoom.name}.')
        print_wrapped_lines(currRoom.description)
        print('\n')
        print_wrapped_lines(f'This room has {currRoom.item.description}.')

        print('\n')

        print_wrapped_lines('What would you like to do?')
        next_action = input('(g)et <item> / (d)rop <item> / (i)inventory / (k)eep moving / (q)uit :')
        next_action = next_action.lower()

        if next_action[:4] == 'get ':
            try_get_item(next_action[4:])
            continue

        elif next_action[:2] == 'g ':
            try_get_item(next_action[2:])
            continue

        elif next_action[:5] == 'drop ':
            try_drop_item(next_action[5:])
            continue

        elif next_action[:2] == 'd ':
            try_drop_item(next_action[2:])
            continue

        elif next_action == 'inventory' or next_action == 'i':
            print(text_divider)
            view_inventory()
            print('\n')
            continue

        elif next_action == 'keep moving' or next_action == 'k':
            pass
        
        elif next_action == 'quit' or next_action == 'q':
            print(text_divider)
            print_wrapped_lines('Do you really want to quit?')
            print('\n')
            confirm_exit = input('(y)es / (n)o :')
            confirm_exit = confirm_exit.lower()

            if confirm_exit == 'yes' or confirm_exit == 'y':
                print(text_divider)
                print_wrapped_lines('See ya!')
                return print('/n')
            else:
                print(text_divider)
                continue
        
        else:
            print(text_divider)
            print(f'Invalid input: {next_action}')
            print('\n')
            continue

        print(text_divider)
        print_wrapped_lines('You decide to keep moving.')
        print('\n')
        print_wrapped_lines('Which direction do you want to go?')

        next_move = input('(n)orth / (s)outh / (e)ast / (w)est / (q)uit :')

        next_move = next_move.lower()
        print(text_divider)
        room_attr = f'{next_move[0]}_to'

        if (len(next_move) == 1 and next_move[0] in valid_moves.keys()) or next_move in valid_moves.values():
            if hasattr(currRoom, room_attr):
                currRoom = getattr(currRoom, room_attr)
            else:
                print_wrapped_lines(f'There is nothing to the {valid_moves[next_move[0]]}. Pick another direction.')
                print('\n')
        elif next_move == 'quit' or next_move == 'q':
            print_wrapped_lines('Do you really want to quit?')
            print(text_divider)
            print('\n')
            confirm_exit = input('(y)es / (n)o :')
            confirm_exit = confirm_exit.lower()

            if confirm_exit == 'yes' or confirm_exit == 'y':
                print(text_divider)
                print_wrapped_lines('See ya!')
                return print('/n')
            else:
                print(text_divider)
        else:
            print(text_divider)
            print(f'Invalid direction: {next_move}')
            print('\n')

if __name__ == '__main__':
    start_game()
