from room import Room
from player import Player
from item import Item


class AdventureDone(Exception):
    pass

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'outside', [Item("Fish", "Test"), Item("death", "test")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'foyer'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'overlook'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'treasure'),
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

#
# Main
#
playerName = input("Please input a name:")

# Make a new player object that is currently in the 'outside' room.
currentPlayer = Player(playerName, room['outside'])

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


def ItemEval(item):
    return next((y for y in currentPlayer.room.items if y.name.lower() == item), None)


def TextEval(text):
    print(text)
    if text == "q" or text == "quit":
        raise AdventureDone
    elif text == "n" or text == "north":
        if hasattr(currentPlayer.room, 'n_to'):
            currentPlayer.room = currentPlayer.room.n_to
            return False
        else:
            print("Invalid Direction")
            return True
    elif text == "w" or text == "west":
        if hasattr(currentPlayer.room, 'w_to'):
            currentPlayer.room = currentPlayer.room.w_to
            return False
        else:
            print("Invalid Direction")
            return True
    elif text == "e" or text == "east":
        if hasattr(currentPlayer.room, 'e_to'):
            currentPlayer.room = currentPlayer.room.e_to
            return False
        else:
            print("Invalid Direction")
            return True
    elif text == "s" or text == "south":
        if hasattr(currentPlayer.room, 's_to'):
            currentPlayer.room = currentPlayer.room.s_to
            return False
        else:
            print("Invalid Direction")
            return True
    elif "grab" in text:
        splitCommand = text.split()
        itemObj = ItemEval(splitCommand[1])
        if itemObj is not None:
            currentPlayer.items.append(itemObj)
            currentPlayer.room.items.remove(itemObj)
            print(f'You have grabbed {itemObj.name}')
            return False
        print('That object can not be grabbed')
        return True
    else:
        print("Invalid Direction")
        return True


print(f"Welcome {currentPlayer.name}, pick a direction or use q to quit")

try:
    while True:
        awaitValidDirection = True
        print("\n")
        print(
            f"{currentPlayer.name} is located in {currentPlayer.room.name}")
        print(currentPlayer.room.description)

        if len(currentPlayer.room.items) > 0:
            itemSTR = "Looking around you see the items:"
            for item in currentPlayer.room.items:
                itemSTR = itemSTR+" " + item.name
            print(itemSTR)

        while awaitValidDirection:
            playerInput = input("Please select a direction:")
            awaitValidDirection = TextEval(playerInput.lower())

except AdventureDone:
    print('See you next adventure')
