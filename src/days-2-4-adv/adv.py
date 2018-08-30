from room import Room
from player import Player
from items import Items, Treasure

# Declare all the rooms

room = {
    'outside':  Room("outside the cave entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("in the foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at the grand overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("in the narrow passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("inside the treasure chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Add items to two rooms

room['outside'].items.append(Items("shovel", "Enter \'take shovel\' to dig holes and defend yourself from zombies"))
room['foyer'].items.append(Items("flashlight", "Enter \'take flashlight\' and use it to illuminate the passages"))
room['treasure'].items.append(Treasure("gold", "Enter \'take gold\' thought it's not a chest full, you\'ve found something", "25"))
room['narrow'].items.append(Treasure("silver", "Enter \'take silver\' when there's silver, sometimes gold is near", "10"))
room['overlook'].items.append(Treasure("bronze", "Enter \'take bronze\' when there's bronze, sometimes silver is near", "5"))

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

player = Player(room['outside'])

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

print('\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
print('~ ~ ~ ~ ~ ~ Welcome to TAG, ~ ~ ~ ~ ~ ~ ~')
print('~ ~ ~ ~ the text adventure game! ~ ~ ~ ~')
print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
print('\nFollow the prompts - find the treasure.')

while True:

    print("\n                        _.--.")
    print("                    _.-'_:-'||")
    print("                _.-'_.-::::'||")
    print("           _.-:'_.-::::::'  ||")
    print("         .'`-.-:::::::'     ||")
    print("        /.'`;|:::::::'      ||_")
    print("       ||   ||::::::'     _.;._'-._")
    print("       ||   ||:::::'  _.-!oo @.!-._'-.")
    print("       \'.  ||:::::.-!()oo @!()@.-'_.|")
    # print("\n        \'.'-;|:.-'.&$@.& ()$%-'o.'\U||")
    print("          `>'-.!@%()@'@_%-'_.-o _.|'||")
    print("           ||-._'-.@.-'_.-' _.-o  |'||")
    # print("\n           ||=[ '-._.-\U/.-'    o |'||")
    print("           || '-.]=|| |'|      o  |'||")
    print("           ||      || |'|        _| ';")
    print("           ||      || |'|    _.-'_.-'")
    print("           |'-._   || |'|_.-'_.-'")
    print("            '-._'-.|| |' `_.-'")
    print("                '-.||_/.-'")

    print('\nYou are currently %s'  % (player.room.name))
    print('\n... %s' % (player.room.description))
    
    # Print room contents

    if len(player.room.items) > 0:
        for i in player.room.items:
            print('\nOn the ground you see a %s' % (i.name))
            print('\n... %s' % (i.description))

    # Player input prompt

    inp = input("\nDirections: \'n\'orth, \'e\'ast, \'s\'outh or \'w\'est\nActions: \'take [item]'\', \'drop [item]\' or \'q\'uit\nEnter a command: ").split(' ')
    
    # Single word commands

    if len(inp) == 1:

        if inp[0] in ['n', 's', 'e', 'w']:
            if hasattr(player.room, inp[0] + '_to'):
                player.room = getattr(player.room, inp[0] + '_to')
            else:
                print('\nTHOUGH SHALL NOT PASS. TRY A DIFFERENT DIRECTION.')

        elif inp[0] == 'i':
            if len(player.items) == 0:
                print('\n You aren\'t carrying anything')
            else:
                print('\n You\'re carrying: %s' % (player.items))

        elif inp[0] == 'score':
            if player.score == 0:
                print('\nScore some points before asking - your score is 0!')
            else:
                print('\n Your score is %s' % (player.score))
        
        elif inp[0] == 'q':
            print('\nQuitting game...\n')
            break

            print("\nINVALID INPUT, PLEASE ENTER A DIRECTION OR AN ACTION")

    # Two word commands
    
    if len(inp) == 2:

        if inp[0] == 'take':
            current_item = [item for item in player.room.items if item.name == inp[0]]
            player.addItem(current_item)
            print(player.items)
            print(player.room.items)
            player.room.removeItem(player.room.items[0]) 
            # what happens if there is more than one item in the list?
            # how can we find the removeItem(item) by name instead?
            print('\nYou are now carrying the %s' % (inp[1]))

        if inp[0] == 'drop':
            print(inp[1])
            player.room.addItem(inp[1])
            
            player.removeItem(player.items[0]) 
            print('\nYou are no longer carrying the %s' % (inp[1]))
            