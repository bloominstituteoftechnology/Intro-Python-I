rooms = {
  "outside": {
    "name": "Outside Cave Entrance",
    "description": "North of you, the cave mouth beckons.",
    "n_to": "foyer",
  },

  "foyer": {
    "name": "Foyer",
    "description": "Dim light filters in from the south. Dusty passages run north and east.",
    "n_to": "overlook",
    "s_to": "outside",
    "e_to": "narrow",
  },

  "overlook": {
    "name": "Grand Overlook",
    "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    "s_to": "foyer",
  },

  "narrow": {
    "name": "Narrow Passage",
    "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
    "w_to": "foyer",
    "n_to": "treasure",
  },

  "treasure": {
    "name": "Treasure Chamber",
    "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    "s_to": "narrow",
  },

}

""" template room to copy into code
  "room": {
    "name": "",
    "description": "",
    "n_to": "",
    "s_to": "",
    "e_to": "",
    "w_to": "",
  },
"""