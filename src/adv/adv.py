import textwrap

from player import Player
from room import Room
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# create items
item1 = Item("coins", "Shiny coins")
room['outside'].items.append(item1)

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

def direction(d, curRoom):

    attrib = d + '_to'
    if hasattr(curRoom, attrib):
        return getattr(curRoom, attrib)

    print("You can't go that way")
    return curRoom

player = Player(room['outside'])

print(player.curRoom.name)

done = False

while not done:

    print("\n{}\n".format(player.curRoom.name))

    for line in textwrap.wrap(player.curRoom.description):
        print(line)

    if len(player.curRoom.items) > 0:
        print("\nYou see:")
        for i in player.curRoom.items:
            print("     " + str(i.name))

    s = input("\nCommand> ").strip().lower()

    if s == "q":
        done = True
    elif s in ["n", "s", "w", "e"]:
        player.curRoom = direction(s, player.curRoom)
    else:
        print("Unknown command {}".format(s))

