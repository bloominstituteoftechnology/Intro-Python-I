from room import Room
from player import Player
from item import Item
# Declare all the rooms

items = {
    'potion': Item("potion-name",
                   "description"
    ),
    'sword': Item("excalibur",
                  "desc"
    )
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items["potion"]]
                     #{'n': 'foyer', 's': None, 'e': None, 'w': None}
    ),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty passages run north and east.""",
                     {}
                     #{'n': 'overlook', 's': 'outside', 'e': 'narrow', 'w': None}
    ),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                     {}
                     #{'n': None, 's': 'foyer', 'e': None, 'w': None}
    ),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                     {}
                     #{'n': 'treasure', 's': None, 'e': None, 'w': 'foyer'}
    ),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
                     {}
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
player_name = input("\nEnter your name: ") 
player = Player(player_name, room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

while True:
    print("Move around using north, south, east, & west")
    room["outside"].inv()
    direction = input('input your direction: ')
    secondary = direction.split(" ")
    if len(secondary) >= 1 or len(secondary) <= 2:
        command = secondary[0]
        target = secondary[1] if len(secondary) == 2 else None
    if command == 'q' or command == 'quit':
        print("Thanks for playing!\n")
        break
    if command == 'inventory':
        print(f'{" ".join(item.name for item in player.inventory)}')
    if command == 'myname':
        print(f'your name is {player.name}')
    if command == 'mylocation':
        print(f'your location is {player.location}')
    if command == 'myroom':
        print(f'room is {room[outside]}')
    if command == 'check':
        player.inventory = player.check_items(command)
        print(f'The room includes {player.inventory}')
    if command == f'take':

            new_item = items[target]
            room["outside"].item_picked_up(new_item)
            player.pickup_item(new_item)
    if command == f'dropped':
         if not player.inventory:
            print('player inventory is empty')
         else:
            new_item = items[target]
            player.drop_item(new_item)
            room['outside'].item_dropped(new_item)

    try:
        command = str(command)
    except ValueError:
        print('cannot do that')
        continue

    #print(player.location)
    #player.location = player.try_move(command)
    #print(f'You are in the {player.location.name}')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
