from room import Room
from player import Player
from item import Item
# Declare all the rooms
items = {
    'sword': Item('Sword', '+10 Attack'),
    'shield': Item('Shield', '+5 Defense'),
    'armor': Item('Armor', '+3 Defense'),
    'pants': Item('Pants', '+2 Defense'),
    'dagger': Item('Dagger', '+5 Attack'),
    'bracers': Item('Bracers', '+1 Defense'),
    'potion': Item('Potion', 'Restore 5hp'),
    'bandage': Item('Bandage', 'Restore 2hp'),
    'diamond': Item('Diamond', 'can be traded for 1000 gold'),
    'revivepotion': Item('RevivePotion', 'can revive player 1 time')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons""",
                     [items['sword'], items['bandage']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [items['shield'], items['pants']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [items['armor'], items['dagger']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [items['bracers'], items['potion']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [items['diamond'], items['revivepotion']]),
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
player1 = Player('Stormer', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#('Which direction to do you want to go to (N,S,W,E)?')
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f'\n=== Welcome to the epic MUD game, {player1.name} ===\n')
while True:
    print(f'\nCurrent location:  {player1.location.name}.')
    print(player1.location.description + '\n')
    print(f'Items found: {[i.name for i in player1.location.items]}\n')

    direction = input('Which direction to do you want to go to (N,S,W,E)?')

    if direction.lower() == 'q':
        print('\nGoodbye! Please come again.\n')
        break
    else:
        try:
            if direction.lower() == 'n':
                player1.location = player1.location.n_to
            elif direction.lower() == 's':
                player1.location = player1.location.s_to
            elif direction.lower() == 'w':
                player1.location = player1.location.w_to
            elif direction.lower() == 'e':
                player1.location = player1.location.e_to
            else:
                print('\nPlease enter a valid direction.')
        except:
            print('\nThere is no room in this direction. Please try again!')