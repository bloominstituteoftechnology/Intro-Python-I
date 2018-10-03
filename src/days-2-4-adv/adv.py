from room import Room
from player import Player

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons""", "spear"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "broadsword club"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "spear katana"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "scimitar"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "katana broadsword scimitar"),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#print(room['treasure'].inventory)

# Main

valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "north": "n", "south": "s", "east": "e", "west": "w",
                    "forward": "n", "backward": "s", "right": "e", "left": "w"}

valid_items = {"katana": "katana", "spear": "spear", "broadsword": "broadsword",
                    "scimitar": "scimitar", "club": "club"}

nameInput = input("\n\nHello adventurer! Please enter your name: ")
player = Player(nameInput, room['outside'])
print(f"\n\n{player.currentRoom}\n\nWhich direction do you want to go: N, S, E, or W?")

while True:
    cmds = input("\n-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        elif cmds[0] == "i" or cmds[0] == "inventory":
            player.seeInventory()
        else:
            print("\n\nI did not understand that command; Press q to quit")
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "get" or cmds[0] == "take":
            if cmds[1] in valid_items:
                player.pickUpItem(valid_items[cmds[1]])
                player.currentRoom.removeItem(valid_items[cmds[1]])
        elif cmds[0] == "drop":
            if cmds[1] in valid_items:
                player.dropItem(valid_items[cmds[1]])
                player.currentRoom.addItem(valid_items[cmds[1]])
        else:
            print("\n\nI did not understand that command; Press q to quit")