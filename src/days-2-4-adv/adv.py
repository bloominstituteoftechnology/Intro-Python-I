from room import Room
from player import Player
from game_map import Map
from item import Item
from item import Treasure
from item import Lightsource


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [], True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [], False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [], False),
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

# Add items to rooms
room["outside"].add_item(Lightsource("torch","Should be enough to see..."))
room["foyer"].add_item(Item("sword","Not the sharpest..."),Treasure("spoon","I think it's worth something.", 10, False))
room["overlook"].add_item(Treasure("ruby","Shines bright...",20, False))
room["treasure"].add_item(Treasure("coin","At least it's something.", 15, False))
# Nothin in narrow and treasure


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room["outside"])
map = Map()
print(player.current_room.items[0].name)


print(f"\n\nWelcome adventurer, you are currently in {player.current_room.name}. {player.current_room.descr}\n")
print("""              XXXXXXXX XXX XXXXX
            XXXX XX XXXXXXXX XX XXXXXX
           XXXX XXXXXXXXXX XXXX   XXXX
           XX          XXXXX         X
              +----------------+
              |  Overlook      |
              +------+ +-------+
                     | |
                     | |           +------------+
                     | |           |  Treasure  |
                     | |           |            |
                     | |           +----+ +-----+
                 +---+ +----+           | |
                 |  Foyer   +-----------+ | <---- Narrow
                 |          +-------------+
                 +---+  +---+
XXXXXXXXXX           |  |             XXXXX
         XXXXXXXXXXXX+  +XXXXXXXXXXXXXX

                    Outside
""")
# Write a loop that:
#
# * Prints the current room name
inp = ""
while inp != "q":
    print(f"\nYou are now in {player.current_room.name}. {player.current_room.descr}.\nPress 'm' for map and 'i' for inventory.")
    inp = input("Where would you like to go?\n")
    user_input = inp.split(" ")
    # Map
    if(user_input[0] == "m"):
        map.game_map(player.current_room.name)

    # Inventory
    elif(user_input[0] == "i"):
        print(player.inventory)

    # Movement
    elif (user_input[0] == "n" or user_input[0] == "e" or user_input[0] == "w" or user_input[0] == "s"):
        player.current_room = player.move(user_input[0])

    # Take/drop items
    elif (len(user_input) == 2):
        player.actions(user_input, player.current_room)

    elif (user_input[0] == "search"):
        player.search(player.current_room)
    
    # Score
    elif(user_input[0] == "score"):
        print(f"Your score is currently: {player.score}")

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
