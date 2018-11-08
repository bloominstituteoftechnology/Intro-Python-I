# day 1 - 4 is MVP complete and done some stretch goals. making up some more stretch
from room import Room
from player import Player
from item import Item
from treasure import Treasure
from lightsource import LightSource
from potion import Potion
from computer import Computer
from subprocess import call


## declare some items [ will elaborate and subclass some of these later ]
items = {
    "L115a": Item("L115a"),
    "AK47": Item("AK47"),
    "Stiletto": Item("Stiletto"),
    "C4": Item("C4"),
    "katana": Item("katana"),
    "notepad": Item("notepad"),
    "JohnWick": Item("JohnWick"),
    "torch": LightSource("torch"),
    "ingot": Treasure("ingot", 120),
    "potion": Potion("potion", 100),
    "laptop": Computer("laptop"),
    "qwill": Item("qwill"),
    "pigeon": Item("pigeon")
}

# globals are bad mkay
global has_computer
has_computer = False
# Declare all the rooms

room = {
    'outside':  Room(
                    "Outside Cave Entrance",
                    "North of you, the cave mount beckons.",
                    True,
                    [items['katana'], items['notepad'], items['torch']],
                    {'north': 'foyer', 'south': None, 'east': None, 'west': None},
                    ),

    'foyer':    Room(
                    "Foyer",
                    """Dim light filters in from the south. Dusty passages run north and east.""",
                    False,
                    [items['potion'], items["laptop"]],
                    {'north': 'overlook', 'south': 'outside', 'east': 'narrow', 'west': None},
                    ),

    'overlook': Room(
                    "Grand Overlook",
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                    False,
                    [],
                    {'north': None, 'south': 'foyer', 'east': None, 'west': None}
                    ),

    'narrow':   Room(
                    "Narrow Passage",
                    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                    False,
                    [items['qwill']],
                    {'north': 'treasure', 'south': None, 'east': None, 'west': 'foyer'},
                    ),

    'treasure': Room(
                    "Treasure Chamber",
                    """You've found the long-lost treasure chamber! Sadly, it has already been almost completely emptied by earlier adventurers. The only exit is to the south.""",
                    False,
                    [items['ingot'], items['pigeon']],
                    {'north': None, 'south': 'narrow', 'east': None, 'west': 'foyer'},
                    ),
    'endgame': Room(
                    "The End",
                    """You have completed the demo! Well done, you can fork and clone this game and build upon it as you see fit""",
                    False,
                    [],
                    {'north': None, 'south': None, 'east': None, 'west': None},
                    )
}

# Link rooms together - refactored directions

room['outside'].north_to = room['foyer']
room['foyer'].south_to = room['outside']
room['foyer'].north_to = room['overlook']
room['foyer'].east_to = room['narrow']
room['overlook'].south_to = room['foyer']
room['narrow'].west_to = room['foyer']
room['narrow'].north_to = room['treasure']
room['treasure'].south_to = room['narrow']

# helper functions

# log errors in an orange colour ref: https://bixense.com/clicolors/
def logError(err):
    print(f'\x1b[1;33;40m\n{err}\x1b[0m')

# print current room details
def print_current_room_details(room):
    print("\n You are in the %s" % (room))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# instantiate player object with a starting room
player = Player(room['outside'])

# Main game loop:
while True:
    # print the current room details formatted and coloured
    print("\n\x1b[1;36mYou are in the {}.".format(player.room.name))
    if player.room.has_light or player.check_for_light():
        print(player.room.description)
        if player.room.items:
            player.room.list_items()
    else:
        logError("I can't see a thing! If only we had some sort of lamp like object to light the way")

    # * Waits for user input and decides what to do. add the ability to parse multi word commands
    in_cmd = input("\n:>> ").split(" ")
    if 1 <= len(in_cmd) <= 2:
        command = in_cmd[0]
        target = in_cmd[1] if len(in_cmd) == 2 else None

    # If the user enters "q", quit the game.
    if command.upper() == "QUIT":
        break
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif command.upper() == "NORTH":
        # logic for move north
        if player.room.north_to:
            player.room = player.room.north_to

    elif command.upper() == "SOUTH":
        # logic for move south
        if player.room.south_to:
            player.room = player.room.south_to

    elif command.upper() == "EAST":
        # logic to move east
        if player.room.east_to:
            player.room = player.room.east_to

    elif command.upper() == "WEST":
        # logic to move west
        if player.room.west_to:
            player.room = player.room.west_to

    elif command == "inventory" or command == "i":
            if player.items:
                player.inventory()

    elif command == "get":
            if not player.room.items:
                logError("There are no items in your grasp. maybe we need to rethink this!")
            elif not player.room.check_for_item(target):
                logError("These are not the Items you are looking for.")
            else:
                new_item = items[target]
                player.room.remove_item(new_item)
                player.get(new_item)
                if isinstance(new_item, Treasure):
                    if not new_item.picked_up:
                        player.gold += new_item.value
                        new_item.on_take()
    
    elif command == "drink":
        consumable = items[target]
        if isinstance(consumable, Potion):
            consumable.on_use(player)
        else:
            logError("\nyou can't drink that!\n")
    elif command == "power":
        pc = items[target]
        if isinstance(pc, Computer):
            pc.on_use(target)
            has_computer = True
        else:
            logError("\nyou can't power that up!\n")
    elif command == "drop":
            if not player.items:
                logError("You rummage in your knapsack but find nothing! You may need to rething your life choices and preperation skills at this point!")
            elif not player.check_for_item(target):
                logError("on closer inspection the knapsack does not contain this item.")
            else:
                dropped_item = items[target]
                player.drop(dropped_item)
                player.room.add_item(dropped_item)
                if isinstance(dropped_item, LightSource):
                    dropped_item.on_drop()

    # tell me the truth
    elif command.upper() == "THETRUTH":
        print("\nYOU CAN'T HANDLE THE TRUTH!\n")
    elif command.upper() == "PING":
        if has_computer:
            call(["ping", str(target)])
        else:
            logError("ping? PING? What? Do you think you have some sort of computer or something?!?")

    elif command.upper() == "CLEAR":
        if has_computer:
            call(["clear"])
        else:
            logError("what exactly are you expecting to clear? some sort of screen??!?")

    elif command.upper() == "BROWSE":
        if has_computer:
            call(["chrome", str(target)])
        else:
            logError("browse? What? anyone would think that the internet had been invented?!?")

    elif command == "gold":
            player.check_gold()

    elif command == "help":
            print("\x1b[1;32;40m\nLIST OF COMMANDS\n----------------\n[north] = move north\n[south] = move south\n[east] = move east\n[west] = move west\n[get <item>] = pick up an item\n[drop <item>] = drop an item\n[quit] = give up the game\n[help] = this text\x1b[0m")

    # Print an error message if the movement isn't allowed.
    else:
        print("\nUnknown command!\n")
