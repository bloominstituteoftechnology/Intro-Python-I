from room import Room
from player import Player
from item import Item
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Sword", "A rusty sword")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[Item("Shield", "A sturdy shield")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Treasure", "A candy")]),
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

player = Player("Luke", room['outside'])

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

gameEnd = False

while not gameEnd:
    currentRoom = player.room
    prettyDesc = textwrap.fill(currentRoom.desc)
    itemDesc = textwrap.fill(",".join([item.name for item in player.room.items]))
    print(f'{currentRoom.name}\n{prettyDesc}')
    print("Items: " + f'{itemDesc}\n')

    command = input("Command> ").strip().lower()
    cmds = command.split(" ")

    if len(cmds) == 1:

        if command == 'q' or command == 'quit' or command == 'exit':
            gameEnd = True

        elif command in ["s", "n", "w", "e"]:
            direction = command + "_to"

            if hasattr(currentRoom, direction):
                player.room = getattr(currentRoom, direction)

            else:
                print("There is nothing there")
        elif command == "i" or command == "inventory":
            print("\nInventory:\n" + "\n".join([item.name + " - " + item.desc for item in player.inventory + "\n"]))
            
        else:
            print("Wrong command")
    elif len(cmds) == 2:
        verb = cmds[0]
        obj = cmds[1]
        if verb == "get" or verb == "take":
            if obj in [item.name.lower() for item in player.room.items]:
                for i, o in enumerate(player.room.items):
                    if o.name.lower() == obj:
                        player.inventory.append(o)
                        print("\nPicked up %s\n" %(o.name))
                        del player.room.items[i]
                        break
            else:
                print("\nNo such object in the room")
        elif verb == "drop":
            if obj in [item.name.lower() for item in player.inventory]:
                for i, o in enumerate(player.inventory):
                    if o.name.lower() == obj:
                        player.room.items.append(o)
                        del player.inventory[i]
                        print("\nDropped %s\n" %(o.name))
                        break
            else:
                print("\nNo such object in the inventory")
    else:
        print("\nWrong command end")
