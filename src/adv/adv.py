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
def playerAction(action):
    try:  # check for N, S, E, or W, then move the player that direction
        global player
        global playing
        if re.match(r'[n|N]', action):
            player.loc = player.loc.n_to
        elif re.match(r'[s|S]', action):
            player.loc = player.loc.s_to
        elif re.match(r'[e|E]', action):
            player.loc = player.loc.e_to
        elif re.match(r'[w|W]', action):
            player.loc = player.loc.w_to
        elif re.match(r'[i|I]', action):
            items = ''
            for item in player.playerInv:
                items += item.name + ' '
            print("\nInventory: " + items)
        # If the user enters "q", quit the game.
        elif re.match(r'[q|Q]', action):
            playing = False
            return
    except:  # if a bad command was given, let the player know
        print("You have entered an unknown action.\n\n")
        print(div)
    return
    

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
    matchAction = re.match(r'(\w+)\s(\w+)', action)  # check for two words
    if matchAction:
        action = [matchAction.group(1), matchAction.group(2)] # set action as two word command (get/take ___, go ___, drop ___)
    else:
        action = action[0] # check for direction fully spelled(eg. north), and set action as single character command (n, s, e, w)
#
# If the user enters a cardinal direction, attempt to move to the room there.
    if len(action) == 1:
        playerAction(action[0])
        print(div)
    elif len(action) == 2:
        try:
            if re.match(r'[g|G][e|E][t|T]|[t|T][a|A][k|K][e|E]', action[0]): # check for "get" or "take"
                for item in player.loc.roomInv:
                    if action[1].lower() == item.name.lower():
                        player.loc.roomInv.remove(item)
                        player.playerInv.append(item)
                        for item in player.playerInv:
                            print(item.name)
                        print("\nYou picked up the " + item.name.lower() + '\n')  # confirm that the player picked up this item by name
                        print(div)
            if re.match(r'[g|G][o|O]', action[0]):  # check for "go"
                playerAction(action[1][0])  #move the player N, S, E, or W
                print(div)
            if re.match(r'[d|D][r|R][o|O][p|P]', action[0]): # check for "drop"
                if re.match(r'[i|I][t|T]', action[1]): # check for "it"
                    item = player.playerInv.pop() # remove the last item
                    player.loc.roomInv.append(item) # add that item to this room
                    print('\nYou have dropped the ' + item.name) # confirm with player that they dropped the item
                else:
                    confirmItem = False # used to check inventory
                    for item in player.playerInv:
                        if action[1].lower() == item.name.lower(): # compare command with inventory
                            confirmItem = True # if not confirmed, they don't have it to drop it
                            player.playerInv.remove(item) # remove from player
                            player.loc.roomInv.append(item) # add to room
                            print('\nYou have dropped the ' + item.name) # tell player what item they dropped
                            break # end the loop, so you only drop one
                    if confirmItem == False: # if the item was never dropped, tell them they don't have it.
                        print('\nYou do not have one of those.')
                print(div)
        except:
            print("\nYou have entered an unknown action.\n")