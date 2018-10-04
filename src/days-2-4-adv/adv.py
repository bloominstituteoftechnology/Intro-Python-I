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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#items
item = {
    'walrus': Item("walrus",
    "What a thick boy!")
}

room['outside'].items.append(item['walrus'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player(input("What is your name? "), room['outside'])
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

direction = ("n", "e", "s", "w")
while True:

    print(f'\n {p.currentRoom.name!s} \n \n {p.currentRoom.description!s}')
    if len(p.currentRoom.items) > 0:
        for item in p.currentRoom.items:
            print(f'You see a {item.name!s}')
    cmds = input("-->").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds in direction:
            p.move(cmds[0])
        else:
            print(f"What do you mean by {cmds!s}, {p.name!s}?")
    elif len(cmds) > 1:
        if cmds[0] == "get" or "take":
            itemTaken = p.currentRoom.findItemByName(" ".join(cmds[1:]))
            if itemTaken is not None:
                p.getItem(itemTaken.name)
                p.currentRoom.removeItem(itemTaken)
            else:
                item = " ".join(cmds[1:])
                print(f"There is no {item!s} here.")
        

