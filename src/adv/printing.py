import os

def turn(player):
    clear()
    print(f"{player} is in the {player.room}\n")

    # Nothing can be seen if the room is dark and player has no light source
    if not player.can_see():
        print("It's too dark to see anything!")
        return

    print(player.room.describe())
    if player.room.items:    
        item_text = tabulate(
            "\nYou see the following in this room:\n",
            *format_items(player.room.items))

        print(item_text)

def inventory(player):
    if player.items:
        inventory_text = tabulate(
            f"{player} is carrying:\n",
            *format_items(player.items))
    else:
        inventory_text = f"{player} is not carrying anything."

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
        f"{player}'s score:\n",
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

def pause(string):
    return input(f"\n{string}")

def prompt(message, prompt_message="Press Enter to continue..."):
    clear()
    print(message)
    return pause(prompt_message)

def tabulate(*lines, bullet="-"):
    join_string = f"\n  {bullet} "
    return join_string.join(lines)

def format_items(items):
    return [f"A {item}" for item in items]