from room import Room
from player import Player
from item import Item, LightSource, Treasure, Weapon

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
chamber! Sadly, it has already been completely emptied except 
for the remains of a previous adventurer. The only exit is to the south."""),

    'throne': Room("Throne Room",
"""The room opens up immensely, wide enough to
fit over a hundred people and a ceiling that
reached very high. Along the top of the walls
there are windows that light the room from the
outside. Across from the entance on the other
side of the room, you notice a throne.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].w_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].n_to = room['throne']
room['overlook'].e_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

rock = Item("Rock", "This is a rock.")
lantern = LightSource("Lantern", "A lantern that emits light.")
coins = Treasure("Coins", "A small pile of coins.", 50)
sword = Weapon("Sword", "A standard arming blade.", 10)
big_rock = Item("Big Rock", "This is a big rock.")

room['outside'].addItem(rock)
room['outside'].addItem(big_rock)
room['foyer'].addItem(lantern)
room['overlook'].addItem(coins)
room['treasure'].addItem(sword)

room['outside'].light = True
room['foyer'].light = True
room['overlook'].light = True
room['throne'].light = True



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
recent_item = []

validDirections = {"n": "n", "s": "s", "e": "e", "w": "w", "north": "n", "south": "s", "east": "e", "west": "w"}

player = Player(input("What is your name?"), room['outside'])
print(player.currentRoom)

while True:
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in validDirections:
            player.travel(validDirections[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        elif cmds[0] == "i" or cmds[0] == "inventory":
            player.printInventory()
        elif cmds[0] == "p" or cmds[0] == "score":
            print(f"You have {player.score} points.")
        elif cmds[0] == "stats":
            player.printStats()
        else:
            print("I did not understand that command.")    
    else:
        if cmds[0] == "look":
            if cmds[1] in validDirections:
                player.look(validDirections[cmds[1]])
        elif cmds[0] == "take":
            if cmds[1] == "it":
                itemToTake = player.currentRoom.findItembyName(recent_item[0])
                if itemToTake is not None:
                    player.addItem(itemToTake)
                    player.currentRoom.removeItem(itemToTake)
                    print(f"You have picked up {itemToTake.name}")
                else:
                    print("You do not see that item.")
            else:
                itemToTake = player.currentRoom.findItembyName(" ".join(cmds[1:]))
                if itemToTake is not None:
                    player.addItem(itemToTake)
                    player.currentRoom.removeItem(itemToTake)
                    print(f"You have picked up {itemToTake.name}")
                    if len(recent_item) > 0:
                        recent_item.pop()
                    recent_item.append(" ".join(cmds[1:]))
                else:
                    print("You do not see that item.")
        elif cmds[0] == "drop":
            if cmds[1] == "it":
                itemToDrop = player.findItembyName(recent_item[0])
                if itemToDrop is not None:
                    player.removeItem(itemToDrop)
                    player.currentRoom.addItem(itemToDrop)
                    print(f"You have dropped {itemToDrop.name}")
                else:
                    print("You are not holding that item.")
            else:
                itemToDrop = player.findItembyName(" ".join(cmds[1:]))
                if itemToTake is not None:
                    player.removeItem(itemToDrop)
                    player.currentRoom.addItem(itemToDrop)
                    print(f"You have dropped {itemToDrop.name}")
                    if len(recent_item) > 0:
                        recent_item.pop()
                    recent_item.append(" ".join(cmds[1:]))                    
                else:
                    print("You are not holding that item.")
        elif cmds[0] == "equip":
            if cmds[1] == "it":
                itemToEquip = player.findItembyName(recent_item[0])
                if itemToEquip is not None:
                    if hasattr(itemToEquip,'equippable'):
                        player.equipItem(itemToEquip)
                        player.removeItem(itemToEquip)
                        print(f"You have equipped {itemToEquip.name}")
                    else:
                        print("You cannot equip this item.")
                else:
                    print("You are not holding that item.")
            else:
                itemToEquip = player.findItembyName(" ".join(cmds[1:]))            
                if itemToEquip is not None:
                    if hasattr(itemToEquip,'equippable'):
                        player.equipItem(itemToEquip)
                        player.removeItem(itemToEquip)
                        print(f"You have equipped {itemToEquip.name}")
                        if len(recent_item) > 0:
                            recent_item.pop()
                        recent_item.append(" ".join(cmds[1:]))
                    else:
                        print("You cannot equip this item.")
                else:
                    print("You are not holding that item.") 
        elif cmds[0] == "unequip":
            if cmds[1] == "it":
                itemToUnequip = player.findItembyName(recent_item[0])
                if itemToUnequip is not None:
                    player.unequipItem(itemToUnequip)
                    player.addItem(itemToUnequip)
                    print(f"You have unequipped {itemToUnequip.name}")
                else:
                    print("You are not holding that item.")
            else:
                itemToEquip = player.findItembyName(" ".join(cmds[1:]))
                if itemToUnequip is not None:
                    player.unequipItem(itemToUnequip)
                    player.addItem(itemToUnequip)
                    print(f"You have unequipped {itemToUnequip.name}")
                    if len(recent_item) > 0:
                        recent_item.pop()
                    recent_item.append(" ".join(cmds[1:]))
                else:
                    print("You are not holding that item.") 
        else:
            print("I did not understand that command.")  