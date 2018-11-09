from room import Room
from player import Player
import textwrap
from item import Item, Treasure, LightSource

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

# Add items to rooms

room['foyer'].items.append(Item('sword','A sword that you can instantly tell is well-made.'))
room['foyer'].items.append(LightSource('lamp','a source of light that can be refueled'))
room['narrow'].items.append(Item('vitamin tablet', 'a source of vitamins that stores for a long time'))

# Add treasures to rooms
room['foyer'].items.append(Treasure('gold brick', 'a shiny brick of gold weighing a kilogram', 500))
room['overlook'].items.append(Treasure('ruby', 'a beautiful ruby of 100 carats', 300))
room['treasure'].items.append(Treasure('diamond', 'a glimmering diamond cut to perfection', 800))

# Add light to proper rooms
room['outside'].is_light = True
room['foyer'].is_light = True
room['overlook'].is_light = True

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Masaharu Morimoto')
player.room = room['outside']
print(f'Player created...\nName: {player.name}.\nLocation: {player.room.name}\n')

# Write a loop that:
#
def print_items(array):
    if len(array)==0:
        return 'nothing'
    str1 = ''
    for addy in array:
        str1+= f'{addy.name}, '
    return str1

def add_item(room, item):
    room.items.append(item)

def get_amount_of_words(command):
    for letter in command:
        if letter==' ':
            return 2
    return 1

def get_first_word(command):
    str1 = ''
    for letter in command:
        if letter==' ':
            return str1
        str1+=letter
    print(f'error getting first word of {command}')

def get_second_word(command):
    second_word = ''
    passed_first_word = False
    for letter in command:
        if not passed_first_word:
            if letter==' ':
                passed_first_word = True
                continue
            else:
                continue
        else:
            second_word+=letter
    return second_word

def take_item(command):
    second_word = get_second_word(command)
    item_found = False
    for item in player.room.items:
        if item.name==second_word:
            if player.room.is_light:
                player.items.append(item)
                player.room.items.remove(item)
                item.on_take()
                item_found = True
            else:
                print('Good luck finding that in the dark!')
            return
    if not item_found:
        print(f'There is no {second_word} here.')
    else:
        print(f'Error occurred when trying to {command}.')

def drop_item(command):
    second_word = get_second_word(command)
    item_found = False
    for item in player.items:
        if item.name==second_word:
            player.items.remove(item)
            player.room.items.append(item)
            print(f'Player has dropped {item.name}.')
            item_found = True
            return
    if not item_found:
        print(f'Player is not carrying {second_word}.')
    else:
        print(f'Error occurred when trying to {command}.')

while True:
# * Prints the current room name
    if player.room.is_light:
        print(f'\nYou are now in {player.room.name}. Which contains {print_items(player.room.items)}.')
    else:
        print("It's pitch black!")
# * Prints the current description (the textwrap module might be useful here).
    wrapper = textwrap.TextWrapper(width=50)
    current_description = wrapper.wrap(text=player.room.description)
    for element in current_description:
        print(element)
# * Waits for user input and decides what to do.
#
    movement = input('\nPlease enter a direction (N,E,S,W) or command (get, drop, i, score):')
# If the user enters a cardinal direction, attempt to move to the room there.
    amount_of_words = get_amount_of_words(movement)
    if amount_of_words==1:
        if movement=='n' or movement=='N':
            if hasattr(player.room,'n_to'):
                player.room = player.room.n_to
            else:
                print('\nNo way North.')
        elif movement=='e' or movement=='E':
            if hasattr(player.room, 'e_to'):
                player.room = player.room.e_to
            else:
                print('\nNo way East.')
        elif movement=='s' or movement=='S':
            if hasattr(player.room, 's_to'):
                player.room = player.room.s_to
            else:
                print('\nNo way South.')
        elif movement=='W' or movement=='w':
            if hasattr(player.room, 'w_to'):
                player.room = player.room.w_to
            else:
                print('\nNo way West.')
        elif movement=='i' or movement=='inventory':
            print(f'\nYou have {print_items(player.items)}.')
        elif movement=='score':
            print(f'Your score is {player.score}')
    # If the user enters "q", quit the game.
        elif movement=='q':
            print('quitting...')
            break
    elif amount_of_words==2:
        first_word = get_first_word(movement)
        if first_word=='get' or first_word=='take':
            take_item(movement)
        elif first_word=='drop':
            drop_item(movement)
        else:
            print('Please enter N,E,S,W, get [item], or q(to quit)')
# Print an error message if the movement isn't allowed.
    else:
        print('Please enter N,E,S,W, get [item], i, or q(to quit)')
    continue
#
