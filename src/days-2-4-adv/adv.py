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
                     "North of you, the cave mount beckons",
                     [
                        items['crate'],
                        items['torch']
                     ]),

    'foyer':    Room("Foyer", 
                    """Dim light filters in from the south. Dusty passages run north and east.""", 
                    []),                    

    'overlook': Room("Grand Overlook", 
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                    [
                        items['sword']
                    ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
        user_1 = Player(create_name, room['outside'], [])
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

while True:
    print(f"\nCurrently in: {user_1.room.name}\n")
    print(f"\n{user_1.room.description} \n")        

    # Print error message for invalid input
    invalid_input = "\n=== Your character looks confused. He cannot move there, please select another direction===\n"

    direction = input("\nPick a direction: n, e, s, w (north, east, south, west) : Press q to GIVE UP \n")

    if len(direction) == 1:
        # travel_to_room() --!--> error()


        if (direction[0]) == "q":
            break     

        elif (direction[0]) == "n":
            # user_1.travel_to_room(direction[0])
            if hasattr(user_1.room, 'n_to'):
                user_1.room = user_1.room.n_to                

                if user_1.room.name == 'Treasure Chamber':
                    print("\n=== Your character, in utter disbelief of finding all the treasure taken, kills himself due to severe sadness===\n")
                    break

            else:
                print(f"{user_1.name} looks at the direction you commanded the adventurer with a look of suspicion... {user_1.name} tells you: I cannot move that way sire!")
        
        elif (direction[0]) == "e":
            if hasattr(user_1.room, 'e_to'):
                user_1.room = user_1.room.e_to

            else:
                print(f"{user_1.name} looks at the direction you commanded the adventurer with a look of suspicion... {user_1.name} tells you: I cannot move that way sire!")

        elif (direction[0]) == "s":
            if hasattr(user_1.room, 's_to'):
                user_1.room = user_1.room.s_to

            else:
                print(f"{user_1.name} looks at the direction you commanded the adventurer with a look of suspicion... {user_1.name} tells you: I cannot move that way sire!")

        elif (direction[0]) == "w":
            if hasattr(user_1.room, 'w_to'):
                user_1.room = user_1.room.w_to

            else:
                print(f"{user_1.name} looks at the direction you commanded the adventurer with a look of suspicion... {user_1.name} tells you: I cannot move that way sire!")       
        
        elif (direction[0]) == "i":
            print("Inventory: \n")

            if len(user_1.inventory) == 0:
                print("Empty.")
            else:
                for item in user_1.inventory:
                    print(f"{item.name}: {item.description}")

            
    else:
        print("\n===Please enter: n, e, s, w (north, east, south, west)===\n")


# # print(f"\n{user_1.room.items_in_room.name}\n")
# # for i in user_1.room.items_in_room:
# #     print(f"{user_1.room.items_in_room[i].name}")  

# # print(f"\n=== {user_1.starting_item.name} {user_1.starting_item.description} ===\n")
    


