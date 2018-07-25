from room import Room  # importing room object
from player import Player
from item import Item

# Declare all the rooms

items = {
    'outside': Item([
        {
            "stick": "An ordinary stick"
        },
        {
            "Garden hose": "A coil of green rubber"
        },
        {
            "Shovel": "A basic digging tool, a spaed."
        }
    ],
    [
        {
            "stick": "An ordinary stick"
        },
        {
            "Garden hose": "A coil of green rubber"
        },
        {
            "Shovel": "A basic digging tool, a spaed."
        }
    ]),
    'foyer': Item([
        {
            "knife": "A cold steel blade. Good for cutting"
        },
        {
            "broom": "A cleaning tool. Sweepsome dust if you would like"
        },
        {
            "display sword": "A flimsy sword on display"
        },
        {
            "Ceramic bowl": "Make some soupwhy dont you?"
        }
    ],
    [
        {
            "knife": "A cold steel blade. Good for cutting"
        },
        {
            "broom": "A cleaning tool. Sweep some dust if you would like"
        },
        {
            "display sword": "A flimsy sword on display"
        },
        {
            "Ceramic bowl": "Make some soupwhy dont you?"
        }
    ]),
    'overlook': Item([
        {
            "Flower Pot": "Seems useless. A ceramic bowl for plants"
        },
        {
            "Pouch of coins": "A small leather pouch with 5 silver coins. Could be useful"
        },
        {
            "Small lantern": "An oil lantern, need a light?"
        },
    ],
    [
        {
            "Flower Pot": "Seems useless. A ceramic bowl for plants"
        },
        {
            "Pouch of coins": "A small leather pouch with 5 silver coins. Could be useful"
        },
        {
            "Small lantern": "An oil lantern, need a light?"
        },
    ]),
    'narrow': Item([
        {
            "Metal bar": "Heavy, and blunt. The perfect weapon... For trolls..."
        },
        {
            "Small dagger": "A bronze dagger, a stabby tool"
        }
    ],
    [
        {
            "Metal bar": "Heavy, and blunt. The perfect weapon... For trolls..."
        },
        {
            "Small dagger": "A bronze dagger, a stabby tool"
        }
    ]),
    'treasure': Item([
        {
            "Empty chest": "Drats. Someonefound this first... thats too bad"
        },
        {
            "Note": "A note from the person who cleaned this place out, its a map to the new location!"
        },
        {
            "Single gold coin": "All is not lost it seems.."
        }
    ],
    [
        {
            "Empty chest": "Drats. Someonefound this first... thats too bad"
        },
        {
            "Note": "A note from the person who cleaned this place out, its a map to the new location!"
        },
        {
            "Single gold coin": "All is not lost it seems.."
        }
    ])
}


#dictionary called room
room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons""", items['outside'], items['outside']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items['foyer'], items['foyer']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items['overlook'], items['overlook']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items['narrow'], items['narrow']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items['treasure'], items['treasure']),
}


# Link rooms together
#
room['outside'].n_to = room['foyer'] #north_to connector pointing to foyer
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main

# Make a new player object that is currently in the 'outside' room.

new_player = Player("Endor", room['outside'])

# Write a loop that:

# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.

# If the user enters "q", quit the game.

done = False

while not done:
    current_room = new_player.startRoom
    print(f'{current_room.name}\n{current_room.description}')


    
    command = input("Command> ").strip().lower()

    if command == 'q' or command == 'quit' or command == 'exit':
        done == True
        print(current_room.name)

    elif command in ["s", "n", "e", "w"]:
        dirAttr = command + "_to"

        if hasattr(current_room, dirAttr):
            new_player.current_room = getattr(current_room, dirAttr)
        else:
            print("You can't go that way\n")

    else:
        print("I dont understand that command!")