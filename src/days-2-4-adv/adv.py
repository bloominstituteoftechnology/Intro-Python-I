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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

#Items
pebble = Item('pebble')
silver = Item('silver', '5 silver')
rock = Item('rock')

#Treasures
gold = Treasure('gold coins', 'pile of gold', 100)
excalibur = Treasure("Excalibur", "Legendary sword of King Arthur", 10000)
ring = Treasure("Ring", "Seems to hold mysterious powers", 1000)

player.add_item(rock)
room['outside'].add_item(pebble)
room['foyer'].add_item(ring)
room['narrow'].add_item(silver)
room['overlook'].add_item(gold)
room['treasure'].add_item(excalibur)

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
    print(f'\nHello, you are currently at {player.room}.')
    cmd = input("Press N, E, S or W to move.\nPress Q at any time to exit.\nPress I to view inventory.\nEnter get/take item_name to add item to inventory.\nEnter drop/remove item_name to remove item from inventory\n-> ").lower().split()
    if len(cmd) == 1:
        if cmd[0] == 'score':
            print (f'Your score is {player.score}')
        if cmd[0] == 'i' or cmd[0] == 'inventory':
            player.inventory()
        elif cmd[0] == 'q':
            break
        elif cmd[0] == "n":
            if hasattr( player.room , 'n_to' ):
                player.to(player.room.n_to)
            else:
                print('\nThe movement is not allowed.')
        elif cmd[0] == 's':
            if hasattr( player.room , 's_to' ):
                player.to(player.room.s_to)
            else:
                print('\nThe movement is not allowed.')
        elif cmd[0] == 'e':
            if hasattr( player.room , 'e_to' ):
                player.to(player.room.e_to)
            else:
                print('\nThe movement is not allowed.')
        elif cmd[0] == 'w':
            if hasattr( player.room , 'w_to' ):
                player.to(player.room.w_to)
            else:
                print('\nThe movement is not allowed.')
    elif len(cmd) > 1 and len(cmd) < 3:
        if cmd[0] == 'get' or cmd[0] == 'take':
            item = list(filter(lambda item: item.name.lower() == cmd[1].lower(), player.room.items))[0]
            if item in player.room.items:
                player.add_item(item)
                player.room.remove_item(item)
                item.on_take(player)
            else:
                print('\nThe item is not available for pick up.')
        if cmd[0] == 'drop' or cmd[0] == 'remove':
            item = list(filter(lambda item: item.name.lower() == cmd[1].lower(), player.items))[0]
            print(item)
            if item in player.items:
                player.items.remove(item)
                player.room.add_item(item)
            else:
                print('\nYou do not have that item in your inventory.')
