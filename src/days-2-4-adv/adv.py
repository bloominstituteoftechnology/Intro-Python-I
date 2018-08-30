import os
from dicts import item
from dicts import room
from classes import Room
from classes import Player
from classes import Item

player = Player(room['outside'])

while True:
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("\nYou are in the %s. %s" % (player.room.name, player.room.description))
    if player.room.items:
        print(f"\nInside the room, you see the following items: {', '.join(item.name for item in player.room.items)}")
    inp = input("\n>>> ").split(" ")
    if len(inp) == 1 or len(inp) == 2 and not inp[1]:
        command, target = inp[0], None
        if command == "q":
            print("\nYOU HAVE DIED.")
            break
        elif command == "items":
            if player.items:
                print(f"\nYou have the following items: {', '.join(item.name for item in player.items)}")
            else:
                print("\nYou have no items.")
        elif command in ['n', 's', 'e', 'w']:
            if player.room.adjacent_rooms[command] == None:
                print("\nYou cannot move that way.")
            else:
                new_room = player.room.adjacent_rooms[command]
                player.room = room[new_room]
        else:
            print ("\nI did not recognize that command.")
    elif len(inp) == 2:
        command, target = inp
        if command == "get" and not player.room.items:
            print("\nThere is nothing for you to take.")
        elif command == "drop" and not player.items:
            print("\nYou have no items.")
        # elif command == "get" and target not in item.name for item in player.room.items:
        #     print("\nThat item is not present.")
        # elif command == "drop" and target not in player.items:
        #     print("\nYou have no such item.")
        elif command == "get":
            player.get(item[target])
            player.room.remove_item(item[target])
        elif command == "drop":
            player.drop(item[target])
            player.room.add_item(item[target])
        else:
            print ("\nI did not recognize that command.")
    else:
        print ("\nI did not recognize that command.")
