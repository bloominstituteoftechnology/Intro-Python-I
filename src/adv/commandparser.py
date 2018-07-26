import printing

def process_command(command, player):
    tokens = [token.lower() for token in command.split(" ")]

    # Commands with no arguments
    simple_commands = {
        "n": lambda: move("n", player),
        "w": lambda: move("w", player),
        "e": lambda: move("e", player),
        "s": lambda: move("s", player),
        "q": quit_game,
        "quit": quit_game,
        "i": lambda: printing.inventory(player),
        "inventory": lambda: printing.inventory(player),
        "h": printing.help,
        "help": printing.help,
        "score": lambda: printing.score(player)
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
        # Pass along the player object to complex commands
        complex_commands[tokens[0]](tokens[1], player)
    else:
        printing.prompt("Invalid command. Enter 'help' for a list of commands.")

def move(direction, player):
    # the first letter of the direction is all we need
    dir = direction[0]
    if dir in player.room.connections:
        player.room = player.room.connections[dir]
    else:
        printing.prompt("You cannot go that way")

def take_item(item_name, player):
    if not player.can_see():
        printing.prompt(f"{player.name} cannot see well enough to take anything.")
    elif player.room.has_item(item_name):
        player.take_item_from_room(item_name, player.room)
        player.last_item = item_name
    else:
        printing.prompt(f"There are no {item_name}s here to take")

def drop_item(item_name, player):
    if player.has_item(item_name):
        printing.prompt(f"{player} drops the {item_name} in the {player.room.name}")
        player.drop_item_in_room(item_name, player.room)
        player.last_item = item_name
    else:
        printing.prompt(f"{player} has no {item_name}s to drop")

def inspect_item(item_name, player):
    # Check both inventory and the floor
    for location in [player, player.room]:
        if location.has_item(item_name):
            printing.item(location.get_item(item_name))
            return
    
    printing.prompt(f"No {item_name}s in {player}'s inventory or this room")
    
def quit_game():
    printing.prompt("Thanks for playing!")
    exit()