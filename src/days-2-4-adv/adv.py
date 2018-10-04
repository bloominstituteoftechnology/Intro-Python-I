from room import Room, Dark_Room
from player import Player
from item import Item, Treasure, Light_Source
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Treasure(5, 'sword')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Treasure(3, 'shield')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Light_Source('flashlight')]),

    'treasure': Dark_Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('stick')], False),
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
player = Player(input("What is your character's name?   "), room['outside'], [])
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
    print(f'\nLocation: {player.location.name}')
    if hasattr(player.location, 'visibility'):
        for item in player.inventory:
            if hasattr(item, 'light'):
                print(f"The {item.name} gives light to the dark room!")
                player.location.light_on()
                print(f'{player.location.description}')
                if len(player.location.items) > 0:
                    player.location.print_items()
        if player.location.visibility is not True:
            print(f"The room is dark and you can't see anything!")
    else:
        print(f'{player.location.description}')
        if len(player.location.items) > 0:
            player.location.print_items()

    player_input = input(f'\nWhat does {player.name} do?   ')
    player_input_args = player_input.split(' ')

    if len(player_input) < 1:
        print('\nControls: \nN,S,E,W to move to a different room. \nTake ___ to take an item. \nDrop ___ to drop an item. \nI to view your inventory. \nZ to view score \nQ to quit')

    if len(player_input) == 1:
        if player_input[0].lower() == "q":
            break
        elif player_input[0].lower() == "n" or player_input[0].lower() == "s" or player_input[0].lower() == "w" or player_input[0].lower() == "e":
            player.change_location(player_input[0])
        elif player_input[0].lower() == "i":
            player.view_inventory()
        elif player_input[0].lower() == "z":
            player.get_score()
        else:
            print('\nControls: \nN,S,E,W to move to a different room. \nTake ___ to take an item. \nDrop ___ to drop an item. \nI to view your inventory. \nZ to view score \nQ to quit')

    if len(player_input_args) == 2:
        if player_input[0].lower() == "t" or player_input[0].lower() == "take":
            taking_item = player.location.find_item(player_input_args[1])
            if taking_item == None:
                print(f"You couldn't find a {player_input_args[1]}")
            else:
                if hasattr(taking_item, 'value'):
                    player.add_to_score(taking_item.value)
                    if taking_item.value > 0:
                        print(f"You gained {taking_item.value} points for finding the {taking_item.name}")
                    taking_item.remove_value()
                player.take_item(taking_item)
                player.location.remove_item(taking_item)

        elif player_input[0].lower() == "d" or player_input[0].lower() == "drop":
            dropped_item = player.find_item(player_input_args[1])
            if dropped_item.name == None:
                print(f"You dont have a {player_input_args[1]} to drop!")
            else:
                player.drop_item(dropped_item)
                player.location.add_item(dropped_item)
