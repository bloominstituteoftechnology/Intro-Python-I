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

room['outside'].itemslist.append(Item('rusty shield', 'an old rusty shield not of any use'))
room['narrow'].itemslist.append(Item('shield', 'an shield strong and sturdy'))
room['foyer'].itemslist.append(Item('sword', 'it gives off an erry green glow'))
room['treasure'].itemslist.append(Item('crown', 'A golden crown '))

#
# Main
#
itemslist = ["there is nothing here"]
# Make a new player object that is currently in the 'outside' room.

name = input('Enter your name Traveler: ')

# this creates the player
player1 = Player(name, room['outside'])

print("Welcome " + player1.name)

done = False
while not done:
    currentRoom = player1.room

    print("You are currently in " + currentRoom.name)
    #print("The items in this room are ", currentRoom.itemslist)
    print(currentRoom.description)
    
    # print room contents

    if len(currentRoom.itemslist) > 0:
        print("\nYou also see:")
        for i in currentRoom.itemslist:
            print(i.name + " :"  + i.description)

    direction = input('Please enter the direction you would like to go: ').strip().lower()

    # Single word commands

    if len(direction) == 1:
    
        if direction[0] == 'q' or direction[0] == 'quit' or direction[0] == 'exit':
            done = True
        elif direction[0] in ['s', 'n', 'e', 'w']:
            dirAttr = direction[0] + '_to'

            if hasattr(currentRoom, dirAttr):
                player1.room = getattr(currentRoom,dirAttr)
            else: 
                print('That is not a valid direction')
        elif direction[0] in ["i", 'inventory']:
            if len(player1.inventory) > 0:
                print("\n Here is your inventory travler: ")
                for i in player.inventory:
                    print ("  " + i.description)
            else:
                print("You currently are holding nothing")
        else: 
            print('I do not understand that')
    elif len(direction) == 2:

        ver, obj = direction
        if verb in ["get", 'take', 'grab']:
            candidates = [item for item in currentRoom.itemslist if item.name == obj]

            if len(candidates) == 0:
                print("You dont see that here")
            else:
                player1.inventory.append(candidates[0])
                currentRoom.itemslist.remove(candidates[0])
        elif ver == 'drop':
            candidates = [item for item in player1.inventory if item.name == obj]

            if len(candidates) == 0:
                print("You're not carrying that.")
            else:
                player1.inventory.remove(candidates[0])
                currentRoom.itemslist.append(candidates[0])
        else:
            print("I don't understand that")
    else:
        print("I don't understand that")

# Write a loop that:
#
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).
#print(currentRoom.description)
# * Waits for user input and decides what to do.
#
# Print an error message if the movement isn't allowed.
# if direction == 'north':
#     currentRoom.name = 'foyer'

# if direction == 'q':
#     exit()

#
# If the user enters "q", quit the game.
