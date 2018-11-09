from room import Room 
from item import Item
from item import Treasure
from item import LightSource

# Define items
item = {
    'scroll': Item('Scroll', 'A rolled-up piece of old paper'),
    'dictionary': Item('Dictionary', 'An old dusty book with lots of words in it'),
    'holy_grail': Treasure('Holy Grail', 'A golden chalice',100),
    'map': Item('Map', 'A map of the building'),
    'first-aid_kit': Item('First-aid Kit', 'A box of bandages and oitments for patching the wounds.'),
    'ring': Treasure('Ring', 'A golden ring',10),
    'diamond': Treasure('Diamond', 'A ridiculously large piece of diamon',50),
    'lamp': LightSource('lamp', 'An oil lamp')
}

#Define rooms, their descriptions, and initial items found
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['scroll'], item['dictionary']], True),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", [item['ring'], item['lamp']]),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you,falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", []),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.",[item['diamond']]),

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


