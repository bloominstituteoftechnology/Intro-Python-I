from room import Room
from player import Player
from item import Item, Treasure, LightSource

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
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# item = {
#     'sword':  Item("sword",
#                      "slay the creeps using the sword."),
#
#     'ax':    Item("ax",
#                         """crush them with the ax"""),
#
#     'torch': Item("torch",
#                         """Find your way!"""),
#
#     'amulet':   Item("amulet",
#                          """Stop spells"""),
#
# }

coins = Treasure("coins", "gold coins for the taking")
rubies = Treasure("rubies", "sparkleys")

sword = Item("sword", "slay the creeps using the sword.")
ax = Item("ax", "crush them with the ax")
mace = Item("mace", "fly anything with the mace")



playerStartingItems = [sword]
room['outside'].addItem(ax)
room['foyer'].addItem(mace)
room['treasure'].addItem(coins)
room['treasure'].addItem(rubies)

valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

player = Player(input("What is your name? "), room['outside'],playerStartingItems)

print(" debug string ",player.currentRoom)

while True:
    print(" debug string ",player)
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        elif cmds[0] == "i" or cmds[0] == "inventory":
            player.printInventory()
        elif cmds[0] == "status":
            player.printStatus()
        else:
            print("I did not understand that command.")
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "take" or cmds[0] == "get":
            itemToTake = player.currentRoom.findItemByName(" ".join(cmds[1:]))
            if itemToTake is not None:
                player.addItem(itemToTake)
                player.currentRoom.removeItem(itemToTake)
                print(f"You have picked up {itemToTake.name}")
            else:
                print("You do not see that item.")
        elif cmds[0] == "drop":
            player.dropItem(cmds[1:])
        elif cmds[0] == "score":
            items = player.findItemByName(" ".join(cmds[1:]))
            if items is not None and hasattr(items, "score") and items.score() > 0:
                strengthGain = int(items.eat() / 10)
                player.score += score
                player.item(items)
                del items
                print(f"Your score {score} strength!")
            else:
                print("You cannot eat that.")
        else:
            print("I did not understand that command.")
