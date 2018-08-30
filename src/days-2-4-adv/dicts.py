from classes import Room
from classes import Item
from classes import Treasure
from classes import LightSource

item = {
    'knife': Item('knife'),
    'coin': Treasure('coin', 75),
    'shield': Item('shield'),
    'lamp': LightSource('lamp')
}

room = {
    'outside':  Room(
                    "Outside Cave Entrance",
                    "North of you, the cave mount beckons.",
                    True,
                    [item['knife'], item['shield'], item['lamp']],
                    {'n': 'foyer', 's': None, 'w': None, 'e': None},
                    ),

    'foyer':    Room(
                    "Foyer",
                    """Dim light filters in from the south. Dusty passages run north and east.""",
                    False,
                    [],
                    {'n': 'overlook', 's': 'outside', 'w': None, 'e': 'narrow'},
                    ),

    'overlook': Room(
                    "Grand Overlook",
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                    False,
                    [],
                    {'n': None, 's': 'foyer', 'w': None, 'e': None}
                    ),

    'narrow':   Room(
                    "Narrow Passage",
                    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                    False,
                    [],
                    {'n': 'treasure', 's': None, 'w': 'foyer', 'e': None},
                    ),

    'treasure': Room(
                    "Treasure Chamber",
                    """You've found the long-lost treasure chamber! Sadly, it has already been almost completely emptied by earlier adventurers. The only exit is to the south.""",
                    False,
                    [item['coin']],
                    {'n': None, 's': 'narrow', 'w': 'foyer', 'e': None},
                    )
}
