from room import Room
from player import Player
from item import Item

# Declare all the rooms

items = {
    'coins': Item("coins", "a pouch of coins"),
    'sword': Item("sword", "a rusty old sword"),
    'shield': Item("shield", "a battered old shield"),
    'book': Item("book", "a dusty old book")
}

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'outside', [items['sword'], items['shield']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'foyer'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'overlook'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'treasure', [items['coins']]),
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
        inventoryData += "items[%s]," % i.name
        # saveFile.write(",%s" % i.name)
    inventoryData += "]"
    saveFile.write("%s" % inventoryData)
    saveFile.write("//")
    roomData = "{"
    for key, room in rooms.items():
        roomData += "%s:[" % key
        for item in room.items:
            roomData += "items[%s]," % item.name
            # saveFile.write("%s," % item.name)
        roomData += "],"
    roomData += "}"
    saveFile.write("%s" % roomData)
    saveFile.close()
    print("Game saved")


def loadGame(player):
    loadFile = open("saves/%s.txt" % player, "r")
    startingRoom = loadFile.read().split("//")[0]
    inventoryData = loadFile.read().split("//")[1].split(",")
    # lines = loadFile.read().split(',')
    roomData = loadFile.read().split("//")[2].split(",")
    loadFile.close()
    # startingRoom = playerStatus[0]
    return startingRoom


newGame = input("Newgame or Loadgame (n/l): ").lower()
if newGame == "n" or newGame == "new" or newGame == "new game":
    playerName = input("Enter your player name: ")
    player = Player(playerName, rooms[startingRoom], [items['book']])
elif newGame == "l" or newGame == "load" or newGame == "load game":
    playerName = input("Enter the character name you want to load: ")
    startingRoom = loadGame(playerName)
    player = Player(playerName, rooms[startingRoom])
    print("Character %s loaded" % playerName)
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

print("\n" + rooms[startingRoom].description)

while(playing is True):
    curRoom = player.room
    command = input("Enter a command: ").strip().lower()
    if command == "q" or command == "quit":
        print("Game Ogre")
        saveGame(player)
        playing = False
        break
    elif command == "help":
        print('Type n/s/e/w to move in a direction.\nType "i" or "inventory" to check your inventory.\nType "look" or "search" to look around for items.\nType "q" or "quit" to quit and save.\nType "save" to save the game without quitting.')
    elif command == "save":
        saveGame(player)
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
    elif command == "i" or command == "inventory":
        print("You check your inventory.")
        for i in player.inventory:
            print("You have %s." % i.description)
    else:
        print("You entered an invalid command.")
        print('Type n/s/e/w to move in a direction.\nType "i" or "inventory" to check your inventory.\nType "look" or "search" to look around for items.\nType "q" or "quit" to quit and save.\nType "save" to save the game without quitting.')
