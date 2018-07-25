#Standard Library
import sys
import re
#Custom Modules
from room import Room
from roomList import rooms
from player import Player

# ________VARIABLES________
div = "________________________________"
playing = True


#________FUNCTIONS________
def movePlayer(action):
    try:
        if re.match(r'[n|N]', action):
            player.loc = player.loc.n_to
        elif re.match(r'[s|S]', action):
            player.loc = player.loc.s_to
        elif re.match(r'[e|E]', action):
            player.loc = player.loc.e_to
        elif re.match(r'[w|W]', action):
            player.loc = player.loc.w_to
        # If the user enters "q", quit the game.
        elif re.match(r'[q|Q]', action):
            playing = False
    except:
        print("You have entered an unknown action.\n\n")
        print(div)

# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player(rooms['outside'])
# Write a loop that:
while playing is True:
# * Prints the current room name
    print(player.loc.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player.loc.description)
    if len(player.loc.roomInv) > 0:
        items = ''
        for item in player.loc.roomInv:
            items += item.name + ' '
        print("You see: " + items)

# * Waits for user input and decides what to do.
    action = input("What are you going to do? ")
    matchAction = re.match(r'(\w+)\s(\w+)', action)
    if matchAction:
        action = [matchAction.group(1), matchAction.group(2)]
#
# If the user enters a cardinal direction, attempt to move to the room there.
    if len(action) == 1:
        movePlayer(action[0])
        print(div)
    elif len(action) == 2:
        try:
            if re.match(r'[g|G][e|E][t|T]|[t|T][a|A][k|K][e|E]', action[0]):
                for item in player.loc.roomInv:
                    if action[1].lower() == item.name.lower():
                        print("You picked up the " + item.name.lower())
                        print(div)
            if re.match(r'[g|G][o|O]', action[0]):
                movePlayer(action[1][0])
                print(div)
            if re.match(r'[d|D][r|R][o|O][p|P]', action[0]):
                print("DROP")
                print(div)
        except:
            print("you have entered an unknown action.\n\n")