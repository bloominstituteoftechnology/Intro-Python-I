from room import Room 
from player import Player 
import textwrap
from item import Item
from data import room

# Define items
# scroll = Item('Scroll', 'A rolled-up piece of old paper')
# dictionary = Item('Dictionary', 'An old dusty book with lots of words in it')
# holy_grail = Item('Holy Grail', 'A golden chalice')

# Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons", [scroll, dictionary]),

#     'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", []),

#     'overlook': Room("Grand Overlook", "A steep cliff appears before you,falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", []),

#     'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.",[]),

#     'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",[holy_grail]),
# }

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
def main():
    new_player_name = input('Please enter your name: ')

# Make a new player object that is currently in the 'outside' room.
    new_player = Player(new_player_name, room['outside'],[])

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

    while True:
        # display current room info
        print(f"You are in the {new_player.current_room.name}")
        print(textwrap.wrap(new_player.current_room.description))
        print()
        print('Items found in this room: ')
        for item in new_player.current_room.room_items:
            print('- ' + item.name + ': ' + item.description)
        print()
        # promp for an instruction
        print("'i' or 'inventory': display your items in your inventory")
        print("'get' or 'take' (item name): add item found in room to your inventory")
        print("'drop' (item name): drop item from inventory to the room")
        print("'n': go north")
        print("'s': go south")
        print("'e': go east")
        print("'w': go west")
        print("'q': quit game")
        new_input = input("What do you want to do next? ")

        # type check new_input input
        try:
            new_input = str(new_input) 

        except ValueError:
            print("Please make an acceptable input.")
        
        # handle single charactor inputs
        input_list = new_input.split(' ')
        if len(new_input) == 1:
            #handle quit
            if new_input == 'q':
                print("Thank you for playing.  Goodbye!")
                break

            #handle making a move
            elif new_input == 'n' or new_input == 's' or new_input == 'e' or new_input == 'w':
                key = new_input + '_to'
                if hasattr(new_player.current_room, key):
                    new_player.current_room = getattr(new_player.current_room, key)
                    if new_player.current_room.name == 'Treasure Chamber':
                        print("You won!!")
                        break
                else:
                    print("This move is not allowed.  Please try again.")
            
            # handle displaying inventory
            elif new_input == 'i':
                print('You have the following items:')
                for item_object in new_player.player_items:
                    print('- ' + item_object.name +': ' + item_object.description)
            else:
                print("Please enter an acceptable input.")

        # handle 2-word inputs
        elif len(input_list) == 2:
            verb = input_list[0]
            item_name = input_list[1]

            # handle get or take item from room to player
            if verb == 'get' or verb == 'take':
                found_match = False
                # find item in room item list
                for item_object in new_player.current_room.room_items:
                    if item_name == item_object.name:
                        found_match = True
                        new_player.player_items.append(item_object) # add item to player inventory
                        new_player.current_room.room_items.remove(item_object) # remove item from room item list
                        print('You have added' + item_object.name +' to your inventory.')
                if found_match == False:
                    print('Item is not found in room.  Please try again.')
            # handle drop item from player inventory
            elif verb =='drop':
                found_match = False
                # find item in player inventory
                for item_object in new_player.player_items:
                    if item_name == item_object.name:
                        found_match = True
                        new_player.player_items.remove(item_object) #remove item from player inventory
                        new_player.current_room.room_items.append(item_object) # add item to room item list
                if found_match == False:
                    print('Item is not found in your inventory.  Please try again.')
            else:
                print('Command is not recognized.  Please try again.')

        # handle displaying inventory
        elif input_list[0] =='inventory':
            print('You have the following items:')
            for item_object in new_player.player_items:
                print('- ' + item_object.name +': ' + item_object.description)
        else:
            print("Please enter an appropriate input.")

main()