from room import Room
from player import Player
from item import Item, Treasure

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

sword = Item('sword', 'finest steel')
room['overlook'].items.append(sword)

shield = Item('shield', 'heavy duty')
room['narrow'].items.append(shield)

helmet = Item('helmet', 'partially crushed')
room['foyer'].items.append(helmet)

gold = Treasure('gold', 'gold bar')
room['treasure'].items.append(gold)

diamonds = Treasure('diamonds', 'satchel of diamonds')
room['overlook'].items.append(diamonds)

rubies = Treasure('rubies', 'bag of rubies')
room['narrow'].items.append(rubies)

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

def move(direction, presentRoom):
    attr = str(direction) + '_to'
    if hasattr(presentRoom, attr):
        return getattr(presentRoom, attr)
    print('wrong way')
    return presentRoom

def retrieve(name, itemLocation):
    for item in itemLocation.items:
        if item.name == name:
            return item

running = True

while running:
    print("\n{}\n{}".format(player.room.name, player.room.description))

    print("\nItems in the room:")
    for item in player.room.items: 
        print(item.name)

    print('\nNext move: ')
    inp = input().split()
    if len(inp) < 1 or len(inp) > 2:
        print('Unknown Command')
    if len(inp) == 1:
        if inp[0] in ['n', 's', 'e', 'w']:
            player.room = move(inp[0], player.room)
        elif inp[0] == 'q':
            running = False
        elif inp[0] == 'i':
            if len(player.items) == 0:
                print("\nYou don't have anything")
            else:
                print("\nYou have:")
                for item in player.items:
                    print("{}".format(item.name))
        elif inp[0] == 'score':
            print("\nYou're score is {}.".format(player.score))
        else:
            print('Unknown Command')
            print('Enter n, s, e, or w for desired direction or i for inventory or q to quit')
            
    elif len(inp) == 2:
        if inp[0] == 'take':
            item = retrieve(inp[1], player.room)
            if item == None:
                print("That's not here")
            else:
                player.room.items.remove(item)
                player.items.append(item)
        elif inp[0] == 'drop':
            item = retrieve(inp[1], player)
            if item == None:
                print("You don't have that")
            else:
                player.items.remove(item)
                player.room.items.append(item)
        else:
            print('\nUnknown Command')
            print("Enter 'take' or 'drop' to take or drop an item")