from room import Room
from player import Player
from item import Item
from item import LightSource
from item import Treasure


item = {
    "key": Item("key", "a small golden key"),
    "rock": Item("rock", "just a small rock"),
    "torch": LightSource("torch", "a torch with a flame"),
    "coins": Treasure("coins", "a pouch filled with golden coins", 5),

}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item["rock"]], True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item["key"]], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item["torch"]], True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item["coins"]], False),
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
player = Player(name, room['outside'], [], 0)

print (f"Welcome, {player.name}!\n")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    if suppressRoomPrint == True:
        suppressRoomPrint = False
    else:
        
        if player.location.is_light == False and item.LightSource not in player.items and item.LightSource not in player.location.items:
            print("It's pitch black!")
            inp_args = input(">>>").split(" ")
            if inp_args[0] == 'g' or inp_args[0] == 'get':
                print("Good luck finding that in the dark!")
        else:
            print (f"\n  {player.location.title}\n    {player.location.description}\n     Items in this room: \n" )
            for i in player.location.items:
                print (f"\n  {i.name}: {i.description}")
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
        itm = item[inp_args[1]]
        current_room = player.location
        if itm in current_room.items:
            player.getItem(itm)
            current_room.removeItem(itm)
            
        else:
            print("You cannot get that item.")

    elif inp_args[0] == 'd' or inp_args[0] == 'drop':
        itm = item[inp_args[1]]
        current_room = player.location
        if itm in player.items:
            player.dropItem(itm)
            current_room.gainItem(itm)
        else:
            print("You don't have that item.")
    elif inp_args[0] == 'i' or inp_args[0] == 'inventory':
        if len(player.items) == 0:
            print("You have no items.")
        else:
            for i in player.items:
                print(f"\n{i.name}\n")
    elif inp_args[0] == "score":
        print(player.score)
    else:
        print('That command is not recognized.')
        suppressRoomPrint = True
    
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
