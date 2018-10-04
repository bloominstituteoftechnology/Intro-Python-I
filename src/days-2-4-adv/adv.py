from room import Room
from player import Player
from item import Item
import textwrap
import time

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
chamber! """),
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

rock1 = Item("Rock", "This is a rock.")
rock2 = Item("Rock", "This is a rock.")

playerStartingItems = [rock1]
room['outside'].addItem(rock2)

# Valid directions

valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

p = Player(input('\n\n\n\n\nWhat is your name?'), room['outside'], playerStartingItems)

while True:
    time.sleep(1)
    cmd = input('\n\n\n\n\nYou are in the main menu. Are you ready? \n=>')

    if cmd.upper() == 'YES':
        # time.sleep(2)
        print('\n\n\nYour location is: ')
        # time.sleep(1)
        print(p.currentRoom)
        while True:
            # time.sleep(1)
            cmds = input('\n\n\nWhat do you want to do?\n=>').lower().split(" ")
            if len(cmds) == 1:
                if cmds[0] in valid_directions:
                    # time.sleep(2)
                    p.travel(valid_directions[cmds[0]])
                elif cmds[0].upper() == 'Q':
                    # time.sleep(1)
                    cmd = input('\n\n\nAre you sure you want to quit the game?\n=>')
                    if cmd.upper() == 'YES':
                        # time.sleep(1)
                        print('Goodbye!')
                        break
                    elif cmd.upper() == 'NO':
                        continue
                    else:
                        # time.sleep(1)
                        print('\nI cannot understand. Let\'s continue!')
                        continue
                elif cmds[0].upper() == 'I' or cmds[0].upper() == 'INVENTORY':
                    p.printInventory()
                else:
                    time.sleep(1)
                    print('You can only go north, south, east or west! Try going somewhere!')
            elif len(cmds) == 2:
                if cmds[0] == "look":
                    if cmds[1] in valid_directions:
                        # time.sleep(2)
                        p.look(valid_directions[cmds[1]])
                elif cmds[0] == "take":
                    currentRoom = p.currentRoom
                    itemToTake = currentRoom.findItemByName(cmds[1])
                    if itemToTake is not None:
                        p.addItem(itemToTake)
                        currentRoom.removeItem(itemToTake)
                    else:
                        print("You did not see that item.")
                elif cmds[0] == "drop":
                    currentRoom = p.currentRoom
                    itemToDrop = p.findItemByName(cmds[1])
                    if itemToDrop is not None:
                        p.removeItem(itemToDrop)
                        p.currentRoom.addItem(itemToDrop)
                    else:
                        print("You are not holding that item.")
                else:
                    time.sleep(1)
                    print('I did not understand that command!')

    elif cmd.upper() == 'NO':
        # time.sleep(2)
        print('Are you afraid?')
        # time.sleep(1) 
    elif cmd.upper() == 'Q':
        # time.sleep(2)
        print('\n\n\nGoodbye')
        # time.sleep(2) 
        print('coward...\n\n\n\n\n')
        # time.sleep(1) 
        break
    else:
        # time.sleep(2) 
        print('\nI cannot understand you!')
        # time.sleep(1) 
        print('\Yes or no?')
        # time.sleep(2) 
