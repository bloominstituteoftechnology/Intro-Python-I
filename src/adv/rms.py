rooms0 = {
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
        "description": "A steep cliff appears before you, falling into the darkness.\nAhead to the north, a light flickers in the distance, but there is no way across the chasm.",
        "n_to": "level_up",
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
        "description": "You've found the long-lost treasure chamber. Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
        "s_to": "narrow",
    },
    "level_up": {
        "name": "Grand Overlook",
        "description": "You walk towards the flickering light to the north. As you step off the precipice, you realize that there is an impassable chasm as you fa",
        "level_up": True,
        "redirect": "outside",
    }
}

rooms1 = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim amber light filters in from the south. Passages run north and east. The passages seem to be less dusty somehow.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.\n\n...For some reason, the chasm seems interesting. If you stood at the edge of the precipice, you can feel it drawing you in ever so slightly.",
        "error": '''\nIt seems you cannot go that way...
(Remember, type in the cardinal direction you wish to move as a single lower-case letter. For example, type in 's'. Not all directions are valid. For example, 'n' is not a valid direction.)
It's not valid because you will fall and die if you type 'n'.
You can not choose to fall.
You can only choose to move in a valid cardinal direction.
\nTHERE IS NO OTHER CHOICE.\n''',
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The familiar smell of gold permeates the air, but it is being tainted by a sharper metallic smell. It smells...wetter.", 
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure chamber, and within it, there are mountains of treasure! 
Sadly, it has already been found. 
\n
Fortunately, the adventurers who found it are dead. Their corpses
are strewn about the chamber. A disembodied arm seeps blood onto
the piles of gold coins. How inconsiderate.
\n
The only exit is to the south.""",
        "s_to": "leave",
    },
    "leave": {
        "name": "Treasure Chamber",
        "description": "You begin to leave the chamber, when you feel a firm grip around your ankle. You look down to find the disembodied arm clinging steadfastly.\n It is not doing to this entrap you, but to point out something. It signals this intent by raising its bloodied calloused finger and wagging it at you.\n\nYou cannot choose to loot this room.\n\nIf you want this treasure,\nYOU MUST STAY.",
                "error": """\nIt seems you cannot go that way...
(Remember, type in the cardinal direction you wish to move as a single lower-case letter. Not all directions are valid. For example, type in 's'.)\n\n
You can't go north.
You can't go east.
You can't go west.
You can't pick up the gold.
You can't loot the dead bodies.
Remember, type in the cardinal direction SOUTH as a single lower-case letter 's'.\n""",
        "s_to": "level_up",
    },
    "level_up": {
        "name": "Treasure Chamber",
        "description": "You move south in an orderly manner. You're good at moving at cardinal directions, ar=-[>!:&?.*",
        "level_up": True,
        "redirect": "outside",
    } 
}

rooms2 = {
    "outside": {
        "name": "OUTSIDE",
        "description": "NO CONTENT",
        "error": "INVALID",
        "n_to": "foyer",
    },

    "foyer": {
        "name": "FOYER",
        "description": "NO CONTENT",
        "error": "INVALID",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "OVERLOOK",
        "description": """AHEAD TO THE NORTH, A LIGHT FLICKERS IN THE DISTANCE, BUT THERE IS THE WAY ACROSS THE CHASM.""",
        "error": "INVALID",
        "n_to": "level_up",
        "s_to": "foyer",
    },

    "narrow": {
        "name": "NARROW",
        "description": "NO CONTENT", 
        "error": "INVALID",
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "TREASURE",
        "description": "NO CONTENT",
        "error": "INVALID",
        "s_to": "narrow",
    },
    "level_up": {
        "name": "---",
        "description": "You enter a dimly lit room. At first, you thought you see shadows on the floor, but after your eyes adjust, you see what seems like bodies covered in a black cloaks.\nYou realize a figure in a dark cloak stands near a burning candle northwest of you. With a few flickers of candlelight, a look of realization creeps across your face. You move straight towards the figure.\n\nIt is you.\n\nYou smile warmly.\n\n",
        "level_up": True,
        "redirect": 'outside',
    }
}

rooms3 = {
    "outside": {
        "name": "OUT_OF_RANGE",
        "description": "THERE IS VARIABILITY IN ACTIONS. THERE IS PREDICTABILITY IN OUTCOMES.",
        "error": "ALL INPUTS ARE VALID. NO CONTEXT EXISTS FOR VALIDITY OF OUTPUTS.",
        "n_to": "outside",
        "s_to": "outside",
        "e_to": "outside",
        "w_to": "outside",
    },
        "level_up": {
        "name": "OUT_OF_RANGE",
        "description": "THERE IS VARIABILITY IN ACTIONS. THERE IS PREDICTABILITY IN OUTCOMES.",
        "error": "ALL INPUTS ARE VALID. NO CONTEXT EXISTS FOR VALIDITY OF OUTPUTS.",
        "n_to": "outside",
        "s_to": "outside",
        "e_to": "outside",
        "w_to": "outside",
    }
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

rooms = {
    "0": rooms0,
    "1": rooms1,
    "2": rooms2,
    "3": rooms3
}