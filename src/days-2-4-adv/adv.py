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

    direction = input("\nPick a direction: [n],[e],[s],[w]\n").strip().lower().split()

    # --> Check improper commands
    if len(direction) > 2 or len(direction) < 1:
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
        
        elif direction[0] not in ['n', 'north', 'e', 'east', 's', 'south', 'w', 'west']:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nYour character does not understand that command\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    


