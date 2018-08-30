from room import Room
from player import Player
from item import Items

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [knife, twigs]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [book, axe, sword, shield]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [rock]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [coin, coin, torch]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [chest, coin,]),
}

# Declare all items

item = {
    'axe': Item('Axe of the Winterlands', """Hidden within these walls for centuries,
this axe looks as though it has never been put to the test"""),

    'book': Item(,'Book of Everything', """The secrets of the cave may lie within these pages...
or not."""),

    'coin': Item('Gold coin', "WOW! A coin this shiny and heavy must be worth a fortune!"),

    'knife': Item('rusty old knife', """Although it may be small,
this knife may come in handy when you least expect it... """),

    'twigs': Item('A bushel of twigs', "When the Lord of Light is away, these twigs remain."),
    
    'rock': Item('jagged rok', """A rock of this size may slow you down a little bit,
but at least you'll work off that belly full of ale!"""),
    
    'shield': Item('Wooden Shield', """This may not be the fanciest of shields,
but it sure is better than nothing!"""),
    
    'sword': Item('Breaker of Necks', """Battered and bloodied,
this sword seems to have taken many a foe's lives."""),

    'torch': Item('torch', """A mobile form of fire that may illuminate your chosen path.
The Lord of Light approves."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Samwise', room['outside'])

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

initialGreeting = print(f"""Welcome {player.name}! You are currently located in the following room:

    {player.curRoom.name}:
    {player.curRoom.description}

    The following Items are available for you to use:
    {player.curRoom.items}

    How would you like to proceed?""")

while True:
    print(initialGreeting)
    userInput = input()
    command = userInput.split(" ")

    if command[0] == 'quit':
        print('Thanks for playing, have a nice day!')
        exit()
    elif command[0] == 'move': 
        if command[1] in ['north', 'east', 'south', 'west']:
            newRoom = player.curRoom.getRoomInDirection(command[1])
            if newRoom == None:
                print('You cannot move in this direction.')
            else:
                player.change_location(newRoom)
    elif command[0] == 'pickup':
        if command[1] == ''
    else:
        print(f'INVALID INPUT: please input a proper command for {player.name}')