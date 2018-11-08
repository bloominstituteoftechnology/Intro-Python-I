from room import Room
from player import Player
from item import Item
# Declare all the rooms


items = {
    'Knife': Item('Knife', 'A small cooking knife.', True),
    'Torch': Item('Torch', 'An unlit torch', True),
    'Matches': Item('Matches', 'Used for starting fires or lighting torches.'),
    'Rations': Item('Rations', 'Well-preserved food'),
    'Cigarettes': Item('Cigarettes', 'Adventuring can be stressful.'),
    'Pistol': Item('Pistol', 'A standard issue 9mm Pistol', True),
    'Ammunition': Item('Ammunition', 'Ammunition for 9mm weapons.', True),
    'Rusty Key': Item('Rusty Key', "A key that looks like it's spent a lot of time outdoors."), # key to the shed
    'Shiny Key': Item('Shiny Key', "A key that looks like it opens an important room."), # key to the master bedroom
    'Globe': Item('Globe', "A large globe with hardware meant to mount it on something..."), # globe for garden statue
    'Book': Item('Book', "A weathered tome that is unusually heavy.")
}



room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the estate manor beckons. A small garden plot lays to the east."""),

    'garden': Room('Garden', """A small plot of plants that has been overgrown by weeds. There is a large Atlas statue in the middle, and a shed to the north.""", [items['Torch']]),

    'foyer': Room("Foyer", """Dim light filters in from the south. You see doorways to the north, east, and west. A cold draft blows from the west...""", [items['Matches']]),

    'shed': Room("Garden Shed", """Dust floats through the air, and rusty tools are strewn about the inside. Doors lead out to the west and south.""", [items["Book"]], True),

    'basement': Room("Musty Basement", """A damp, moldy basement, dressed with cobwebs. A freezing cold wind blows from the south...""", None, True),

    'dungeon': Room("Dungeon of Horrors", """Blood soaks the floors and walls, and a menacing figure stands in the middle!"""),

    'greathall': Room("Great Hall", """A large hall filled with classic artwork. Passages extend to the east and west, and a staircase winds to the north."""),

    'diningroom': Room("Dining Room", """A large wooden table runs the length of the room, and dust has settled on the plateware. You hear water dripping to the north.""", [items["Rusty Key"]]),

    'kitchen': Room("Kitchen", """An old sink is leaking in the corner of this fully-stocked kitchen.""", [items['Knife']]),

    'library': Room("Library", """Old books line the walls, and a draft seems to be coming from the northern bookshelf."""),

    'secretpassage': Room("Secret Passageway", """A narrow hallway extends north to south. There seems to be an evil presence here...""", [items["Shiny Key"]]),

    'masterbed': Room("Master Bedroom", """A large bed lays undisturbed. A crooked painting hangs on the northern wall.""", None, True),

    'upstairs': Room("Upstairs Hall", """A carpeted corridor runs east to west, with a glass doorway heading north."""),

    'observatory': Room("Observatory", """Scientific instruments are laid about, with all sorts of papers and devices.""", [items["Globe"]]),

    'terrace': Room("Grand Terrace", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [items['Cigarettes']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].e_to = room['garden']
room['garden'].w_to = room['outside']
room['garden'].n_to = room['shed']
room['shed'].s_to = room['garden']
room['shed'].w_to = room['foyer']
room['foyer'].e_to = room['shed']
room['foyer'].s_to = room['outside']
room['foyer'].w_to = room['basement']
room['foyer'].n_to = room['greathall']
room['basement'].s_to = room['dungeon']
room['basement'].e_to = room['foyer']
room['dungeon'].n_to = room['basement']
room['greathall'].n_to = room['upstairs']
room['greathall'].e_to = room['diningroom']
room['greathall'].w_to = room['library']
room['greathall'].s_to = room['foyer']
room['diningroom'].n_to = room['kitchen']
room['diningroom'].w_to = room['greathall']
room['kitchen'].s_to = room['diningroom']
room['library'].n_to = room['secretpassage']
room['library'].e_to = room['greathall']
room['upstairs'].s_to = room['greathall']
room['upstairs'].w_to = room['masterbed']
room['upstairs'].e_to = room['observatory']
room['upstairs'].n_to = room['terrace']
room['terrace'].s_to = room['upstairs']
room['observatory'].w_to = room['upstairs']
room['masterbed'].e_to = room['upstairs']
room['masterbed'].s_to = room['secretpassage']
room['secretpassage'].n_to = room['masterbed']
room['secretpassage'].s_to = room['library']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



# initialize the player to be outside
player = Player(room['outside'])

def commands():
    print(f'Commands: [NORTH] [SOUTH] [EAST] [WEST]. \n Use [LOOK] to look around. \n Input [QUIT] to leave the game. \n Use [GET]/[TAKE] and [DROP] to manage items. \n You can check your inventory using [INVENTORY] or [I].')

while True:

    # print the current room
    print("====================\nCURRENT ROOM: " + player.room.name + "\n" + player.room.description + "\n====================")
    #print command instructions
    print('Type "commands" to see full command list.')
    

    userInput = input(">>: ").split(' ')

    # parse the input if more than 1 command
    if 1 <= len(userInput) <= 2:
        command = userInput[0]
        target = userInput[1] if len(userInput) == 2 else None

    if command.upper() == 'QUIT':
        break

    elif command.upper() == 'COMMANDS':
        # shows the command list
        commands()

    elif command.upper() in ['NORTH', 'N', 'SOUTH', 'S', 'EAST', 'E', 'WEST', 'W']:
        direction = command.upper()
        player.move(player.room, direction)

    elif command.upper() == 'LOOK':
        player.look(player.room)

    elif command.upper() in ['GET', 'TAKE']:
        for item in player.room.items:
            if target == item.name:
                player.pickup(item)
                player.room.remove_item(item)
                print(f'You add the {item.name} to your inventory.')
            else:
                print(f'There is no {target} here.')

    elif command.upper() == 'DROP':
        for item in player.inventory:
            if target == item.name:
                player.drop(item)
                player.room.add_item(item)
                print(f'You drop the {item.name} in the {player.room.name}.')

    elif command.upper() == 'INVENTORY' or command.upper() == 'I':
        player.check_inventory()

    elif command.upper() == 'SCORE':
        print(f'Your current score is {player.score}.')

        
    else:
        print("\n Unknown command, please try again.")
