from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, a huge ugly house sits creepily"),

    'spoopy':   Room("Heckin Spoopy Manor", """This place is spoopy as heck. Weird hallways run north and east. 
But like.. I duno why you would stay""", "rubber duck", "rope"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Hallway", """This narrow hallway bends here from west
to north. The smell of gold permeates the air, which is kinda gross. Metallic and stuff."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "dusty shoe"),
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
        player.currentRoom.getItem()
    elif cmd[0] == "pickup" or cmd[0] == "drop":
        print (player.items)
        player.itemHandler(cmd[0], cmd[1])
    else:
        print ("\nPlease enter a valid direction (n, s, e, w)\n")
    
        
