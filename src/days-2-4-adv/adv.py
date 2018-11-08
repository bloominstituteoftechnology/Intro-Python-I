from room import Room
from player import Player
from item import Item

# Declare all the rooms

items = {
    "rock": Item("rock", "can be used a a weapon and good for building"),
    "sword": Item("sword", "is a weapon and can be used for cutting and slicing things"),
    "coins": Item("coins", "can be used to purchase things"),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items['rock']],),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[items['sword']],),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
[],),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
[items['coins']],),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
[],),
}

# Declare all items



'''rock = Item("Rock", "can be used a a weapon and good for building")
sword = Item("Sword", "is a weapon and can be used for cutting and slicing things")
coins = Item("Coins", "can be used to purchase things")'''

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

'''# Items in rooms
room['outside'].add_item(Rock)
room['narrow'].add_item(Coins)
room['foyer'].add_item(Sword)'''

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
while True:
# * Prints the current room name
    print(player.location.name)

# * Prints the current description (the textwrap module might be useful here).
    print(player.location.description)
    player.location.list_items()

# * Waits for user input and decides what to do.
    userInputs = input("Please enter a command: ").split(' ')

    if 1 <= len(userInputs) <= 2:
        command = userInputs[0]
        target = userInputs[1] if len(userInputs) == 2 else None

    # If the user enters "q", quit the game.
    if command == "q":
        break

# If the user enters a cardinal direction, attempt to move to the room there.
    if command == "n" or command == "s" or command == "e" or command == "w":
        newRoom = player.location.goToRoomInEnteredDirection(command)
       
        # If the movement isn't allowed, print an error message 
        if newRoom == None:
            print("\n ===That direction is not allowed at this time=== \n")
        else:
            # Else move the user to the room specified
            player.change_location(newRoom)

    #if the player enters inventory or i, display players list of items
    if command == 'inventory' or command == 'i':
        if player.items:
            player.inventory()

    if command == 'get' or 'take':
        if not player.location.items:
            print("You have no items to pick up.")
        elif not player.location.find_item(target):
            print("This item is not what you are looking for.")
        else:
            # new_item = target
            new_item = items[target]
            player.location.remove_item(new_item)
            player.get(new_item)

    if command == 'drop':
        if not player.items:
            print('You are not carrying anything with you.')
        elif not player.find_item(target):
            print('This is not one of the items you are carrying')
        else:
            # dropped_item = target
            dropped_item = items[target]
            player.drop(dropped_item)
            player.location.add_item(dropped_item)

    if command == 'score':
        pass #in prep for showing score