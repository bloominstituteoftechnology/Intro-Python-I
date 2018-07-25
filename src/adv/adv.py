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
item2 = Item("coins 2", "Shiny coins 2")
item3 = Item("coins 3", "Shiny coins 3")
room['outside'].addItem(item1)
room['outside'].addItem(item2)
room['outside'].addItem(item3)

item4 = Item('dog', 'black')
room['foyer'].addItem(item4)
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


def findItemInRoom(name):
    return player.curRoom.findItem(name)


done = False

while not done:

    print("\n{}\n".format(player.curRoom.name))

    for line in textwrap.wrap(player.curRoom.description):
        print(line)

    if len(player.curRoom.items) > 0:
        print("\nYou see:")
        for i in player.curRoom.items:
            print("     " + str(i.name))

    s = input("\nCommand> ").strip().lower().split()

    if len(s) > 2 or len(s) < 1:
        print("Cannot use command")

    if len(s) == 1:
        if s[0] == "q":
            done = True
        elif s[0] in ["n", "s", "w", "e"]:
            player.curRoom = direction(s[0], player.curRoom)
        elif s[0] in ["i", "inv", "inventory"]:
            player.printInventory()
        else:
            print("Unknown command {}".format(s))
    elif len(s) == 2:
        if s[0] in ["get", "take", "pickup"]:
            # item = player.curRoom.findItem(s[1])
            item = findItemInRoom(s[1])

            if item is None:
                print("Item not found")
            else:
                player.addItem(item)
                player.curRoom.removeItem(item.name)

def findItemInRoom(name):
    return player.curRoom.findItem(name)
