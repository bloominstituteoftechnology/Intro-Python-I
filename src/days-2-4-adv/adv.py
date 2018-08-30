from room import Room
from player import Player
from item import Item, Treasure

# Declare all the rooms
# Which rooms are empty?? Who knows?
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

# --------------------Helper Functions-----------------
def helpCommands():
    print("""
    -------------------------------------------
    q = Quit
    i / inventory = Show Player Inventory
    north = Move North
    south = Move South
    east = Move East
    west = Move West
    help = See this menu
    score = Show player score
    show = Show items in a Room
    take/get *item* = Pick up Item from Room
    drop *item = Drop Item in the Room
    --------------------------------------------
    """
          )



# --------------------Adding new items-----------------
new_item = Item("flashlight", "Good light source")
new_item2 = Item("bacon", "Good food source")
new_item3 = Item("gold", "This should belong in the treasure room.")
room['outside'].items.append(new_item)
room['foyer'].items.append(new_item2)
room['treasure'].items.append(new_item3)

# adding treasures
treasure1 = Treasure("money", "currency", 100)
treasure2 = Treasure("chalice", "shiny", 2000)
treasure3 = Treasure("battery", "can go in a flashlight", 5)
room['treasure'].items.append(treasure2)
room['foyer'].items.append(treasure3)
room['overlook'].items.append(treasure1)

# ---------------------Initializing Player--------------
player = Player(room['outside'])
allowed = ['north', 'south', 'east', 'west']
"""print(player.room)
player = Player(room['outside'].n_to)
print(player.room)"""
suppressRoomPrint = False

# --------------------Starting Game Loop----------------
while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print("\n----------------Treasure Game----------------")
        print("You are at {}.".format(player.room.getDescription()))
    message = input("\nWhere do you want to go? (north/south/east/west): ")
    if message == 'quit':
        print("Game over")
        break
    if message not in allowed:
        #print("\nPlease only choose north, south, east, or west.\n")
        newMessage = message.split(" ")
        if len(newMessage) > 1:
            if (newMessage[0] == "take" or newMessage[0] == "get"):
                for item in player.room.items:
                    if item.name == newMessage[1]:
                        player.room.items.remove(item)
                        player.items.append(item)
                        item.on_take(player)
                    else:
                        print("{} is not in the room.".format(newMessage[1]))
            elif (newMessage[0] == "drop"):
                for item in player.items:
                    if item.name == newMessage[1]:
                        player.room.items.append(item)
                        player.items.remove(item)
                        item.on_drop(player.room.name)
                    else:
                        print("You are not holding that item. ")
            else:
                print("An error has occurred.")
        elif (newMessage[0] == "i" or newMessage[0] == "inventory"):
            for item in player.items:
                print("You are holding {}".format(item.name))
        elif (newMessage[0] == "help"):
            helpCommands()
            suppressRoomPrint = True
        elif (newMessage[0] == "show"):
            player.room.showItems()
            suppressRoomPrint = True
        elif (newMessage[0] == "score"):
            player.getScore()
        else:
            print("Not a valid option, enter 'help' for a list of all options.")
    else:
        if hasattr(player.room, message[0] + '_to'):
            # print("Worked!")
            player.room = getattr(player.room, message[0] + '_to')
        elif hasattr(player.room, message[0] + '_to') == False:
            print("That doesn't lead anywhere, please choose another direction.")
            suppressRoomPrint = True
