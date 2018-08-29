from room import Room
from player import Player
from item import itemList
from item import Item
from room import roomlist

roomlist['outside'].connectRooms(roomlist['foyer'], "n")
roomlist['foyer'].connectRooms(roomlist['overlook'], "n")
roomlist['foyer'].connectRooms(roomlist['narrow'], "e")
roomlist['narrow'].connectRooms(roomlist['treasure'], "n")
roomlist['overlook'].connectRooms(roomlist['treasure'], "e")
roomlist['foyer'].connectRooms(roomlist['dungeon'], "w")



player = Player(input("\nWhat is your name?:"),  roomlist['outside'], [itemList['torch'], itemList['hat']])
print(f"Welcome, {player.name} !\n")

while True:
    
    print(f"\nCurrent Room: {player.location.title}\n\
Room contains: {player.location.print_items()}\n")

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
    if inp[0]=="l":
        print(f"Current Room Description: {player.location.description}")
        input("Press Enter to Exit Description")
