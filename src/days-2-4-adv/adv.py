from room import Room
from player import Player
from item import itemList
from item import Item
from room import roomlist
from item import LightSource

roomlist['outside'].connectRooms(roomlist['foyer'], "n")
roomlist['foyer'].connectRooms(roomlist['overlook'], "n")
roomlist['foyer'].connectRooms(roomlist['narrow'], "e")
roomlist['narrow'].connectRooms(roomlist['treasure'], "n")
roomlist['overlook'].connectRooms(roomlist['treasure'], "e")
roomlist['foyer'].connectRooms(roomlist['dungeon'], "w")


player = Player(input("\nWhat is your name?:"),
 roomlist['outside'], [itemList['torch'], itemList['hat']], 0)
print(f"Welcome, {player.name} !\n")

playing = True
while(playing):
    print(f"\n\033[92mCurrent Room:\033[0m \033[95m{player.location.title}\033[0m\n---------\
-----------------\n\033[92mRoom contains:\033[94m{player.location.check_for_light(player)}\033[0m\033[0m\n--------------------------")

    inp = input("What is your command: ").split(" ")

    if inp[0] == "q":
        break
    if inp[0] =="n" or inp[0] =="s" or inp[0] =="w" or inp[0] =="e":
        player.move(inp[0])
    if inp[0] =="get" or inp[0] =="take":
        player.get(inp[1])
    if inp[0] =="drop":
        player.drop(inp[1])
    if inp[0]=="i":
        player.player_inventory()
    if inp[0] == "score":
        player.get_score()
    if inp[0] == "inspect":
        player.inspect(inp[1])
    if inp[0]=="l":
        print(f"\n\033[92mCurrent Room Description:\033[0m \n\033[95m{player.location.description}\033[0m")
        input(f"\x1b[1;31;40mPress Enter to Exit Description\x1b[0m")

    if player.score == 57:
        print('CONGRATULATIONS, YOU HAVE WON THE GAME')
        playing = False