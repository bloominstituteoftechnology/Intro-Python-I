from room import Room 
from player import Player 
import textwrap
from item import Item, Treasure
from data import room, item
from item import LightSource

# Main
#
def main():
    player_name = input('Please enter your name: ')

# Make a new player object that is currently in the 'outside' room.
    new_player = Player(player_name, room['outside'], [], 0)
    while True:
        room_lit = new_player.current_room.is_light or len([item for item in new_player.current_room.room_items if isinstance(item, LightSource)]) > 0 or len([item for item in new_player.player_items if isinstance(item, LightSource)]) > 0
        if room_lit:
        # display current room info
            print()
            print()
            print()
            print(f"You are in the {new_player.current_room.name}")
            print()
            print(textwrap.wrap(new_player.current_room.description)[0])
            print()
            print('Items found in this room: ')
            for item in new_player.current_room.room_items:
                print('- ' + item.name + ': ' + item.description)
            print()
        else:
            print("It's pitch black!")
        # promp for an instruction
        print("'i' or 'inventory': display your items in your inventory")
        print("'get' or 'take' (item name): add item found in room to your inventory")
        print("'drop' (item name): drop item from inventory to the room")
        print("'n': go north")
        print("'s': go south")
        print("'e': go east")
        print("'w': go west")
        print("'s': display score")
        print("'q': quit game")
        new_input = input("What do you want to do next? ")

        # type check new_input input
        try:
            new_input = str(new_input) 

        except ValueError:
            print("Please make an acceptable input.")
        
        # handle single charactor inputs
        input_list = new_input.strip().lower().split(' ', 1)
        if len(new_input) == 1:
            #handle quit
            if new_input == 'q':
                print("Thank you for playing.  Goodbye!")
                break
            elif new_input == 's':
                print("Your current score is: " + str(new_player.score))

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
            verb = input_list[0].lower()
            item_name = input_list[1].lower()

            # handle get or take item from room to player
            if verb == 'get' or verb == 'take':
                if room_lit:
                    found_match = False
                    # find item in room item list
                    for item_object in new_player.current_room.room_items:
                        if item_name == item_object.name.lower():
                            found_match = True
                            new_player.take_item(item_object)
            
                            print('You have added ' + item_object.name +' to your inventory.')
                    if found_match == False:
                        print('Item is not found in room.  Please try again.')
                else:
                    print("Good luck finding that in the dark!")
            # handle drop item from player inventory
            elif verb =='drop':
                found_match = False
                # find item in player inventory
                for item_object in new_player.player_items:
                    if item_name == item_object.name.lower():
                        found_match = True
                        new_player.drop_item(item_object)
                if found_match == False:
                    print('Item is not found in your inventory.  Please try again.')
            else:
                print('Command is not recognized.  Please try again.')

        # handle displaying inventory
        elif input_list[0] =='inventory':
            print('You have the following items:')
            for item_object in new_player.player_items:
                print('- ' + item_object.name +': ' + item_object.description)
        elif input_list[0] == 'score':
            print('Your current score is: ' + new_player.score)
        else:
            print("Please enter an appropriate input.")        

main()