from room import Room
from player import Player
from weapon import Weapon
from item import Item
from item import Treasure
from item import LightSource
from time import sleep
import random
import os 
# Declare all the rooms
lights = {
    "flashlight": LightSource("flashlight", "The flashlight helps you see better but can also be used as a weapon careful if you use it as a weapon it may not work anymore as a visual aid."),
    "latern" : LightSource("latern", "use this to see in dark rooms, able to use underwater, may break if dropped"),
    "torch" : LightSource("torch", "use as a light source torch stakes do not stay lit when wet"),
}

items = {
    "shovel": Item("shovel", "Use this to dig or hit with manually droppable item"),
    "sword": Item("sword", "Use this to chop or slice manually droppable item"),
    "spells": Item("spells", "Book of spells manually droppable item"),
    "bat": Item("bat", "Use this to knock down or hit with manually droppable item"),
    "gun": Item("gun", "Shoot with this manually droppable item"),
    "extinguisher": Item("extinguisher", "Put out fires or use as a decoy, manually droppable item"),
    "coins": Item("coins", "coins count as points, every room has coins This item cannot be mannually dropped"),
    "key": Item("key", "Master key that can unlock anything might be worth holding on to."),
    "scuba": Item("scuba", "Scuba Mask allows you to breathe under water for extended periods of time.")
}

treasures = {
    "gold": Treasure(1000, "gold", "Chest full of Gold. The chest features 1000 points worth of gold. You will need a master key to unlock it!"),
    "silver": Treasure(500, "silver", "500 points worth of valuable silver at the bottom of the pool. YOu will need a scuba mask due the pool being 50 feet deep. Silvers at the bottom."),
    "wallet": Treasure (250, "wallet", "You have found the kings wallet featuring 250 points"),
}

room = {
    'outside':  Room("outside",
                     "Outside Cave Entrance North of you, the cave mount beckons", [items["coins"],treasures["gold"]],False),

    'foyer':    Room("foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["coins"], lights["flashlight"],treasures["silver"]], True),

    'overlook': Room("overlook", """Grand Overlook A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items["spells"],items["coins"],treasures["wallet"]], True),

    'narrow':   Room("narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items["coins"]], is_light = True),

    'treasure': Room("treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items["gun"],items["coins"]], is_light = True ),
    'prison': Room('Prison', """You will have to fight your way out of the prison if you wish to go north.
     If you wish not to fight run left or right""", [items["bat"],items["coins"]]),
    'coward': Room("coward", """You have entered Cowards Forest. You coward! You ran from the fight. Now the goblins have been alerted.  """, [items["shovel"]], is_light = True),
    'kitchen': Room('Kitchen', """Welcome to the kitchen """, [items["sword"],items["coins"]], is_light = True)
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



directions = ["n", "s", "e", "w"]
# set of  directions want to key them to the direction.

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:

# "i"  should allow one to check inventory. 
moves = ["drop", "grab", "look"]
suppressRoomPrint = False
player = Player(input("What is your name? "), room['outside'])
print("Starting game:\n\n options -> Enter q to quit,\n score to view currentScore\n n to go North\n s to go South\n e to go East\n w to go West\n\n i should allow you to check your inventory\n\n")
while True:
    #sleep(20) #implement for production currently commented out for development purposes.
    #os.system('cls') #clears out previous input. 
    print(f"{player.currentRoom}\n\n")
    option = input(
        "option ->")
    option = option.lower().split(" ")
    if option[0] == "q":
        print("Exiting the game!")
        break
    elif option[0] == "d":
        print(player.currentRoom.getDirections())
    elif option[0] == "i":
        print(f"You currently have in your inventory the following items: {player.showInventory()}\n\n")
    elif option[0] == "score":
        print(player.currentScore())
    elif directions.count(option[0]) > 0:
        print(player.room_change(option[0]))
    elif moves.count(option[0]) > 0:
        if len(option) > 1:
            if option[0] == 'grab':
                if player.looked:
                #check what type of instance the item is.
                    if list(items.keys()).count(option[1]) > 0:
                        print(items[option[1]].on_take())
                        print(player.grabItem(items[option[1]]))
                    elif list(lights.keys()).count(option[1]) > 0:
                        print(lights[option[1]].on_take())
                        print(player.grabItem(lights[option[1]]))
                    elif list(treasures.keys()).count(option[1]) > 0:
                        print(treasures[option[1]].on_take())
                        print(player.grabItem(treasures[option[1]], treasures[option[1]].value, True))
                else:
                    print(f"You must look before you grab\n Use keyword\n\n look")
            elif option[0] == 'drop':
                itemsAvaliable = list(items.keys()) + list(treasures.keys()) + list(lights.keys())
                if itemsAvaliable.count(option[1]) > 0:
                    # check what type of instance the item is 
                    # alternatively could have done a isinstance but would have required more lines of code.
                    if list(items.keys()).count(option[1]) > 0:
                        if option[1] != "coins":
                            print(items[option[1]].on_drop())
                        print(player.dropItem(items[option[1]]))
                    elif list(lights.keys()).count(option[1]) > 0:
                        print(lights[option[1]].on_drop())
                        print(player.dropItem(lights[option[1]]))
                    elif list(treasures.keys()).count(option[1]) > 0:
                        print(treasures[option[1]].on_drop())
                        print(player.dropItem(treasures[option[1]]))
                else:
                    print(f"That item doesn't exist.\n\n")
        
        elif option[0] == 'look':
            print(player.lookAround())
            #sleep(10)
        else:
            print(f"choose what you wish to {option[0]}")
    else:
        print("That is not a valid choice")

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
