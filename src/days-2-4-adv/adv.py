from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["rock", "rock", "rock", "rock"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["key"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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


room['outside'].connectRooms(room['foyer'], "n")
room['foyer'].connectRooms(room['overlook'], "n")
room['foyer'].connectRooms(room['outside'], "s")
room['foyer'].connectRooms(room['narrow'], "e")
room['overlook'].connectRooms(room['foyer'], "s")
room['narrow'].connectRooms(room['foyer'], "w")
room['narrow'].connectRooms(room['treasure'], "n")
room['treasure'].connectRooms(room['narrow'], "s")



#
# Main
#
suppressRoomPrint = False

validDirection: ['n', 's', 'e', 'w']

# Make a new player object that is currently in the 'outside' room.

name = input("What is your name? ")
player = Player(name, room['outside'], [])

print (f"Welcome, {player.name}!\n")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print (f"\n  {player.location.title}\n    {player.location.description}\n" )

    inp_args = input(">>>").split(" ")
    if inp_args[0] == "q":
        break
    if inp_args[0] == "n" or inp_args[0] == "s" or inp_args[0] == "w" or inp_args[0] == "e":
        newRoom = player.location.getRmInDir(inp_args[0])
        if newRoom == None:
            print("You cannot move in that direction")
            suppressRoomPrint = True
        else:
            player.changeLocation(newRoom)

    elif inp_args[0] == 'g' or inp_args[0] == 'get':
        item = inp_args[1]
        player.getItem(item)
        #room.removeItem(item)
    elif inp_args[0] == 'd' or inp_args[0] == 'drop':
        player.dropItem(inp_args[1])
        #room.gainItem(inp_args[1])
    elif inp_args[0] == 'i' or inp_args[0] == 'inventory':
        if len(player.items) == 0:
            print("You have no items.")
        else:
            print(f"\n{player.items}\n")
    else:
        print('That command is not recognized.')
        suppressRoomPrint = True
    
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
