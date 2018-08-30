from classes import Room
from classes import Item

item = {
    'knife': Item('knife'),
    'coin': Item('coin'),
    'shield': Item('shield')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [item['knife'], item['shield']],
                    {'n': 'foyer', 's': None, 'w': None, 'e': None}),

    'foyer':    Room("Foyer",
                    """Dim light filters in from the south. Dusty passages run north and east.""",
                    [],
                    {'n': 'overlook', 's': 'outside', 'w': None, 'e': 'narrow'}),

    'overlook': Room("Grand Overlook",
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                    [],
                    {'n': None, 's': 'foyer', 'w': None, 'e': None}),

    'narrow':   Room("Narrow Passage",
                    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                    [],
                    {'n': 'treasure', 's': None, 'w': 'foyer', 'e': None}),

    'treasure': Room("Treasure Chamber",
                    """You've found the long-lost treasure chamber! Sadly, it has already been almost completely emptied by earlier adventurers. The only exit is to the south.""",
                    [item['coin']],
                    {'n': None, 's': 'narrow', 'w': 'foyer', 'e': None})
}
