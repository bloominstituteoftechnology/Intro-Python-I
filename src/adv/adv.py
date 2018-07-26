import os
from room import Room
from player import Player
from item import Item

# Declare the items
items = {
    'jewel': Item("jewel",
        ["glittering"],
        "It is a deep red hue and seems to pulse to an unheard rhythm."),
    'locket': Item("locket", 
        ["battered", "silver"],
        "Opening it reveals a faded photograph of two lovers."),
    'dagger': Item("dagger",
        ["thin"],
        "It looks like it could be used to stab somebody.")
}

# Declare the rooms
rooms = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", True),
    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", True, [items['dagger']]),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", True, [items['locket']]),
    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.", False),
    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! The only exit is to the south.", False, [items['jewel']]),
}

# Link rooms together

rooms['outside'].connections['n'] = rooms['foyer']
rooms['foyer'].connections['s'] = rooms['outside']
rooms['foyer'].connections['n'] = rooms['overlook']
rooms['foyer'].connections['e'] = rooms['narrow']
rooms['overlook'].connections['s'] = rooms['foyer']
rooms['narrow'].connections['w'] = rooms['foyer']
rooms['narrow'].connections['n'] = rooms['treasure']
rooms['treasure'].connections['s'] = rooms['narrow']


#
# Player input handling methods
#

def process_command(command):
    tokens = [token.lower() for token in command.split(" ")]

    # Commands with no arguments
    simple_commands = {
        "n": lambda: move("n"),
        "w": lambda: move("w"),
        "e": lambda: move("e"),
        "s": lambda: move("s"),
        "q": quit_game,
        "quit": quit_game,
        "i": print_inventory,
        "inventory": print_inventory,
        "h": print_help,
        "help": print_help,
        "score": print_score
    }

    # Commands with one or more arguments
    complex_commands = {
        "move": move,
        "inspect": inspect_item,
        "get": take_item,
        "take": take_item,
        "drop": drop_item,
    }

    # Handle 'it' as a stand-in for an item
    if len(tokens) is 2 and tokens[1] == "it":
        tokens[1] = player.last_item

    if tokens[0] in simple_commands:
        simple_commands[tokens[0]]()
    elif len(tokens) > 1 and tokens[0] in complex_commands:
        complex_commands[tokens[0]](tokens[1])
    else:
        prompt("Invalid command. Enter 'help' for a list of commands.")

def move(direction):
    # the first letter of the direction is all we need
    dir = direction[0]
    if dir in player.room.connections:
        player.room = player.room.connections[dir]
    else:
        prompt("You cannot go that way")

def take_item(item_name):
    if player.room.has_item(item_name):
        prompt(f"You take the {item_name} from the {player.room.name}.")
        player.take_item_from_room(item_name, player.room)
        player.last_item = item_name
    else:
        prompt(f"There are no {item_name}s here to take")

def drop_item(item_name):
    if player.has_item(item_name):
        prompt(f"You drop the {item_name} in the {player.room.name}")
        player.drop_item_in_room(item_name, player.room)
        player.last_item = item_name
    else:
        prompt(f"You have no {item_name}s to drop")

def inspect_item(item_name):
    item = None
    for location in [player, player.room]:
        if location.has_item(item_name):
            item = location.get_item(item_name)
    
    if item:
        text = tabulate(str(item).capitalize(), "\n", item.description, bullet="")
    else:
        text = f"No {item_name}s in {player}'s inventory or this room"
    
    prompt(text)

def quit_game():
    prompt("Thanks for playing!")
    exit()

#
# Display methods
#

def print_turn():
    clear()
    print(f"{player} is in the {player.room.name}\n")
    print(player.room)
    if player.room.items:    
        item_text = tabulate(
            "\nYou see the following in this room:\n",
            *list(map(str, player.room.items)))

        print(item_text)

def print_inventory():
    if player.items:
        inventory_text = tabulate(
            f"{player.name} is carrying:\n",
            *map(str, player.items))
    else:
        inventory_text = f"{player.name} is not carrying anything."

    prompt(inventory_text)


def print_help():
    help_text = tabulate(
        "Available commands:\n",
        "move < north | east | south | west >",
        "take < item >",
        "drop < item >",
        "inspect < item >",
        "quit",
        "inventory",
        "help")

    prompt(help_text)

def print_score():
    score_text = tabulate(
        f"{player.name}'s score:\n",
        f"Items: {player.score['items']}",
        f"Monsters: {player.score['monsters']}",
        f"Total: {player.get_score()}")

    prompt(score_text)

def clear():
    os.system('cls' or 'clear')

def pause():
    input("\nPress Enter to continue...")

def prompt(message):
    clear()
    print(message)
    pause()

def tabulate(*lines, bullet="-"):
    join_string = f"\n  {bullet} "
    return join_string.join(lines)

#
# Main loop
#

# Make a new player object that is currently in the 'outside' room.
name = input("Welcome to the Dungeon of Diogenes! Who are you? ")
player = Player(name, rooms['outside'])
while True:
    print_turn()
    process_command(input("\nEnter choice (or help): "))