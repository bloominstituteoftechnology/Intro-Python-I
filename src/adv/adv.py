from room import Room
from player import Player
from item import Item
import textwrap


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", 
                     "To the East you see a bus stop! North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exits are to the south and what looks like 
some stairs leading to a basement to the east."""),

    'bus stop': Room("bus stop", """You're now waiting at the bus stop, too bad 
there isnt another bus coming until next month! You might as well head back west and explore these rooms!"""),

    'basement': Room("basement", """You're in the basement, its dark, you trip over something on the floor.
do you pick it up?""")
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].e_to = room['bus stop']
room['bus stop'].w_to = room['outside']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].e_to = room['basement']

# adding an item to a room
room['basement'].contents.append(Item("coins", "gold coins"))
room['bus stop'].contents.append(Item("coins", "gold coins"))


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("yasin", room['outside'])

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

done = False

while not done:
    curRoom = player.room
    print(f'{curRoom.name}\n{curRoom.description}')

    if len(curRoom.contents) > 0:
        print("you just found:")
        for i in curRoom.contents:
            print("  " + i.description)
        print()

    command = input("\nCommand> ").strip().lower()

    command = command.split(' ')
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
            print("I don't understand that!")

    elif len(command) == 2:

        verb, obj = command

        if verb in ['get', 'take']:
            candidates = [item for item in curRoom.contents if item.name == obj]

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
            print("I don't understand that!")

    else:
        print("I don't understand that!")