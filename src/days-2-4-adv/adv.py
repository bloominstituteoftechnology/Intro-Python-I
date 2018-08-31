from dicts import items, rooms
from classes import Room, Player, Item, Treasure, LightSource

def printErrorString(errorString):
    print(f'\x1b[1;31;40m\n{errorString}\x1b[0m')

player = Player(rooms['outside'])

while True:
    print("\nYou are in the {}.".format(player.room.name))
    if player.room.is_lit or player.check_for_light():
        print(player.room.description)
        if player.room.items:
            player.room.inventory()
    else:
        printErrorString("It's pitch black!")
    inp = input("\n>>> ").split(" ")
    if 1 <= len(inp) <= 2:
        command = inp[0]
        target = inp[1] if len(inp) == 2 else None
        if command == "quit":
            printErrorString("YOU HAVE DIED.\n")
            break
        elif command == "score":
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
                player.room = rooms[player.room.adjacent_rooms[command]]
        elif command == "get":
            if not player.room.is_lit and not player.check_for_light():
                printErrorString("Good luck finding that in the dark!")
            elif not player.room.items:
                printErrorString("There is nothing for you to take.")
            elif not player.room.check_for_item(target):
                printErrorString("That item is not present.")
            else:
                new_item = items[target]
                player.room.remove_item(new_item)
                player.get(new_item)
                if isinstance(new_item, Treasure):
                    if not new_item.picked_up:
                        player.score += new_item.value
                        new_item.on_take()
        elif command == "drop":
            if not player.items:
                printErrorString("You have no items.")
            elif not player.check_for_item(target):
                printErrorString("You have no such item.")
            else:
                dropped_item = items[target]
                player.drop(dropped_item)
                player.room.add_item(dropped_item)
                if isinstance(dropped_item, LightSource):
                    dropped_item.on_drop()
        else:
            printErrorString("I did not recognize that command.")
