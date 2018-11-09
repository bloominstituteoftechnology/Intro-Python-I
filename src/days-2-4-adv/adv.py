from room import Room
from player import Player
from item import Item, Treasure, LightSource

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance", "North of you, the cave mount beckons", True
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        True,
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}

# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# Add items to rooms

room["outside"].populate_item(
    Item(
        "Crimson", "The weapon fills its bearer with an unquenchable thirst for blood."
    )
)
room["outside"].populate_item(
    Item("Tonic", "Seals wounds and mends broken bones for all injuries sustained.")
)
room["foyer"].populate_item(
    Item(
        "Butcher",
        "Embodiment of the madness and depravity that overwhelmed the people of Cairn following the Grim Dawn.",
    )
)
room["overlook"].populate_item(
    Item(
        "Final",
        "Forged by railyard workers during a desparate battle against the rising Chthonian forces.",
    )
)
room["narrow"].populate_item(
    Item(
        "Codex",
        "Forbidden texts of the witch god Solael, as recorded by Cabalist Hester Maughan.",
    )
)
room["treasure"].populate_item(
    Item(
        "Glyph",
        "Signet granted by Kelphat'Zoth, Grand Harbinger of Ch'Thon, upon his most loyal followers.",
    )
)
room["narrow"].populate_item(
    Item(
        "Aegis",
        "The guiding light of Ishtak cleanses of pain and fills with renewed resolve.",
    )
)

# Add treasures to rooms

room["outside"].populate_item(
    Treasure(
        "Silver",
        "**Silver has become highly prized over gold for the ability to craft armaments.",
        200,
    )
)
room["treasure"].populate_item(
    Treasure(
        "Silver",
        "**Silver has become highly prized over gold for the ability to craft armaments.",
        200,
    )
)
room["overlook"].populate_item(
    Treasure(
        "Scepter",
        "**Ancient folklore spoke of a cloaked figure that traveled the world cleansing disease and mending wounds, never once asking for payment or any other sign of gratitude.",
        800,
    )
)
room["narrow"].populate_item(
    Treasure(
        "Blademaster",
        "**A symbol of mastery in the art of wielding two melee weapons at the same time.",
        650,
    )
)
room["outside"].populate_item(
    LightSource("Lamp", "Let there be light unto the world Lucius said.")
)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

while True:
    new_player = input("Welcome Hero. ")
    new_player = input("What is your name? ")
    if len(new_player) == 0:
        print("Please enter your hero's name.\n")
    else:
        player = Player(new_player, room["outside"])
        player.populate_inventory(
            Item("Bread", "Some hard, crusty bread that looks good right about now.")
        )
        print(f"\n*~*~*~*~*~*\nWelcome to Myst...\n{player.name}\n*~*~*~*~*~*")
        break

print(any(isinstance(x, Item) for x in player.inventory))

# Light Check with filter
def light_check():
    if (
        player.current.is_lit
        or list(filter(lambda x: x.name.lower() == "lamp", player.current.items))
        or list(filter(lambda x: x.name.lower() == "lamp", player.inventory))
    ):
        return True
    else:
        return False


# Light Check with isinstance
# def light_check():
#     if (
#         player.current.is_lit
#         or any(isinstance(x, LightSource) for x in player.current.items)
#         or any(isinstance(x, LightSource) for x in player.inventory)
#     ):
#         return True
#     else:
#         return False


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

while True:
    print(f"\n\n===You are in {player.current.name.upper()}.")
    print(f"{player.current.desc}.\n")
    print("Go [n]orth [e]ast [s]outh [w]est\n")
    print("[search] area")
    print("[inventory] check")
    print("[score] check\n")
    print("[get <item>]")
    print("[drop <item>]\n")
    print("[q]uit\n")
    choice = input("===What to do? ")
    if len(choice) == 1:
        if choice == "q":
            print(f"\nAye, perhaps another day.")
            break
        elif choice == "n":
            player.move_to(choice)
        elif choice == "e":
            player.move_to(choice)
        elif choice == "s":
            player.move_to(choice)
        elif choice == "w":
            player.move_to(choice)
        else:
            print(f"\nPlease make a choice.")
    elif len(choice) > 1:
        format_choice = choice.lower().split(" ")
        if choice == "search":
            if light_check():
                player.current.show_items()
            else:
                print("It's pitch black!")
        elif choice == "inventory":
            if light_check():
                player.show_inventory()
            else:
                print("It's pitch black!")
        elif choice == "score":
            player.show_score()
        elif (format_choice[0] == "get" or format_choice[0] == "take") and len(
            format_choice
        ) == 2:
            if light_check():
                if len(format_choice[1]) > 0:
                    player.add_item(format_choice[1])
                else:
                    print("Enter an item also.")
            else:
                print("Good luck finding that in the dark!")
        elif format_choice[0] == "drop" and len(format_choice) == 2:
            if len(format_choice[1]) > 0:
                player.remove_item(format_choice[1])
            else:
                print("Enter an item also.")
        else:
            print(f"\nTry again.")
    else:
        print(f"\nAgain, where would you like to go?")
