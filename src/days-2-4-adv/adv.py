from dicts import item
from dicts import room
from classes import Room
from classes import Player
from classes import Item
from classes import Treasure

def printErrorString(errorString):
    print(f'\x1b[1;31;40m\n{errorString}\x1b[0m')

player = Player(room['outside'])

while True:
    print("\nYou are in the %s. %s" % (player.room.name, player.room.description))
    if player.room.items:
        player.room.inventory()
    inp = input("\n>>> ").split(" ")
    if len(inp) == 1 or len(inp) == 2 and not inp[1]:
        command, target = inp[0], None
        if command == "quit":
            printErrorString("YOU HAVE DIED.\n")
            break
        if command == "score":
            player.score_report()
        elif command == "items":
            if player.items:
                player.inventory()
            else:
                printErrorString("You have no items.")
        elif command in ['n', 's', 'e', 'w']:
            if player.room.adjacent_rooms[command] == None:
                printErrorString("You cannot move that way.")
            else:
                player.room = room[player.room.adjacent_rooms[command]]
        else:
            printErrorString("I did not recognize that command.")
    elif len(inp) == 2:
        command, target = inp
        if command == "get" and not player.room.items:
            printErrorString("There is nothing for you to take.")
        elif command == "drop" and not player.items:
            printErrorString("You have no items.")
        elif command == "get" and not player.room.check_for_item(target):
            printErrorString("That item is not present.")
        elif command == "drop" and not player.check_for_item(target):
            printErrorString("You have no such item.")
        elif command == "get":
            new_item = item[target]
            player.room.remove_item(new_item)
            player.get(new_item)
            if type(new_item) is Treasure:
                if not new_item.picked_up:
                    player.score += new_item.value
                    new_item.on_take()
        elif command == "drop":
            player.drop(item[target])
            player.room.add_item(item[target])
        else:
            printErrorString("I did not recognize that command.")
    else:
        printErrorString("I did not recognize that command.")
