from room import Room
from player import Player
from items import Treasure, Weapon, LightSource
import time
# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", True),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

items = {
    'sword': Weapon("sword", "An old sword, very rusty, will not last thru the winter"),
    'bow': Weapon("bow", "A worthless bow, looks like something out of a zelda game"),
    'book': Treasure("bible", "The most worthless of items a person could find"),
    'hair': Treasure("hair", "This item is still more useful than the bible"),
    'lamp': LightSource("lamp", "a cheap lamp from the dollar store, this wont last long")
}

# Link item to room
room['foyer'].addItem(items['sword'])
room['foyer'].addItem(items['bow'])
room['treasure'].addItem(items['book'])
room['foyer'].addItem(items['hair'])
room['overlook'].addItem(items['lamp'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

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

playing = True

while playing:
    time.sleep(1)
    canSee = player.inRoom.isLight
    for item in player.items + player.inRoom.items:
        if isinstance(item, LightSource):
            canSee = True
            item.useFuel(player)
            print(f'\n!!!!!!Light source {item.name} has {item.fuel} fuel uses left')
            time.sleep(1)

    if canSee:
        print(f"\n=======\nRoom: {player.inRoom.name}, Description: {player.inRoom.description}\nType help for command list")
    else:
        print(f"it's pitch black in here")
    cmd = input("\nInput Task: ").strip().lower().split()
    verb = cmd[0]
    if verb == "q":
        print("Thank you for Playing")
        playing = False

    # start on 2 input commands
    if len(cmd) > 1:
        obj = cmd[1]

        if verb == 'get':
            toGet = 0
            for item in player.inRoom.items:
                if obj == item.name:
                    item.on_take(player)
                    player.inRoom.dropItem(item)
                    toGet = 1
            if toGet == 0:
                print(f"{obj} is not in this room")
        elif verb == 'drop':
            for item in player.items:
                if obj == item.name:
                    player.dropItem(item)
                    player.inRoom.addItem(item)
                else:
                    print(f"{obj} is not in your inventory")

    # start of 1 input commands
    else:
        if verb in ["n", "s", "e", "w"]:
            direc = ''.join([verb + '_to'])
            if hasattr(player.inRoom, direc):
                player.move(getattr(player.inRoom, direc))
            else:
                print(f"\n===You can't go {verb}===")
                time.sleep(1)
        elif verb == 'i':
            player.showItmes()
            time.sleep(1)
        elif verb == 'room':
            if canSee:
                player.inRoom.showItmes()
                time.sleep(1)
            else:
                print('you need to find some light buddy')
        elif verb == 'score':
            player.showScore()
            time.sleep(1)
        else:
            print(f"{verb} is not valid")
