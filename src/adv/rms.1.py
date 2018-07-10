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
        "description": "A steep cliff appears before you, falling into the darkness.\nAhead to the north, a light flickers in the distance, but there is no way across the chasm.",
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
        "description": "You've found the long-lost treasurechamber. Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
        "s_to": "narrow",
    },
    "level_up": {
        "name": "Grand Overlook",
        "description": "You walk towards the flickering light to the north. As you step off the precipice, you realize that there is an impassable chasm as you fa",
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
        "s_to": "level_up",
    },
    "level_up": {
        "name": "Treasure Chamber",
        "description": "You begin to leave the chamber, when you feel a firm grip around your ankle. You look down to find the disembodied arm clinging steadfastly.\n It is not doing to this entrap you, but to point out something. It signals this intent by raising its bloodied calloused finger and wagging it at you.\n\nYou cannot choose to loot this room.\n\n(Remember, the only valid input that exists is 'n', 's', 'e', 'w')\n\nIf you want this treasure,\nYOU MUST STAY.",
        "n_to": "outside",
        "s_to": "outside",
        "e_to": "outside",
        "w_to": "outside",
    } 
}

rooms2 = {
    "outside": {
        "name": "OUTSIDE",
        "description": "NO CONTENT",
        "n_to": "foyer",
    },

    "foyer": {
        "name": "FOYER",
        "description": "NO CONTENT",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "OVERLOOK",
        "description": """AHEAD TO THE NORTH, A LIGHT FLICKERS IN THE DISTANCE, BUT THERE IS THE WAY ACROSS THE CHASM.""",
        "n_to": "level_up",
        "s_to": "foyer",
    },

    "narrow": {
        "name": "NARROW",
        "description": "NO CONTENT", 
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "TREASURE",
        "description": "NO CONTENT",
        "s_to": "narrow",
    },
    "level_up": {
        "name": "",
        "description": "You see a figure in the dimly lit room. As the light flickers across the figure's face, you realize it is you."
    }
}

rooms3 = {
    "outside": {
        "name": "OUT_OF_RANGE",
        "description": "THERE IS VARIABILITY IN ACTIONS. THERE IS PREDICITABILITY IN OUTCOMES.",
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