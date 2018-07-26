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
player = Player("Jacob", room['outside'],[],6);
# Write a loop that:
#
# setting my flag for the coditon of my while loop
playing = True;
# as long as this is true keep looping
while(playing):
    #width = os.get_terminal_size() 
    # setting a variable for my borders and one for my error messages
    borderTop = "╔"+ ("═" * 70) + "╗"
    borderBtm = "╚"+ ("═" * 70) + "╝"
    caret = "^" *72

# * Prints the current room name
    # setting the players current room into a variable
    curRoom = player.current
    # setting up a text wrap for the description
    prettyDescription = textwrap.fill(curRoom.description)
    #prettyDescription = prettyDescription.center(40,"
    #  ")
    # setting up a varible to hold and empty string
    items = ""
    # iterate through the items in my room and add them to the items string
    for item in curRoom.items:
        items +=  item + ", "
    # when the current room no longer has  any items have "Empty" displayed
    if len(curRoom.items) ==0:
        items = "Empty"
    # set up emptry string name it bag
    bag = ""
    # iterate through the players inventory and create a string of all items
    for item in player.inventory:
            bag += item +", " 
    # when the players bag has no items display "Empty"       
    if len(player.inventory) == 0:
      bag += "Empty"
      # when the player bag is equal to the bag size then it is full.
      # display "Your bag is full: " followed by the items in your inventory
    elif len(player.inventory)==player.bagSize:
      tempBag = bag
      bag ="Your bag is Full: \n" + tempBag
    #  this will print out the main part of the information being displayed
    #  such starting with the room name then the top border,
    #   then the description followed by the rooms items.
    #   after that the players inventory and the bottom border will be displayed
    print('\n\t\tYou are in the {}.\n{}\n\n{}\n\nLoot:\n{}\n\nBag:\n{}\n\n{}\n'.format(curRoom.name, borderTop, prettyDescription,items,bag,borderBtm))
    # ask the player if they would like to take or drop an item and take.
    # store the input into the loot varible, strip off white space and set to lower case.
    loot =  input("would you like to take or drop an item?\n(yes/no) ").strip().lower()
    # if the user enters in a "yes" or a "y", then ask them what they would like to do
    if loot == "yes" or loot =="y":
        # strip, lower and store the user input into a choice variable.
        choice =input("Would you like to get or drop an item? \nPick: ").strip().lower()
        # slice the action out of the input by starting at the 0 index,
        # and going to the where the space is in the choice string.
        action = choice[0:choice.index(" ")]
        # slice the item out of the choice string, since strings are arrays,
        # this works, just grab start the slice at the index of the space,
        # then add 1 on it so it starts at the first letter then just got to the end of the string
        item = choice[choice.index(" ") +1:len(choice)]
        print("you want to {} a {}".format(action,item))
        # when the action matches "get", "gake" or "grab" then allow this block to execute
        if action == "get" or action == "take" or action == "grab" :
          
            print("what would you like to loot:\n{}".format
            (curRoom.items))
            #removed = curRoom.items.pop(curRoom.items.index(input("pick:").strip().lower()))
        
            # iterate through the items in the current room and if it is not in there,
            # print that it is not inside ot the room.
            if item not in curRoom.items:
                print("\n\n\t  Error: {} is not loot available this room\n{}".format(item,caret))
            #  if it is inside of the room and the players bags are not full, then allow the player to remove items from the room
            # and place them into the players inventory.
            elif len(player.inventory) < player.bagSize:
                removed = curRoom.items.pop(curRoom.items.index(item))

                #removed = curRoom.items.remove(grab)
                print("You added {} to your bag".format(removed))
                player.inventory.append(removed)
            # if the  players inventory exceeds the value of  the players bag size,
            # then send an error showing the player that the bag is full.   
            elif len(player.inventory) >= player.bagSize:
          
                print("\n\n\t\t\tError: My bag is full!\n{}".format(caret))
        # if it is not one of the actions to remove an item form the room,
        # check to see if it is one of the actions to drop an item in the room.
        # if so then remove the item from the players inventory, and add it to the current room.
        elif action == "drop" or action == "leave" or action =="remove" or action =="place":
             place = player.inventory.pop(player.inventory.index(item))

             #removed = curRoom.items.remove(grab)
             print("You dropped {} inside of {}".format(place,curRoom.name))
             curRoom.items.append(place)
        # if the action is not matching the actions above then print out an error.    
        else:
            print("\n\n\t  Error: {} is not a valid action, try (get/drop)\n{}.".format(action,caret))         
    # if the input matches  "q","quit","exit" or "stop" then set the flag to false stopping the code
    elif loot =='q' or loot == 'quit' or loot =='exit' or loot == 'stop':
             playing = False 
    # if the player selects no then give them directions to pick from,
    # and move the room in that direction        
    elif loot == "no" or loot =="n": 
        command = input("Enter a direction:\n N, S, W, E,").strip().lower()
        # if the player entered in one of the commands that stops the game, then do so
        if command =='q' or command =='quit' or command == 'exit':
            playing = False
        # if the command is in this list than excute the code block
        elif command in ["s","n","e","w"]:
            # set the direction attribute to  the command plus the string "_to" allowing dirAttr to equal s_to, n_to ect...
            dirAttr = command + "_to"
        # hasattr thakes two params the object and the string,
        # if this returns ture, set the players current room,
        # as the room returned by getattr
        if hasattr(curRoom,dirAttr):
             player.current = getattr(curRoom,dirAttr)
        # if that path is non existant than, prompt the player.     
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
