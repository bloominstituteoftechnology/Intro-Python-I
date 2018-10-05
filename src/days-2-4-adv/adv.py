from room import Room
from player import Player
from item import Item, Treasure, Light
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, a huge ugly house sits creepily", True),

    'spoopy':   Room("Heckin Spoopy Manor", """This place is spoopy as heck. Weird hallways run north and east. 
But like.. I duno why you would stay""", True, Treasure("duck", "it's made of rubber, a lil weird", 1), Item("rope", "this seems chill")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True, Light("lamp", "still lit for some reason", 3)),

    'narrow':   Room("Narrow Hallway", """This narrow hallway bends here from west
to north. The smell of gold permeates the air, which is kinda gross. Metallic and stuff.""", True, Treasure("spoon", "genuiiiine silver", 5)),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False, Item("dusty-shoe", "this thing is gross")),
}


# Link rooms together

room['outside'].n_to = room['spoopy']
room['spoopy'].s_to = room['outside']
room['spoopy'].n_to = room['overlook']
room['spoopy'].e_to = room['narrow']
room['overlook'].s_to = room['spoopy']
room['narrow'].w_to = room['spoopy']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("what's yer name? "), room['outside'])
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
print (f"\n{player.currentRoom.name}:\n\n{player.currentRoom.description}\n\nPick a direction to start (n, s, e, w)\n")

while True: 
    cmd = input("what next?-> ").split(" ")
    if cmd[0] is "q":
        print ("\n~~~~ until tomorrow ~~~~\n")
        break
    elif cmd[0] == "n" or cmd[0] == "s" or cmd[0] == "e" or cmd[0] == "w":
        player.enter(cmd[0])
    elif cmd[0] == "take" or cmd[0] == "drop":
        player.itemHandler(cmd[0], cmd[1])
    elif cmd[0] == "i" or cmd[0] == "inventory":
        if len(player.items) != 0:
            inv = ", ".join([each.name for each in player.items])
            print (f"\nyou're curently holding: {inv}\n")
        else: 
            print (f"\nyou don't have anything on you, not even a cellphone?!\n")
    elif cmd[0] == "score":
        print (f"\nya score is {player.score}\n")
    else:
        print ("\nPlease enter a valid command: \n(n, s, e, w, i/inventory, score, take itemname, drop itemname)\n")
    
        
