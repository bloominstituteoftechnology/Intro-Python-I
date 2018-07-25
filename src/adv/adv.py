from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Staff", "A plain, worn wooden staff")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Amulet", "The chain is made of finely worked gold cradling a small ruby")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Chainmail", "Slightly rusty and scarred, this armor is nevertheless still servicable")]),
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

def dircheck(attr):
    if hasattr(player.room, attr):
        player.room = getattr(player.room, attr)
    else:
        print("\nInaccessible direction, try again")

while True:
    print("\n* " + player.room.name + " *")
    print(textwrap.fill(player.room.desc, 50))
    print("Items: " + (",".join([item.name for item in player.room.items]) or "None") + "\n")
    cmd = input("Enter a command: ").strip().lower()
    cmds = cmd.split(" ")
    if len(cmds) == 1:
        if cmd == "q" or cmd == "quit":
            break
        elif cmd in ["n", "e", "s", "w"]:
            dircheck(cmd + "_to")
        elif cmd == "i" or cmd == "inventory":
            print("\nInventory:\n" + "\n".join([item.name + " - " + item.desc for item in player.inventory]))
        else:
            print("\nInvalid command, try again")
    elif len(cmds) == 2:
        verb = cmds[0]
        obj = cmds[1]
        if verb == "get" or verb == "take":
            if obj in [item.name.lower() for item in player.room.items]:
                for i, o in enumerate(player.room.items):
                    if o.name.lower() == obj:
                        player.inventory.append(o)
                        del player.room.items[i]
                        break
            else:
                print("\nObject not found in room")
        elif verb == "drop":
            if obj in [item.name.lower() for item in player.inventory]:
                for i, o in enumerate(player.inventory):
                    if o.name.lower() == obj:
                        player.room.items.append(o)
                        del player.inventory[i]
                        break
            else:
                print("\nObject not found in inventory")
    else:
        print("\nInvalid command, try again")