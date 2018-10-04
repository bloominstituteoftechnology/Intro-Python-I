from room import Room
from player import Player
from item import Item, Treasure, LightSource
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air. The wall to the east looks weird.""", False),

    'wall':   Room("Wall", """This wall looks out of place... Maybe if I try to push it...""", False),

    'hidden':   Room("Hidden Room", """A hidden room. Some sacrificial markings on the wall and ground. I better turn around.""", True),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['treasure']
room['narrow'].w_to = room['foyer']
room['narrow'].e_to = room['wall']
room['narrow'].n_to = room['treasure']
room['wall'].n_to = room['hidden']
room['wall'].w_to = room['narrow']
room['hidden'].s_to = room['wall']
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
bones = Item('bones', 'pile of bones')

#Treasures
gold = Treasure('gold', 'pile of gold', 100)
excalibur = Treasure("Excalibur", "Legendary sword of King Arthur", 10000)
ring = Treasure("Ring", "Seems to hold mysterious powers", 1000)

#LightSource
lamp = LightSource('lamp', 'a source of light')
player_items = ''.join(player.items)

player.add_item(rock)
room['outside'].add_item(pebble)
room['foyer'].add_item(ring)
room['foyer'].add_item(lamp)
room['narrow'].add_item(silver)
room['overlook'].add_item(gold)
room['treasure'].add_item(excalibur)
room['hidden'].add_item(bones)

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
    if player.room.is_light == True or any(isinstance(item, LightSource) for item in player.items) or any(isinstance(item, LightSource) for item in player.room.items):
        if len(player.room.items) > 0:
            print(f'\nItems available in this room: {player.room.items}')
        else:
            print(f'\nThere\'s nothing of interest in this room.')
    else:
        print(f'\nIt\'s pitch black!')
    print(f'\nYou are currently at {player.room}.')
    cmd = input("================================\nPress N, E, S or W to move.\nPress Q at any time to exit.\nPress I to view inventory.\nEnter get/take item_name to add item to inventory.\nEnter drop/remove item_name to remove item from inventory\nEnter score to view your current score\n================================\n-> ").lower().split()
    if len(cmd) == 1:
        if cmd[0] == 'score':
            print (f'\nYour score is {player.score}')
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
            for item in player_items:
                if item in player.room.items:
                    if player.room.is_light == True or any(isinstance(item, LightSource) for item in player.items) or any(isinstance(item, LightSource) for item in player.room.items):
                        player.add_item(item)
                        player.room.remove_item(item)
                        item.on_take(player)
                    else:
                        print(f'\nGood luck finding that in the dark!')
                else:
                    print('\nThe item is not available for pick up.')
        if cmd[0] == 'drop' or cmd[0] == 'remove':
            for item in player_items:
                if item in player.items:
                    player.items.remove(item)
                    player.room.add_item(item)
                    item.on_drop()
                else:
                    print('\nYou do not have that item in your inventory.')
    if player.score >= 9000:
        print(f'Congratulations! You won!')
        break
