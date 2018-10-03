import random
from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items),
}

# Items - suppose to have different items in different rooms
items = {
    "1": "AK47",
    "2": "M416",
    "3": "M16A4",
    "4": "AWM",
    "5": "First Aid Kit"
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
    print("ℹ️\n\nPlease enter n/e/s/w to pick a direction,\nenter d for description of current location,\nenter q for quitting the game,\nenter i for checking items\n")

    """
    Get user input
    """
    cmd = input("➡️  ")
    
    """
    Process user input
    """
    if cmd is "q":
        break
    if cmd is "d":
        player.location.print_description()
    if cmd is "i":
        player.get_item()
    elif cmd in valid_directions:
        player.travel(valid_directions[cmd])
        player.location.generate_items(player)

    """
    End this round
    """
    number_round += 1