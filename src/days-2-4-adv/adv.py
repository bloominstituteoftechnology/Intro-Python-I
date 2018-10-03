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
                     "North of you, the cave mount beckons",[sword]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [knife,coins]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[arrow,coins]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[knife,coins]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[sword,coins]),
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
p=Player(input('What is your name?'),room['outside'])

# Write a loop that:

direction = "What direction would you like to walk in?[n,s,e,w or q to quit]"
print(f'Hello {p.name},Your current location is:{p.currentRoom.name} and it has items: {p.currentRoom.showItems()}')
print(f'{p.currentRoom.text}')
print(direction)


valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w","forward": "n", "backwards": "s", "right": "e", "left": "w"}

while True:        
        cmds = input("-> ").lower().split(' ')
        print(cmds[1])
        cmd=cmds[0]
        print(cmd[0])
        if len(cmd)==1:
                cm=cmd[0]
                print(cm)
                if cm == "q":
                        print('You choose to quit.')
                        break
                elif cm in valid_directions:
                        print('inside valid')
                        p.travel(cm)
                elif cm =="t" or cm =="g":
                        print(cmds[1])
                        result=p.currentRoom.getItem(cmds[1])
                        if result!=None:
                                p.items.append(result)
                                p.currentRoom.removeItem(cmds[1])
                                print(f'p.currentRoom.showItems()')
                else:
                        print('I cannot understand your command')
        else:
                print("I did not understand that command.")        


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
