from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the items

sword=Item('sword','It is magical sword with interesting powers')
knife=Item('knife','It is an ancient knife with speed and power')
arrow=Item('arrow','Bow and arrow are a deadly combination')
coins=Item('coins','Coins can buy you other items')



# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[sword, coins]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [knife,coins]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[arrow, coins]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[knife, coins]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[sword, coins]),
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
p=Player(input('\nWhat is your name?'),room['outside'])

# Write a loop that:

direction = "\nWhat direction would you like to walk in?[n,s,e,w or q to quit]\nYou could also enter commands like take sword or get coins to grab the availabe items in the room\n to view your items or inventory type i or inventory"

print(f'\nYour current location is:{p.currentRoom.name}')
print('\nItems availabe in this room are:\n') 
p.currentRoom.showItems()
print(f'{p.currentRoom.text}')
print(direction)


valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w","f": "n", "b": "s", "r": "e", "l": "w"}

while True:        
        cmds = input("-> ").lower().split(' ')
        #print(cmds)
        cmd=cmds[0]
        #print(cmd)
        if cmd == "q":
                print('You choose to quit.')
                break
        elif cmd in valid_directions:
                p.travel(valid_directions[cmd])
                print(f'Items available in this room are:')
                p.currentRoom.showItems()
        elif cmd == "take" or cmd == "get":
                result=p.currentRoom.getItem(cmds[1])
                #print(f'{result}')
                if result!=None:
                        p.addItem(result)
                        room[p.currentRoom.name].removeItem(result)
                        result1=p.currentRoom.getItem(result)
                        if result1 == None:
                                print(f'{result} successfuly removed from the room')
                else:
                        print(f'Item not availabe')
        elif cmd == "inventory" or cmd =="i":
                print('Your inventory has')
                p.showItems()
        elif cmd =="drop":
                p.removeItem(cmds[1])    
        else:
                print('I cannot understand your command')


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
