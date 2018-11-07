from room import Room
from player import Player
from item import Item
# Declare all the rooms


items = {
    'Knife': Item('Knife', 'A small cooking knife.', True),
    'Torch': Item('Torch', 'An unlit torch', True),
    'Matches': Item('Matches', 'Used for starting fires or lighting torches.'),
    'Rations': Item('Rations', 'Well-preserved food'),
    'Cigarettes': Item('Cigarettes', 'Adventuring can be stressful.'),
    'Pistol': Item('Pistol', 'A standard issue 9mm Pistol', True),
    'Ammunition': Item('Ammunition', 'Ammunition for 9mm weapons.', True)
}



room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items['Torch']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['Matches'], items['Knife']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['Cigarettes']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['Rations']]),
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



# initialize the player to be outside
player = Player(room['outside'])

#initialize a function to examine the room
def look(room, player):
    if len(room.items) == 0:
        print("====================\n You don't see anything useful here. \n ====================")
    if len(room.items) >= 1:
        print(f'==================== \n You notice the following:\n')
        for i in room.items:
            print(i.name + ': ' + i.description + '\n')
        print('====================')

def commands():
    print(f'Commands: [NORTH] [SOUTH] [EAST] [WEST]. \n Use [LOOK] to look around. \n Input [QUIT] to leave the game. \n Use [GET] and [DROP] to manage items.')

while True:

    #print command instructions
    print('Type "commands" to see full command list.')

    # print the current room
    print("==================== \n CURRENT ROOM:\n" + "  " + player.room.name + "\n" + "    " + player.room.description + "\n ====================")
    

    userInput = input(">>: ").split(' ')

    # parse the input if more than 2 commands
    if 1 <= len(userInput) <= 2:
        command = userInput[0]
        target = userInput[1] if len(userInput) == 2 else None


    if command.upper() == 'QUIT':
        break

    elif command.upper() == 'COMMANDS':
        commands()

    elif command.upper() == 'NORTH':
        if player.room.n_to:
            player.room = player.room.n_to
            print(f"\n You move north into the {player.room.name}. {player.room.description}")
        else:
            print("\n There is nowhere to move north.")
            continue

    elif command.upper() == 'SOUTH':
        if player.room.s_to:
            player.room = player.room.s_to
            print(f"\n You move south into the {player.room.name}. {player.room.description}")
        else:
            print('\n There is nowhere to move south.')
            continue

    elif command.upper() == 'EAST':
        if player.room.e_to:
            player.room = player.room.e_to
            print(f"\n You move ease into the {player.room.name}. {player.room.description}")
        else:
            print("\n There is nowhere to move east.")
            continue

    elif command.upper() == 'WEST':
        if player.room.w_to:
            player.room = player.room.w_to
            print(f"\n You move west into the {player.room.name}. {player.room.description}")
        else:
            print("\n There is nowhere to move west.")
            continue

    elif command.upper() == 'LOOK':
        look(player.room, player)

    elif command.upper() == 'GET':
        for item in player.room.items:
            if target == item.name:
                player.pickup(item)
                player.room.remove_item(item)
                print(f'You add the {item.name} to your inventory.')
            else:
                print(f'There is no {target} here.')

    elif command.upper() == 'DROP':
        for item in player.inventory:
            if target == item.name:
                player.drop(item)
                player.room.add_item(item)
                print(f'You drop the {item.name} in the {player.room.name}.')


    else:
        print("\n Unknown command, please try again.")
