import textwrap
# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.
commands = {
    "n e s w": "Use these to navigate the map",
    "q or quit": "Quit the game",
    "get [item]": "Acquire an item and add to inventory",
    "check bag": "Check the contents of your inventory"
}

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "contents": [],
        "n_to": "foyer",
        "q_to": "catSanctuary",
    },

    "foyer": {
        "name": "Foyer",
        "description": """Dim light filters in from the south.
Dusty passages run north and east.""",
        "contents": ["hope"],
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "contents": [],
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": """The narrow passage bends here from
west to north. The smell of gold permeates the air.""",
        "contents": [],
        "w_to": "foyer",
        "n_to": "treasure"
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "contents": ["treasure"],
        "s_to": "narrow",
    },
    "catSanctuary": {
        "name": "Cat Sanctuary",
        "description": """Your quest has ended and you are at peace,
surrounded by cats""",
        "contents": [],
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
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

# Write a class to hold player information,
# e.g. what room they are in currently


class Player:
    """information about player"""
    def __init__(self, start):
        self.currentRoom = start
        self.inventory = []


def direction(option, currentRoom):
    """player movement """
    key = option + "_to"
    keys = ("n_to", "s_to", "w_to", "e_to", "q_to")
# keys is a tuple of all the keys I wanted as options in options
# In options, I only used keys in rooms[currentRoom] that were in keys
# I then called the keys method on the dictionary to get only the key names
# That resulted in options printing as "dict_keys: [key]"
# So I wrapped that in a list so that it would not display dict_keys:
# fixedOptions then takes the "_to" part off the keys in options
#   (surprisingly, the thing that took the most time was that last part)
    options = list(
        dict((k, rooms[currentRoom])
             for k in keys if k in rooms[currentRoom]).keys())
    fixedOptions = [s.strip("_to") for s in options]

    if key not in rooms[currentRoom]:
        print("""You cannae go that way!
        Your options are: %s""" % fixedOptions)
        return currentRoom

    destination = rooms[currentRoom][key]
    return destination


def contents(currentRoom):
    items = rooms[currentRoom]['contents']
    return items
#
# Main
#

# Make a new player object that is currently in the 'outside' room.


player = Player('outside')


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * User prompt
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
quit = False

while not quit:
    print("""\nThe room you are in is:
    \n*** {} ***\n""".format(rooms[player.currentRoom]['name']))
# Added indent for description so that it stands out more
    for line in textwrap.TextWrapper(
        drop_whitespace=False,
        initial_indent="  ",
        subsequent_indent="  ").wrap(
             rooms[player.currentRoom]['description']):
        print(line + '\n')

    if rooms[player.currentRoom]['contents'] != []:
        for item in rooms[player.currentRoom]['contents']:
            print("""\nIn the room, you find:\n
{}\n""".format(item))

    if player.currentRoom == "catSanctuary":
        print("""
\n************** YOU WON THE GAME *******************\n
                                 .''.
       .''.             *''*    :_\/_:     .
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\n*************** YOU WON THE GAME! *****************\n""")
        quit = True
        break

    text = input("What is thy command?> ").lower()
    if text[0:3] == "get":
        if text[4:12] == 'treasure':
            print("\nYou got treasure!")
            player.inventory.append('treasure')
            rooms[player.currentRoom]['contents'].remove('treasure')
        if text[4:9] == "hope":
            print("\nHope acquired!")
            player.inventory.append('hope')
            rooms[player.currentRoom]['contents'].remove('hope')
            rooms['foyer']['w_to'] = "catSanctuary"
            rooms['foyer']['description'] = """A cat sanctuary?!
Move to the west to investigate."""
    elif text == "q":
        quit = True
    elif text == "check bag":
        if player.inventory != []:
            print("""\nContents of your bag:\n
{}""".format(player.inventory))
        else:
            print('Your pockets are empty')

    elif text in ["n", "s", "w", "e"]:
        player.currentRoom = direction(text, player.currentRoom)

    elif text not in ["n", "s", "w", "e", "q"]:
        print("{} is a command unknown to me".format(text))
