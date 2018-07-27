from player import Player
from room import Room
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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

#
# Main
#
room['overlook'].contents.append(Item("coins", "Gold coins"))
room['overlook'].contents.append(Item("sword", "Sword made of platinum"))

# Make a new player object that is currently in the 'outside' room.

# player_name = input("Enter a player name: ")
player = Player("Kenzie", room['outside'])
# print("\nWelcome, %s!" % (player.playerName))

# * Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# * If the user enters a cardinal direction, attempt to move to the room there.
# * Print an error message if the movement isn't allowed.
# * If the user enters "q", quit the game.

done = False

while not done:
    curRoom = player.room

    prettyDesc = textwrap.fill(curRoom.description)

    print(f'\n{curRoom.name}\n\n{prettyDesc}')

    #Room Contents
    if len(curRoom.contents) > 0:
        print("\nYou also see:")
        for i in curRoom.contents:
            print("   " + i.description)

    command = input("\nCommand> ").strip().lower()

    command = command.split(' ')

    #Single Word Commands
    if len(command) == 1:

        if command == 'q' or command == 'quit' or command == 'exit':
            done = True

        elif command in ["s", "n", "e", "w"]:
            dirAttr = command + "_to"

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
            print("Turn around!")
    
    #Two Word Commands
    elif len(command) == 2:

        verb, obj = command

        if verb in ['get', 'take']:
            candidates = [item for item in curRoom.contents if item.name == obj]
            
            if len(candidates) == 0:
                print("You don't see that here.")

            else:
                player.contents.append(candidates[0])
                curRoom.contents.remove(candidates[0])
    
        if verb == 'drop':
            candidates = [item for item in player.contents if item.name == obj]
        
            if len(candidates) == 0:
                print("You're not carrying that.")

            else:
                player.contents.remove(candidates[0])
                curRoom.contents.append(candidates[0])
        else:
            print("I don't understand that!")

# while True:
#   currRoom = player.room
#   print(currRoom.get('name'))
#   print(currRoom.get('description'))
#   userInput = input('What do you want to do? ')
#   if userInput in directions:
#       move exists
#       key = '{}_to'.format(userInput)
#   if rooms[player1.currRoom].get(key):
#       player1 = Player(rooms[player1.currRoom].get(key))
#   else:
#       print('you cannot move there')
#   elif userInput == 'q':
#       break
