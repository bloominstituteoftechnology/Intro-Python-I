from room import Room
from player import Player
from item import Item, Treasure, LockedItem, LightSource
# create rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", True),
    'secret room': Room('Secret Room', """A secret room...search it and see what you find...""", False),
    'strange room': Room('Strange Room', "There is no floor...you are floating over a great chasm...", False)
}

# create items
note = Item('note', 'a note with >>> 2 3 1 <<< written on it')
key = Item('key', 'a small key with a dragon head')
torch = Item('torch', 'illuminates dark places')
mirror = Item('mirror', 'a small mirror')
flint = Item('flint', 'used for making fire')

game_items = {
    'torch': Item('torch', 'illuminates dark places'),
    'key': Item('key', 'small key with dragon head'),
    'note': Item('note', '>>>> 2 3 1 <<<<'),
    'chest': LockedItem('treasure chest', 'shut with a combination lock expecting three numbers', note),
    'lockedDoor': LockedItem('locked door', 'a locked door with a dragon on it', key),
    'curtains': LockedItem('curtains', """
    some old curtains with flame symbols on them hang on the wall to the east...strange...
    """, torch),
    'strange statue': LockedItem('Statue', 'A statue of a woman looking at herself in a mirror...the mirror is broken...', mirror)
}

# place items in room
room['foyer'].items.append(game_items['torch'])
room['overlook'].items.append(game_items['key'])
room['narrow'].items.append(game_items['note'])
room['treasure'].items.append(game_items['lockedDoor'])
room['secret room'].items.append(game_items['chest'])
room['strange room'].items.append(game_items['curtains'])


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['overlook'].s_to = room['foyer']
room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

new_player_message = """
****************************************************************************************************************
                                     WELCOME TO THE SUPER ADVENTURE GAME
                                        ENTER A NAME FOR YOUR HERO
****************************************************************************************************************
>>> """

name = input(new_player_message)
player = Player(name, room['outside'])
player.items.append(flint)
player.items.append(mirror)
print(player.items)