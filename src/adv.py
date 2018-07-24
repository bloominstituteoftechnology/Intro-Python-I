import textwrap
import sys
# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

rooms = {
    "outside": 
    {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n": "foyer",
        "e": "bridge",
        "i": "show inventory",
        "t": "take item",
        "d": "drop item"
    },

    "foyer": {
        "name": "Foyer",
        "description": """Dim light filters in from the south. Dusty passages run north and east.
You find a potion and a parchment which says 'Drink this to fight foul monsters but beware. Your urge to kill grows with every strike' """,
        "items": ['torch', 'potion', 'parchment'],
        "n": "overlook",
        "s": "outside",
        "e": "narrow",
        "w": "armory",
        "i": "show inventory",
        "t": "take item",
        "d": "drop item"
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """You find the ancient hero's statue and find his sword locked in its scabbard. Beyond,a steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "items": ["hero's sword"],
        "s": "foyer",
        "i": "show inventory",
        "t": "take item",
        "d": "drop item"
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w": "foyer",
        "n": "treasure",
        "s": "cathedral",
        "i": "show inventory",
        "t": "take item",
        "d": "drop item"
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, all but a brass key have been taken by
earlier adventurers. The only exit is to the south.""",
        "items": ["brass key"],
        "s": "narrow",
        "i": "show inventory",
        "t": "take item",
        "d": "drop item"
    },

    "bridge": {
        "name": "Bridge",
        "description": """Rough winds blow acoss a lonely bridge. The smell of dragon fire and brimstone is heavy here.
On the other side you see a red dragon sleeping in the sunlight. It guards the entrance to an ancient cathedral""",
        "w": "outside",
        "n": "cathedral",
        "e": "outside",
        "i": "show inventory",
        "t": "take item",
        "d": "drop item",
        "s": "slay dragon"
    },

    "cathedral": {
        "name": "Cathedral",
        "description": """Broken pews, torn tapestries, and skeletons of past adventurers are all that remain inside.
At the end, sunlight illuminates the lady's chapel. You see a crack in the wall.""",
        "n": "narrow",
        "s": "bridge",
        "i": "show inventory",
        "t": "take item",
        "d": "drop item"
    },

    "armory": {
        "name": "Armory",
        "description": """You find a small armory filled with rusted weapons and some tools. At the far end lies a locked chest
and a blackened shield. You find an encryption on the chest lid: 'The ancient hero offers his sword but only to those he deems worthy' """,
        "items": ["blackened shield"],
        "e": "foyer",
        "i": "show inventory",
        "t": "take item",
        "d": "drop item"
    }

}

""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        "n": "",
        "s": "",
        "e": "",
        "w": "",
    },
"""

# Write a class to hold player information, e.g. what room they are in currently
class Player:
    def __init__(self,room):
        self.room = room
        self.inventory = []
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player(rooms["outside"])
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

quit = False # describes game state

while not quit:
    print(new_player.room["name"])
    print(textwrap.fill(new_player.room["description"]))

    # show items in room when player walks in"items"]
    if "items" in new_player.room:
        print("Items: {0}".format(new_player.room["items"]))
    player_input = input("Where will you go next?")
    # quit game
    if player_input == "q":
        quit = True
        sys.exit(1)

    # validate player input
    if player_input in new_player.room:
        if player_input == "i":
            # show player inventory
            print("Player Inventory: {0}".format(new_player.inventory))
        elif player_input == "t":
            if "items" in new_player.room:
                # player takes an item
                chosen_item = input("What item will you take?")
                chosen_item = chosen_item.lower()
                # player must have key to take hero's sword
                if (chosen_item == "hero's sword") and ("brass key" in new_player.inventory):
                    print("Player unlocks hero's sword from statue")
                    new_player.room["items"].remove(chosen_item)
                    new_player.inventory.append("hero's sword")
                elif chosen_item != "hero's sword":
                    print("Player chose to take the {0}".format(chosen_item))
                    # remove item from room
                    new_player.room["items"].remove(chosen_item)
                    # add item to player inventory
                    new_player.inventory.append(chosen_item)
                else:
                    print("You need the key to unlock the hero's sword")
            else:
                print("There are no items in this room")
        elif player_input == "d":
            if len(new_player.inventory) > 0:
                # drop an item from player inventory
                drop_item = input("What item will you drop? You cannot recover dropped items")
                drop_item = drop_item.lower()
                print("Player dropped the {0}".format(drop_item))
                new_player.inventory.remove(drop_item)
            else:
                # no items to drop
                print("You don't have anything to drop")
        elif player_input == "s" and new_player.room["name"] == "Bridge":
            slay_dragon = input("Are you sure you want to fight the dragon?")
            slay_dragon = slay_dragon.lower()
            if slay_dragon == 'y' or slay_dragon == 'yes':
                print("Player wakes up dragon!!")
                # player can slay dragon with potion alone
                if ("potion" in new_player.inventory):
                    print("Player drinks potion and slays dragon with one punch!")
                    sys.exit(1) # player wins
                # player needs heroes sword and shield to slay dragon without potion
                if ("hero's sword" in new_player.inventory) and ("blackened shield" in new_player.inventory):
                    print("Player blocks dragon fire with the blackened shield and slays dragon with the hero's sword! You Win!")
                    sys.exit(1) # player wins
                else:
                    # player will lose without the right items
                    print("Player is devoured by dragon! Game Over!")
                    sys.exit(1)
            else:
                print("Player avoids fighting the dragon.")
        else:
            new_room = new_player.room[player_input]
            # update player instance with the new room
            new_player.room = rooms[new_room]
    else:
        # player enters an invalid direction
        print("Please enter a valid direction: n, e, s, w, t, d")





