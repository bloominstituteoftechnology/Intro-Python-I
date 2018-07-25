import textwrap
import os
from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",["stick","rock","flint","apple"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",["cloak","hat","rock"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",["rock","potion","binoculars"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",["shield","sword","water","candle"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",["gold","wand","bow","beef","grog"]),
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

# Make a new player object that is currently in the 'outside' room.
player = Player("Jacob", room['outside'],[],16);
print(player)

# Write a loop that:
#
playing = True;
while(playing):
    #width = os.get_terminal_size() 
    underline = " <"+ ("-" * 70) + ">"

# * Prints the current room name
    curRoom = player.current
    prettyDescription = textwrap.fill(curRoom.description)
    #prettyDescription = prettyDescription.center(40," ")
    print('\n\t\tYou are in the {}.\n{}\n\n{}\n\nLoot:\n{}\n\nBag:\n{}\n{}\n'.format(curRoom.name, underline, prettyDescription,curRoom.items,player.inventory,underline))
    loot =  input("would you like to take an item?\n(yes/no)").strip().lower()
    if loot == "yes" or loot =="y":
        if len(player.inventory) < 4:
            print("what would you like to loot:\n{}".format
            (curRoom.items))
            removed = curRoom.items.pop(curRoom.items.index(input("pick:").strip().lower()))


            #removed = curRoom.items.remove(grab)
            print("You added {} to your bag".format(removed))
            player.inventory.append(removed)
        elif len(player.inventory) >=player.bagSize:
          
             print("Bag is full!")

    elif loot =='q' or loot == 'quit' or loot =='exit' or loot == 'stop':
             playing = False 
    elif loot == "no" or loot =="n": 
        command = input("Enter a direction:\n N, S, W, E, ").strip().lower()

        if command =='q' or command =='quit' or command == 'exit':
            playing = False

        elif command in ["s","n","e","w"]:
            dirAttr = command + "_to"

        if hasattr(curRoom,dirAttr):
             player.current = getattr(curRoom,dirAttr)
        else:
             print("\n You cannot choose that path.\n")



#     wrappedText = textwrap.TextWrapper(width=40);
#     wordList = wrappedText.wrap(text=jacob.current.description);

# for line in wordList:
#     print(line);


# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
# #
# playerInput = input("What direction will you choose young hero?\n path choices: n, s, e, w,\n the choice is yours decide a path.")
# # If the user enters a cardinal direction, attempt to move to the room there.
# if playerInput = "q":
#     playing = False;

# elif playerInput in ["n","s","w","e"]:
    
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
