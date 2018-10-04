from room import Room
from player import Player




# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
    "Jar of Fairies"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
"Magic Roomba"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
"A golden septor"),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",),
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
valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
	                "north": "n", "south": "s", "east": "e", "west": "w",
                    "forward": "n", "backward": "s", "right": "e", "left": "w"}

valid_items = {"Jar of Fairies":"Jar of Fairies","Magic Roomba":"Magic Roomba","A golden septor":"A golden septor"}

name = input("\nWhat's your name?:")
player = Player(name , room['outside'])
print(f"\n\n{player.currentRoom}")

while True:
    cmds = input("\n-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
           break
        
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
             player.seeInventory()
        else:
         print("\n\nI did not understand that command; Press q to quit")
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
        elif cmds[0] == "get" or cmds[0] == "take":
            if cmds[1] in valid_items:
                player.pickUpItem(valid_items[cmds[1]])
        elif cmds[0] == "drop":
            if cmds[1] in valid_items:
                player.dropItem(valid_items[cmds[1]])
        else:
            print("\n\nI did not understand that command; Press q to quit") 









# Make a new player object that is currently in the 'outside' 
# room.
# name = input("\nWhat's your name?:")
# player = Player(input("\nWhat's your name?:"),room['outside'],[])


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

# while True:
    
       
        

#     print(f'\nRoom: {player.currentRoom.name}')
#     print(f'{player.currentRoom.description}')
#     player.currentRoom.printInv()

   

#     suppressRoomPrint = False

#     directions = {"N": "N", "NORTH": "N", "S": "S", "SOUTH": "S",
#      "E": "E", "EAST": "E", "W": "W", "WEST": "W"}

#     cmds = input("\nWhere to now? \n Or will you quit like a chicken? Press Q to QUIT\n").upper().split(" ")
#     if len(cmds) == 1:
#         if cmds[0] in directions:
#                     player.travel(directions[cmds[0]])
#         elif cmds[0] == "LOOK":
#             player.look()
#         elif cmds[0] == "INV":
#             print(f"Here you go!: ")
#             if len(player.items) > 0:
#                 for item in player.items:
#                     print(item.name)
#             else:
#                 print("Nothing in here.")
#         elif cmds[0] == "Q" or cmds[0] == "QUIT":
#             break
#         else:
#             print("Nope try again!")
#             print('\n')
#     else:
#         if cmds[0] == "LOOK":
#             if cmds[1] in directions:
#                 player.look(directions[cmds[1]])
#         elif cmds[0] == "TAKE":
#             for item in player.currentRoom.items:
#                 if cmds[1] in item.name:
#                     item.takeItem(player)
#                     print(f"You have taken {cmds[1]}!\n")
#         elif cmds[0] == "DROP":
#             for item in player.items:
#                 if cmds[1] in item.name:
#                     item.dropItem(player)
#                     print(f"You have dropped {cmds[1]}!\n")
#         else:
#             print("Nope! Try again")

    
    # if answer == "q":
    #     print("Get outta here!!")
    #     break

    # if answer == ""

    # if answer == "n":
    #     if not hasattr(player.currentRoom,'n_to'):
    #         print(error)
    #     else:
    #         player.currentRoom = player.currentRoom.n_to

    
    # if answer == "s":
    #     if not hasattr(player.currentRoom,'s_to'):
    #         print(error)
    #     else:
    #         player.currentRoom = player.currentRoom.s_to

    

    # if answer == "e":
    #     if not hasattr(player.currentRoom,'e_to'):
    #         print(error)
    #     else:
    #         player.currentRoom = player.currentRoom.e_to

    
    # if answer == "w":
    #     if not hasattr(player.currentRoom,'w_to'):
    #         print(error)
    #     else:
    #         player.currentRoom = player.currentRoom.w_to


   


