import textwrap

from player import Player
from room import Room
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# create items
item1 = Item("coins", "Shiny coins")
item2 = Item("coins2", "Shiny coins 2")
item3 = Item("coins3", "Shiny coins 3")
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

done = False
inputCommand = []


def basicCommand():
    global done, player
    dirtionCommands = ["n", "s", "w", "e"]
    if inputCommand[0] == "q":
        done = True
    elif inputCommand[0] in dirtionCommands:
        player.curRoom = direction(inputCommand[0], player.curRoom)
    elif inputCommand[0] in ["i", "inv", "inventory"]:
        player.printInventory()
    elif inputCommand[0] == 'score':
        player.printScore()
    else:
        print("Unknown command {}".format(inputCommand))


def complexCommand():
    pickupcommands = ["get", "take", "pickup"]
    if inputCommand[0] in pickupcommands:
        player.pickUpItem(inputCommand[1])
    elif inputCommand[0] in ['drop', 'use']:
        player.useItem(inputCommand[1])
    else:
        print("Unknown command {}".format(inputCommand))



def startGameText():
    print("\n{}\n".format(player.curRoom.name))
    for line in textwrap.wrap(player.curRoom.description):
        print(line)
    if len(player.curRoom.items) > 0:
        print("\nYou see:")
        for i in player.curRoom.items:
            print("     " + str(i.name))


while not done:

    startGameText()

    inputCommand = input("\nCommand> ").strip().lower().split()

    if len(inputCommand) > 2 or len(inputCommand) < 1:
        print("Cannot use command")

    if len(inputCommand) == 1:
        basicCommand()
    elif len(inputCommand) == 2:
        complexCommand()
