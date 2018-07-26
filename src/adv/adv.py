from room import Room
from player import Player
from item import Item
from item import Treasure

# Declare all the rooms

items = {
    'coins': Treasure("coins", "a pouch of coins", 100),
    'sword': Item("sword", "a rusty old sword"),
    'shield': Item("shield", "a battered old shield"),
    'book': Item("book", "a dusty old book")
}

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'outside', [items['coins'], items['sword'], items['shield']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'foyer'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'overlook'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'treasure', [items['coins'], items['coins'], items['coins']]),
}

# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

startingRoom = 'outside'


def saveGame(player):
    saveFile = open("saves/%s.txt" % player.name, "w+")
    saveFile.write("%s" % player.room.key)
    inventoryData = "//["
    for i in player.inventory:
        inventoryData += "items['%s']," % i.name
    inventoryData += "]"
    saveFile.write("%s" % inventoryData)
    saveFile.write("//")
    roomData = ""
    for key, room in rooms.items():
        roomData += "["
        for item in room.items:
            roomData += "items['%s']," % item.name
        roomData += "];"
    saveFile.write("%s//%d" % (roomData, player.score))
    saveFile.close()
    print("Game saved.")


def loadGame(playerName):
    loadFile = open("saves/%s.txt" % playerName, "r")
    lines = loadFile.read().split('//')
    startingRoom = lines[0]
    inventoryData = lines[1]
    roomData = lines[2].strip(';').split(';')
    playerScore = int(lines[3])
    loadFile.close()
    for index, room in enumerate(rooms.items()):
        # print(index)
        rooms[room[0]].items = eval(roomData[index])
    # print("startingRoom: %s\ninventoryData: %s\nroomData: %s\n" %
    #       (startingRoom, inventoryData, roomData))
    return Player(playerName, rooms[startingRoom], eval(inventoryData), playerScore)


newGame = input("Newgame or Loadgame (n/l): ").lower()
if newGame == "n" or newGame == "new" or newGame == "new game":
    playerName = input("Enter your player name: ")
    player = Player(playerName, rooms[startingRoom], [items['book']])
elif newGame == "l" or newGame == "load" or newGame == "load game":
    playerName = input("Enter the character name you want to load: ")
    loadData = loadGame(playerName)
    player = loadData
    print("Character %s loaded." % playerName)
else:
    print("Restart the program and choose whether to load or start a new game.")
    exit()

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

playing = True
helpString = 'Type n/s/e/w to move in a direction.\nType "i" or "inventory" to check your inventory.\nType "look" or "search" to look around for items.\nType "t" or "take" and the name of the item you want to take to pick up an item.\nType "d" or "drop" and the name of the item in your inventory that you want to drop.\nType "score" to see your score.\nType "q" or "quit" to quit and save.\nType "save" to save the game without quitting.'

print("\n" + player.room.description)

while(playing is True):
    curRoom = player.room
    playerInput = input("Enter a command: ").strip().lower().split()
    command = playerInput[0]
    playerInput.append("")
    secondCommand = playerInput[1]
    if command == "q" or command == "quit":
        print("You have exited the game.")
        saveGame(player)
        playing = False
        break
    elif command == "help":
        print(helpString)
    elif command == "save":
        saveGame(player)
    elif command == "score":
        print("Your score is: %s" % player.score)
    elif command in ["s", "n", "e", "w"]:
        dirAttr = command + "_to"
        if hasattr(curRoom, dirAttr):
            player.room = getattr(curRoom, dirAttr)
            print("\n" + player.room.description)
        else:
            print("You can't go that way.")
    elif command == "look" or command == "search":
        print("You scan your surroundings.")
        for i in curRoom.items:
            print("You find %s." % i.description)
        if len(curRoom.items) == 0:
            print("You find nothing of note.")
    elif command == "i" or command == "inventory":
        print("You check your inventory.")
        for i in player.inventory:
            print("You have %s." % i.description)
    elif command == "t" or command == "take":
        item = next((i for i in curRoom.items if i.name == secondCommand), None)
        if item != None:
            player.inventory.append(item)
            curRoom.items.remove(item)
            print("You picked up %s." % item.description)
            # print(isinstance(item, Treasure))
            if isinstance(item, Treasure) is True:
                # print("True or false " + str(item.taken))
                if item.taken == False:
                    item.on_take(player)
                    print("Looting treasure increases your score by %s!" %
                          item.value)
        else:
            print("There isn't any of that item that you can pick up.")
    elif command == "d" or command == "drop":
        item = next(
            (i for i in player.inventory if i.name == secondCommand), None)
        if item != None:
            player.inventory.remove(item)
            curRoom.items.append(item)
            print("You dropped a %s." % item.name)
        else:
            print("You don't have that object.")
    else:
        print("You entered an invalid command.")
        print(helpString)
