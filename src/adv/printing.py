import os

def turn(player):
    clear()
    print(f"{player} is in the {player.room.name}\n")
    print(player.room)
    if player.room.items:    
        item_text = tabulate(
            "\nYou see the following in this room:\n",
            *list(map(str, player.room.items)))

        print(item_text)

def inventory(player):
    if player.items:
        inventory_text = tabulate(
            f"{player.name} is carrying:\n",
            *map(str, player.items))
    else:
        inventory_text = f"{player.name} is not carrying anything."

    prompt(inventory_text)


def help():
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

def score(player):
    score_text = tabulate(
        f"{player.name}'s score:\n",
        f"Items: {player.score['items']}",
        f"Monsters: {player.score['monsters']}",
        f"Total: {player.get_score()}")

    prompt(score_text)

def item(item):
    text = tabulate(
        str(item).capitalize(), 
        "\n", 
        item.description, 
        bullet="")

    prompt(text)

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