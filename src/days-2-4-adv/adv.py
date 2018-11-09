from room import Room
from player import Player
from item import Item

# Declare all the rooms

items = {
    'potion': Item("potion",
                   "this improves health"
    ),
    'sword': Item("excalibur",
                  "very sharp"
    ),
    'treasure': Item("treasure",
                     "lots of gold coins"
    ),
    'lamp': Item('lamp',
                 'helps you see'
    )
}


room = {
    'outside':  Room("outside",
                     "North of you, the cave mount beckons",
                     True,
                     [items["potion"]]
                     #{'n': 'foyer', 's': None, 'e': None, 'w': None}
    ),

    'foyer':    Room("foyer",
                     """Dim light filters in from the south. Dusty passages run north and east.""",
                     False,
                     [items["treasure"]]
                     #{'n': 'overlook', 's': 'outside', 'e': 'narrow', 'w': None}
    ),

    'overlook': Room("overlook",
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                     False,
                     [items["treasure"]]
                     #{'n': None, 's': 'foyer', 'e': None, 'w': None}
    ),

    'narrow':   Room("narrow",
                     """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                     True,
                     [items["lamp"]]
                     #{'n': 'treasure', 's': None, 'e': None, 'w': 'foyer'}
    ),

    'treasure': Room("treasure",
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
                     False,
                     [items["treasure"]]
                     #{'n': None, 's': 'narrow', 'e': None, 'w': None}
    ),
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

player_name = input("\nEnter your name: ") 
player = Player(player_name, room["outside"])

while True:
    action = input('input your action: ')
    secondary = action.split(" ")
    if len(secondary) >= 1 or len(secondary) <= 2:
        command = secondary[0]
        target = secondary[1] if len(secondary) == 2 else None
    if command == 'q' or command == 'quit':
        print("Thanks for playing!\n")
        break
    if command == 'inventory':
        print(f'You have [{" ".join(item.name for item in player.inventory)}]')
    if command == 'myname':
        print(f'your name is {player.name}')
    if command == 'mylocation':
        print(f'your location is {player.location}')
    if command == 'check':
        if room[player.location.name].is_light == True or player.has_item('lamp'):
            print('The room includes: ')
            print(room[player.location.name].inv())
        else:
            print(f'{player.inventory}')
            print('It\'s pitch black!')
    if command == f'take':
        if room[player.location.name].is_light == True or player.has_item('lamp'):
            new_item = items[target]
            room[player.location.name].item_picked_up(new_item)
            player.pickup_item(new_item)
        else:
            print('Good luck finding that in the dark')
    if command == f'drop':
         if not player.inventory:
            print('player inventory is empty')
         else:
            dropped_item = items[target]
            print(f'{dropped_item.name} was dropped')
            player.drop_item(dropped_item)
            room[player.location.name].item_dropped(dropped_item)
    if command == f'score':
        print(f'your score is {player.score}')

    player.location = player.try_move(command)
    print(f'You are in the {player.location.name}')