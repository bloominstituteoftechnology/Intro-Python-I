from os import system # for system clear on game play
from room import Room
from player import Player
from item import Item
import textwrap


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

# Add items

room['outside'].contents.append(Item("rose", "A fragrent crimson rose."))
room['foyer'].contents.append(Item("dagger", "A silver dagger."))
room['overlook'].contents.append(Item("wine", "A vintage bottle of French wine."))
room['narrow'].contents.append(Item("sword", "A gem embelished sword."))
room['treasure'].contents.append(Item("diamond", "A small sparkly diamond."))


#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player = Player( "Natalie", room['outside'])

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

# def pickup(self, player, item):
#         try:
#             self.items.remove(item)
#             player.addItem(item)
#             return "Picked up " + item.name + '\n'
#         except:
#             return "There is no " + item.name + '\n'

done = False

while not done:
    curRoom = player.room

    # Print out room description

    prettyDesc = textwrap.fill(curRoom.description)

    print(f'\n{curRoom.name}\n\n{prettyDesc}')

    # Print room contents

    if len(curRoom.contents) > 0:
        print("\nYou also see:")
        for i in curRoom.contents:
            print("   " + i.description)

    # Prompt

    command = input("\nCommand> ").strip().lower()

    command = command.split(' ')

    # Single word commands

    if len(command) == 1:

        if command[0] == 'q' or command[0] == 'quit' or command[0] == 'exit':
            done = True

        elif command[0] in ["s", "n", "e", "w"]:
            dirAttr = command[0] + "_to"

            if hasattr(curRoom, dirAttr):
                player.room = getattr(curRoom, dirAttr)

            else:
                print("You can't go that way.")

        elif command[0] in ["i", "inventory"]:
            if len(player.contents) > 0:
                print("\nYou're currently carrying:")
                for i in player.contents:
                    print("   " + i.description)
            else:
                print("\nYou're not carrying anything.")

        else:
            print("I don't understand that command.")

        # Check score
        elif command[0] in ["Score?"]:
            print(player.score)


    elif len(command) == 2:

        verb, obj = command

        if verb in ['get', 'take']:
            candidates =  [item for item in curRoom.contents if item.name == obj]

            if len(candidates) == 0:
                print("You don't see that here.")

            else:
                player.contents.append(candidates[0])
                curRoom.contents.remove(candidates[0])

        elif verb == 'drop':
            candidates = [item for item in player.contents if item.name == obj]

            if len(candidates) == 0:
                print("You're not carrying that.")

            else:
                player.contents.remove(candidates[0])
                curRoom.contents.append(candidates[0])

        else:
            print("I don't understand that command.")

    else:
        print("I don't understand that command.")