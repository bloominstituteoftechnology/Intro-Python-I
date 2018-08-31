from room import Room
from player import Player
from item import Item

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

gold = Item("gold")
axe = Item("axe")
lattern = Item("lattern")

room['outside'].addItem(gold)
room['outside'].addItem(lattern)


player = Player(room['outside'])
ast = "\n*********************************************\n"



##### Game Loop Starts Below
while True:
    print (f"{ast}You are at the {player.location.name.upper()}\n   {player.location.description}{ast}")
    inp = input(">>> ENTER YOUR COMMAND: ").lower().split(" ", 1)
    inpArg1 = inp[0]
    inpArg2 = None
    if len(inp) > 1:    
        inpArg2 = inp[1]
    if inpArg1 == "quit" or inpArg1 == "q":
        break
    if inpArg1 == "n" or inpArg1 == "e" or inpArg1 == "s" or inpArg1 == "w":
        newRoom = player.location.getRoomDirection(inpArg1)
        if newRoom == None:
            print ("You can not move in that direction.")
        else:
            player.changeLocation(newRoom)
    if inpArg1 == "inventory" or inpArg1 == "i":
        print(f"Your inventory contains: {player.items}")
    if inpArg1 == "look" or inpArg1 == "l":
        print(f"The {player.location} contains: {player.location.items}")


    if inpArg1 == "pick-up" or inpArg1 == "p":
        if inpArg2 == None:
            print("error")
        else:
            currentItem = inpArg2
            # currentItem = currentItem[1]
            # print(room['outside'].addItem(currentItem))
            currentItem = player.location.findItemByName(currentItem)
            if currentItem == None:
                print("error2")
            else:
                player.addItem(currentItem)
                player.location.removeItem(currentItem)


    if inpArg1 == "drop" or inpArg1 == "d":
        if inpArg2 == None:
            print("error4")
        else:
            currentItem = inpArg2
            currentItem = player.findItemByName(currentItem)
            if currentItem == None:
                print("error5")
            else:
                player.removeItem(currentItem)
                player.location.addItem(currentItem)