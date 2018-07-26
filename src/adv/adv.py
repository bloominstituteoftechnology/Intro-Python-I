from room import Room
from player import Player
import textwrap
import item from Item

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
earlier adventurers. The only exit is to the south.""",
}

# Create items and add to rooms

item1 = Item("A rose.", "Smells lovely.")
item2 = Item("A single small diamond.", "Sparkles.")
room['outside'].addItem(item1)
room['treasure'].addItem(item2)


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
player = Player("Natalie", room['outside'])

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

def pickup(self, player, item):
        try:
            self.items.remove(item)
            player.addItem(item)
            return "Picked up " + item.name + '\n'
        except:
            return "There is no " + item.name + '\n'

done = False

while not done: 
    curRoom = player.room

    prettyDesc = textwrap.fill(curRoom.description.items)

    print(f'{curRoom.name}\n{prettyDesc.description}')

    if len(player.curRoom.items) > 0:
        print("\nYou see:")
        for i in player.curRoom.items:
            print("     " + str(i.name))
            
    command = input("Command> ").strip().lower().split() #takes off white space and returns lowercase

    if command == 'q' or command == 'quit' or command == 'exit':
        done = True

    elif command in ["s", "n", "e", "w"]:
        dirAttr = command + "_to"

        if hasattr(curRoom, dirAttr): 
          player.room = getattr(curRoom, dirAttr)

        else: 
            print("You can't go that way.")
    elif len(s) == 2:
        if s[0] in ["get", "take", "pickup"]:
            item = player.curRoom.findItem(s[1])

            if item is None:
                print("Item not found")
            else:
                player.addItem(item)
                player.curRoom.removeItem(item.name)
        
    else: 
        print("I don't understand that command.")