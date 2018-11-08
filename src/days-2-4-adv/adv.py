from room import Room
from player import Player
from item import Item
# Declare all the rooms

items = {
    'crate': Item('Wooden Crate', 'Could be something valuable in there. If only there was a way to open it'),
    'torch': Item('Torch', 'A useful light source. Don\'t get it wet!'),
    'sword': Item('Iron Sword', 'How do you like your goblin? Medium rare? Or Dead.')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", 
                    """Dim light filters in from the south. Dusty passages run north and east."""),                    

    'overlook': Room("Grand Overlook", 
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# --> Add items to rooms
room['outside'].items.append(Item('Torch', 'A useful light source. Don\'t get it wet!'))
room['outside'].items.append(Item('Sword', 'Great for killing stuff'))
room['treasure'].items.append(Item('Midas Cup', 'It honestly is just a cup.'))

#
# Main
#

'''
Order to win:

1. Head n to foyer
2. Head e into the narrow
3. Head n to the treasure (break here. User has won)
'''

# Make a new player object that is currently in the 'outside' room.

while True:
    create_name = input("Choose a name adventurer: ")

    if len(create_name) == 0:
        print("\nYour adventurer cannot be name-less!\n")
    else:        
        player = Player(create_name, room['outside'])
        break

# Write a loop that:
# * Prints the current room name --> /
# * Prints the current description (the textwrap module might be useful here). --> /
# * Waits for user input and decides what to do. --> somewhat /
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game. -->

game_finish = False

while not game_finish:
    print("===========================")
    print(f"\nCurrently in: {player.room.name}\n")
    print(f"{player.room.description} \n")   
    print("===========================")

    direction = input("\nPick a direction: [n],[e],[s],[w]\n").strip().lower().split(" ", 1)    
    # --> Check improper commands
    if len(direction) > 3 or len(direction) < 1:
        print("\nYour character does not understand that command\n")
        continue

    # --> Check one word/character command
    if len(direction) == 1:        

        # --> User wants to quit
        if (direction[0]) == "q" or direction[0] == "quit":
            game_finish = True    
        
        # --> User wants to move in any direction        
        elif direction[0] in ['n', 'north', 'e', 'east', 's', 'south', 'w', 'west']:
            # --> If user delivers something like 'north', we just take the first letter of it
                # --> note: Double bracket ==> first one to access letter ==> second one to access first letter only
            player.room = player.try_move(direction[0][0])
        
        elif direction[0] not in ['n', 'north', 'e', 'east', 's', 'south', 'w', 'west', 'i', 'inventory', 'l', 'look']:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nYour character does not understand that command\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        elif (direction[0]) == "i" or direction[0] == "inventory":
            if len(player.inventory) == 0:
                print(f"{player.name} looks into their bag. 2 pieces of dirt lie in there.")
            else:
                for item in player.inventory:
                    print(f"{item.name}")

        elif direction[0] == "l" or direction[0] == "look":
            if len(player.room.items) == 0:
                print(f"{player.name} looks around, and sees no items of use")
            else:
                for item in player.room.items:
                    print("~~~~~~~~~~~~~~~~~~~~LOOKING.....~~~~~~~~~~~~~~~~~~~~")
                    print(f"{player.name} looks around, and sees:")
                    print(f"{item.name}")
        

    # --> Handle item pick up
    elif len(direction) == 2:
        print("direction -->", direction[0], ", ", direction[1])
        
        if direction[0] == "get" or direction[0] == "take":
            if len(player.room.items) > 0:
                item = player.find_item(direction[1])
                print(item)
                if item: 
                    item.on_take(player)                   
                    player.room.items.remove(item)
                    player.inventory.append(item)                        
                    print(f"{player.name} has picked up: {item.name}")
                else:
                    print("Your character does not see that item in this room")

        elif direction[0] == "drop" or direction[0] == "delete":
            item = player.find_in_inventory(direction[1])
            if item:
                item.on_drop(player)
                player.inventory.remove(item)
                player.room.items.append(item)
                print(f"{player.name} has dropped: {item.name}")
            else:
                print("Your character does not have any items to drop")