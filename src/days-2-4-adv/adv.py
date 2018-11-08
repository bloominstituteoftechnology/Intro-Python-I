from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms
item = {
    'item1': Item('This is a thing', 
                    "this is a description")
}
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item['item1']),
                

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['item1']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['item1']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['item1']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['item1']),
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

# room['outside'].items.append(Item('Garbage', 'Why would you pick this up?'))
# room['treasure'].items.append(Item('McDonald\'s Monopoly Park Place sticker', 'Oh my god! You\'ll be rich!'))
# #
# # Main
#

# Make a new player object that is currently in the 'outside' room.

 


player = Player('tom', room['outside'], [])

 

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.

# print (player.room)
 

# Rooms are initiliazed with no items. To add them, use the
# Room.add_items(*items) method. You may pass in a  list,
# individual items, or a combination of both
# e.g. Room.add_items('sword', 'shield', ['treasure, 'crown', 'chalice'])



while True:
    print (' ')
    print ('Your current location:', player.room.name)
    print ( textwrap.wrap(player.room.description) )
    print(player.room.items)
    # if len(player.room.items) > 0:
    #     for item in player.room.items: 
    #         print("You spot a {item}. {description}".format(item=item.item_name, description=item.description))
    move = raw_input('Input your next move: ')
    
    try:
       move = move.lower()
       print('the move is ' + move)
    except AttributeError:
        print('Please enter a direction to move next')
        continue
    if move in ['n', 'e', 's', 'w', 'q', 'get']:
        if move == 'n':
            try:
                player.room = player.room.n_to
            except AttributeError:
                print('You may not move in that direction. Try again')
                continue
        elif move == 'e':
            try:
                player.room = player.room.e_to
            except AttributeError:
                print('You may not move in that direction. Try again')
                continue
        elif move == 's':
            try:
                player.room = player.room.s_to
            except AttributeError:
                print('You may not move in that direction. Try again')
                continue
        elif move == 'w':
            try:
                player.room = player.room.w_to
            except AttributeError:
                print('You may not move in that direction. Try again')
                continue
        elif move =='get':
            try:
                print(len(player.inventory))
                player.inventory.append(player.room.items) 
                print(len(player.inventory)) 
                print(player)


                # print(room.item)
            except AttributeError:
                print('You were not able to pick up the item. Choose a direction to proceed') 
                continue       
        elif move == 'q':
            break
    else:
        print('Please enter a cardinal direction or "q" to quit')
