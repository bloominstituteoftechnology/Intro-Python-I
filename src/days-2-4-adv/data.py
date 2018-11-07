from room import Room 
from item import Item 

# Define items
item = {
    'scroll': Item('Scroll', 'A rolled-up piece of old paper'),
    'dictionary': Item('Dictionary', 'An old dusty book with lots of words in it'),
    'holy_grail': Item('Holy Grail', 'A golden chalice')
}

#Define rooms and their descriptions
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['scroll'], item['dictionary']]),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", []),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you,falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", []),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.",[]),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",[item['holy_grail']]),
}

#Define moves from each room
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Define items in each room at start of game


