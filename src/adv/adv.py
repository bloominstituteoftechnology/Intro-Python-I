from room import Room
from player import Player
from item import Item, Treasure
import textwrap

# Declare all the rooms
item = {
    'torch' : Item(name = "Torch", description = "Ahh Light"),
}

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
earlier adventurers. The only exit is to the south. """),
}

t = Item("Torch", "And Let There Be Light")
h = Treasure("Poo", "I don't know why you would pick this up", 100)
room['outside'].item.append(h)



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
player = Player(room['outside'])
player.item.append(t)

# Write a loop that:
def cardDirection(self, currentArea):
    destination = self + '_to'
    if hasattr(currentArea, destination):
       return getattr(currentArea, destination)
    else: print("YOU SHALL NOT PASS")
    return currentArea

over = False

while over is False:
    print("\n{}\n".format(player.currentArea.name))
    for each in textwrap.wrap(player.currentArea.description):
        print(each)
    print("Items in Area: " + str(player.currentArea.item))
    u = input("\nWhich Direction?\n")
   
    if player.currentArea is room['treasure']:
        print("You return home dejected")
        over = True
    elif len(u) > 2:
        if u == "take item":
            if not player.currentArea.item:
                print("You grasp air....")
            else:
                print("You picked up an item " + str(player.currentArea.item))
                player.currentArea.item[0].on_take(player)
                player.item.append(player.currentArea.item)
                player.currentArea.item = []
        elif u == "drop item":
            player.currentArea.item.append(player.item[-1])
            player.item.pop()
        elif u == "take": print("What did you mean to take? item? Use two words")
        elif u == 'inventory': print("Player Held Items: " + str(player.item))
        else: print("Commands: n,s,w,e | take item | q | quit")
    elif u in ["n", "s", "e", "w"]:
        player.currentArea = cardDirection(u, player.currentArea)
    elif u == 'i':
        print("Player Held Items: " + str(player.item))
        print("Player Score: " + str(player.score))
    elif u == "q":
        print("Quitter")
        over = True
    elif u == "t": print("Did you mean take? If so take what? item? Use two words")
    else: print("Commands: n,s,w,e | take item | q | quit")



#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

