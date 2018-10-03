from room import Room
from player import Player
from weapon import Weapon
from item import Item
import random
# Declare all the rooms
items = {
    "shovel": Item("shovel", "Use this to dig or hit with manually droppable item"),
    "sword": Item("sword", "Use this to chop or slice manually droppable item"),
    "spells": Item("spells", "Book of spells manually droppable item"),
    "bat": Item("bat", "Use this to knock down or hit with manually droppable item"),
    "gun": Item("gun", "Shoot with this manually droppable item"),
    "extinguisher": Item("extinguisher", "Put out fires or use as a decoy, manually droppable item"),
    "coins": Item("coins", "coins count as points, every room has coins This item cannot be mannually dropped"),
    "flashlight": Item("flashlight", "The flashlight helps you see better but can also be used as a weapon careful if you use it as a weapon it may not work anymore as a visual aid."),
}
room = {
    'outside':  Room("outside",
                     "Outside Cave Entrance North of you, the cave mount beckons", [items["coins"]]),

    'foyer':    Room("foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["coins"], items["flashlight"]]),

    'overlook': Room("overlook", """Grand Overlook A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items["spells"],items["coins"]]),

    'narrow':   Room("narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items["coins"]]),

    'treasure': Room("treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items["gun"],items["coins"]]),
    'prison': Room('Prison', """You will have to fight your way out of the prison if you wish to go north.
     If you wish not to fight run left or right""", [items["bat"],items["coins"]]),
    'coward': Room("coward", """You have entered Cowards Forest. You coward! You ran from the fight. Now the goblins have been alerted.  """, [items["shovel"]]),
    'kitchen': Room('Kitchen', """Welcome to the kitchen """, [items["sword"],items["coins"]])

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
room['treasure'].n_to = room['kitchen']
room['kitchen'].e_to = room['prison']
room['prison'].n_to = room['coward']

# Weapons


# Main

rooms = ["outside", "foyer", "overlook",
         "narrow", "treasure", "kitchen", "prison"]

directions = {"n", "s", "e", "w"}
# set of  directions want to key them to the direction.

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
directions = ["n", "s", "e", "w"]
# "i"  should allow one to check inventory. 
moves = ["drop", "grab"]
suppressRoomPrint = False
player = Player(input("What is your name? "), room['outside'])
print("Starting game:\n\n options -> Enter q to quit, n to go North s to go South e to go East w to go West\n\n i should allow you to check your inventory")
while True:
    print(f"{player.currentRoom}")
    option = input(
        "option ->")
    option = option.lower().split(" ")
    if option[0] == "q":
        print("Exiting the game!")
        break
    elif option[0] == "i":
        print(f"You currently have in your inventory the following items: {player.showInventory()}")
    elif directions.count(option[0]) > 0:
        print(player.room_change(option[0]))
    elif moves.count(option[0]) > 0:
        if option[0] == 'grab':
            print(player.grabItem(items[option[1]]))
        elif option[0] == 'drop':
            itemsAvaliable = list(items.keys())
            if itemsAvaliable.count(option[1]) > 0:
                print(player.dropItem(items[option[1]]))
            else:
                print("That item doesn't exist.")

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
