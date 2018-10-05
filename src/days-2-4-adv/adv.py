import random
from room import Room
from player import Player
from item import Item, Treasure, LightSource


# Items - suppose to have different items in different rooms
items_dic = {
    "AK47":{ 
        "name": "AK47", 
        "description": "The AK-47, AK, or as it is officially known, also known as the Kalashnikov, is a gas-operated, 7.62×39mm assault rifle, developed in the Soviet Union by Mikhail Kalashnikov." 
        },
    "M416":{ 
        "name": "M416", 
        "description": "The Heckler & Koch HK416 is an assault rifle designed and manufactured by Heckler & Koch." 
        },
    "FAK":{ 
        "name": "First Aid Kit", 
        "description":  "A Swedish folk duo that consists of the sisters Klara and Johanna Söderberg" 
        }
}

treasure_dic = {
    "Win":{
        "name": "Chicken", 
        "description": "Winner chicken dinner",
        "value": 50
        },
}

items = [ Item(items_dic[item]["name"], items_dic[item]["description"]) for item in items_dic ]
treasures = [ Treasure(treasure_dic[treasure]["name"], treasure_dic[treasure]["description"], treasure_dic[treasure]["value"]) for treasure in treasure_dic ]
flashlight = [ LightSource(name = "Flashlight", description = "It lights up the darkness") ]

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     items),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                     passages run north and east.""",
                     items),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                     into the darkness. Ahead to the north, a light flickers in
                     the distance, but there is no way across the chasm.""", 
                     items = items, 
                     lightsources = flashlight),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                     to north. The smell of gold permeates the air.""", 
                     items, 
                     treasures),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                     chamber! Sadly, it has already been completely emptied by
                     earlier adventurers. The only exit is to the south.""", 
                     items, 
                     treasures),
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
print("🎮  Welcome to Adventure beta v 0.1")
player = Player(name = input("📝  Please enter your name: \n"), location = room['outside'])
print(f"👋  Hi, { player.name }! You've started your adventure at 🏠 { player.location.get_room() }")
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
# Initialise number of round
number_round = 1

# Valid direction
valid_directions = {
    "n": "n",
    "e": "e",
    "s": "s",
    "w": "w",
}

while True:
    """
    Each new round
    """
    print (f"\n--- Round {number_round} ---\n")
    print("ℹ️\n\nPlease enter n/e/s/w to pick a direction,\nenter d for description of current location,\nenter q for quitting the game,\nenter i for checking items, \nenter s for checking your score")
    if len(player.location.treasures) > 0:
        print(f"👉 {player.location.print_treasures()} 👈 is found!\n")

    """
    Get user input
    """
    cmd = input("➡️  ")
    cmd_tokens = cmd.split(' ') or []

    """
    Process user input
    """
    # unless user wants to quit
    if cmd == "q":
        break
    # if not keep running
    else: 
        while len(cmd_tokens) > 0:
            token = cmd_tokens[0]
            # hotkeys command
            if len(token) is 1:
                if token == "d" and player.location.is_lighted == True:
                    player.location.print_description()
                elif token == "i" and player.location.is_lighted == True:
                    player.get_item()
                elif token == "s":
                    player.get_score()
                elif token in valid_directions and player.location.is_lighted == True:
                    player.travel(valid_directions[token])
                    player.location.generate_items(player)
                else:
                    print(f"⚫  The room is full of darkness... pick up { player.location.lightsources[0].name }")
            # words command
            else:
                if len(cmd_tokens) > 1:
                    next_token = cmd_tokens[1] 
                else:
                    break
                if token == "get":
                    if player.location.is_lighted == True:
                        # for items
                        for item in player.location.items:
                            if next_token == item.name:
                                player.add_item(item)
                                # remove item in room instance
                                player.location.items.remove(item)
                        # for treasures
                        for treasure in player.location.treasures:
                            if next_token == treasure.name:
                                player.add_treasure(treasure)
                                player.location.treasures.remove(treasure)
                    else: 
                        print("⚫   Good luck finding that in the dark!")
                    # for lightsources
                    for lightsource in player.location.lightsources:
                        if next_token == lightsource.name:
                            player.add_lightsource(lightsource)
                            player.location.is_lighted = True
                elif token == "drop":
                    # for items
                    for item in player.items:
                        if next_token == item.name:
                            player.items.remove(item)
                            # remove item in room instance
                            player.location.items.append(item)
                    # for treasures
                    for treasure in player.treasures:
                        if next_token == treasure.name:
                            player.treasures.remove(treasure)
                            player.location.treasures.append(treasure)
                else:
                    print(f"⚠️  Input command is not found")
                # remove item command in token list
                cmd_tokens.pop(1)
            # remove first item
            cmd_tokens.pop(0)

    """
    End this round
    """
    number_round += 1