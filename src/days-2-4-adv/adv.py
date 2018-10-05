from room import Room
from player import Player
from item import Item
import os


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


items = {
    'backpack': Item('backpack', " that is empty", 10),
    'lumiere': Item('lumiere', " lighting the room", 20),
    'parachute': Item('parachute', " but you don't use it", 30),
    'dust': Item('dust', " but what can you do..", 40),
    'chest': Item('chest', " ..that's also empty", 50),

}





items['backpack'].n_to = items['lumiere']
items['lumiere'].s_to = items['backpack']
items['lumiere'].n_to = items['parachute']
items['lumiere'].e_to = items['dust']
items['parachute'].s_to = items['lumiere']
items['dust'].w_to = items['lumiere']
items['dust'].n_to = items['chest']
items['chest'].s_to = items['dust']



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

# p = Player(input("What is your name? "))

choice_dictionary = {"n": "North", "s": "South", "e": "East", "w": "West", "u": "Up", "d": "Down"}

# Make a new player object that is currently in the 'outside' room.

playername = input("Enter Your Name: ")
currentItem = items["backpack"]


p = Player(playername, room["outside"], currentItem, 0)

# clearTerminal = os.system("clear")

inventory = ["pennies", "nickels", "dimes"]
player_inventory = inventory
player_score = 0
currentPoints = currentItem.points


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

def current(location):
    for key in room:
        if key == location:
            print("Current Location: " + room[key].name)
            print(room[key].description)


    
    

while True:
    RED = '\033[31m'
    BLACK = '\033[0;30m'
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    currentPlayer = p.name
    currentLocation = p.location
    currentItem = p.item
    itemDescription = currentItem.description
    currentPoints = currentItem.points
    # inventory = []
    new_list = []
    
    # player_score = p.score
    print(f"" + RED + "\nYou are currently in the great " + p.location.name + "\n\n" + p.location.description + "\n\nYou find " + p.item.name + currentItem.description + BLACK)

    # if inventory:
    #     for each in inventory:
    #         print(inventory[each])
    # else:
    #     print(" ")
            

    if hasattr(p.location, "S_to"):
        print("\n\n    'S' to" + str(p.location.s_to))
        if hasattr(p.location, "e_to"):
            print("    'E' to" + str(p.location.e_to))
            if hasattr(p.location, "n_to"):
                print("    'N' to" + str(p.location.n_to))
                if hasattr(p.location, "w_to"):
                    print("    'W' to" + str(p.location.w_to))
    elif hasattr(p.location, "w_to"):
        print("\n\n    'W' to" + str(p.location.w_to))
        if hasattr(p.location, "n_to"):
            print("    'N' to" + str(p.location.n_to))
            if hasattr(p.location, "e_to"):
                print("    'E' to" + str(p.location.e_to))
                if hasattr(p.location, "s_to"):
                    print("    'S' to" + str(p.location.s_to))
    elif hasattr(p.location, "e_to"):
        print("\n\n    'E' to" + str(p.location.e_to))
        if hasattr(p.location, "s_to"):
            print("    'S' to" + str(p.location.s_to))
            if hasattr(p.location, "w_to"):
                print("    'W' to" + str(p.location.w_to))
                if hasattr(p.location, "n_to"):
                    print("    'N' to" + str(p.location.n_to))
    elif hasattr(p.location, "n_to"):
        print("\n\n    'N' to" + str(p.location.n_to))
        if hasattr(p.location, "e_to"):
            print("    'E' to" + str(p.location.e_to))
            if hasattr(p.location, "s_to"):
                print("    'S' to" + str(p.location.s_to))
                if hasattr(p.location, "w_to"):
                    print("    'W' to" + str(p.location.w_to))
    else:
        if hasattr(p.location, "S_to"):
            print("\n\n    'S' to" + str(p.location.s_to))
            if hasattr(p.location, "e_to"):
                print("    'E' to" + str(p.location.e_to))
                if hasattr(p.location, "n_to"):
                    print("    'N' to" + str(p.location.n_to))
                    if hasattr(p.location, "w_to"):
                        print("    'W' to" + str(p.location.w_to))
        elif hasattr(p.location, "w_to"):
            print("\n\n    'W' to" + str(p.location.w_to))
            if hasattr(p.location, "n_to"):
                print("    'N' to" + str(p.location.n_to))
                if hasattr(p.location, "e_to"):
                    print("    'E' to" + str(p.location.e_to))
                    if hasattr(p.location, "s_to"):
                        print("    'S' to" + str(p.location.s_to))
        elif hasattr(p.location, "e_to"):
            print("\n\n    'E' to" + str(p.location.e_to))
            if hasattr(p.location, "s_to"):
                print("    'S' to" + str(p.location.s_to))
                if hasattr(p.location, "w_to"):
                    print("    'W' to" + str(p.location.w_to))
                    if hasattr(p.location, "n_to"):
                        print("    'N' to" + str(p.location.n_to))
        elif hasattr(p.location, "n_to"):
            print("\n\n    'N' to" + str(p.location.n_to))
            if hasattr(p.location, "e_to"):
                print("    'E' to" + str(p.location.e_to))
                if hasattr(p.location, "s_to"):
                    print("    'S' to" + str(p.location.s_to))
                    if hasattr(p.location, "w_to"):
                        print("    'W' to" + str(p.location.w_to)) 

    print("\n\n")
    cmd = input("-> ")
    if cmd == "q":
        os.system("clear")
        print(CBLACK)
        break
    elif cmd.upper() == 'N':
        os.system("clear")
        print(currentPlayer + ",")

        # if p.location == room['treasure']:
        #     break

        if hasattr(p.location, 'n_to'):
            p.location = currentLocation.n_to
            p.item = currentItem.n_to
            p.score = currentItem.n_to
            print("n_to", p.score)
            # if hasattr(p.location, 's_to'):
            #     print("\n     Enter "S" to go Souther")
            # else:
            #     return
        else:
            os.system("clear")
            print("\n    You Can't Go Any Farther North, Go Another Direction \n\n")
            if hasattr(p.location, "S_to"):
                print("\n\n    'S' to" + str(p.location.s_to))
                if hasattr(p.location, "e_to"):
                    print("    'E' to" + str(p.location.e_to))
                    if hasattr(p.location, "n_to"):
                        print("    'N' to" + str(p.location.n_to))
                        if hasattr(p.location, "w_to"):
                            print("    'W' to" + str(p.location.w_to))
            elif hasattr(p.location, "w_to"):
                print("\n\n    'W' to" + str(p.location.w_to))
                if hasattr(p.location, "n_to"):
                    print("    'N' to" + str(p.location.n_to))
                    if hasattr(p.location, "e_to"):
                        print("    'E' to" + str(p.location.e_to))
                        if hasattr(p.location, "s_to"):
                            print("    'S' to" + str(p.location.s_to))
            elif hasattr(p.location, "e_to"):
                print("\n\n    'E' to" + str(p.location.e_to))
                if hasattr(p.location, "s_to"):
                    print("    'S' to" + str(p.location.s_to))
                    if hasattr(p.location, "w_to"):
                        print("    'W' to" + str(p.location.w_to))
                        if hasattr(p.location, "n_to"):
                            print("    'N' to" + str(p.location.n_to))
            else:
                print("\n\n    'N' to" + str(p.location.n_to))
                if hasattr(p.location, "e_to"):
                    print("    'E' to" + str(p.location.e_to))
                    if hasattr(p.location, "s_to"):
                        print("    'S' to" + str(p.location.s_to))
                        if hasattr(p.location, "w_to"):
                            print("    'W' to" + str(p.location.w_to)) 
    elif cmd.upper() == 'E':
        print(currentPlayer + ",")
        if hasattr(p.location, 'e_to'):
            p.location = currentLocation.e_to
            p.item = currentItem.e_to
            p.score = currentItem.e_to
            print("e_to", p.score)
        else:
            os.system("clear")
            print("\n    You Can't Go Any Farther East, Go Another Direction \n\n")
    elif cmd.upper() == 'S':
        print(currentPlayer + ",")
        if hasattr(p.location, 's_to'):
            p.location = currentLocation.s_to
            p.item = currentItem.s_to
            p.score = currentItem.s_to
            print("s_to", p.score)
        else:
            os.system("clear")
            print("\n    You Can't Go Any Farther South, Go Another Direction \n\n")
    elif cmd.upper() == 'W':
        print(currentPlayer + ",")
        if hasattr(p.location, 'w_to'):
            p.location = currentLocation.w_to
            p.item = currentItem.w_to
            p.score = currentItem.w_to
            print("w_to", p.score)
        else:
            os.system("clear")
            print("\n    You Can't Go Any Farther West, Go Another Direction \n\n")
            # print(f"\n You are currently in the grand " + p.location.name)
    # elif cmd == "n":
    #     print(f"You are currently " + currentLocation.name)
    #     currentLocation = currentLocation.n_to
    #     print(f"You are currently " + currentLocation.name)
    # elif cmd == "s"
    # elif cmd == "e"
    # elif cmd == "w"
    # elif cmd == "u"
    # elif cmd == "d"
    # elif p.location == room['treasure']:
    #     pass
    else:
        sentence = cmd
        split = sentence.split()
        length = len(split)
        # if cmd == "inventory":
        #     for each in inventory:
        #         print(each)

        if " " in cmd:
            itemCMD = split[0]
            if itemCMD == "get":
                thingName = currentItem.name
                thingInput = split[1]
                if thingInput == "items":
                    print("\n\nBe more specific....")
                    print("\n..but you see " + thingName + " in the room..")
                elif thingInput in player_inventory:
                    print("But you already have it")
                elif not thingInput == thingName:
                    print("\n\nCan't get that..")
                else:
                    # item_name = currentItem.name
                    player_inventory.append(thingInput)
                    player_score += currentItem.points
                    print("\n\nItem Secured!")
                    print(f"\nYou got a new item, you now have " + inventory[(len(inventory) - 1)] + "\n\nInventory:")
                    thingName = "nothing"
                    for item in player_inventory:
                        print(item)

                    print("" + GREEN + "\n\nYour score is now " + str(player_score) + BLACK) 
                    
            elif itemCMD == "take":
                thingName = currentItem.name
                thingInput = split[1]
                if thingInput == "items":
                    print("\n\n....be more specific")
                    print("\n..but you see " + thingName + " in the room..")
                elif thingInput in player_inventory:
                    print("\n\nCan't take what you already have..")
                elif not thingInput == thingName:
                    print("That's not in here")
                else:
                    item_name = currentItem.name
                    player_inventory.append(item_name)
                    player_score += currentItem.points
                    print("Item Taken!")
                    print(f"\nYou took a new item, you now have " + inventory[(len(inventory) - 1)] + "\n\nInventory:")
                    thingName = "nothing"
                    for item in player_inventory:
                        print(item)

                    print("" + GREEN + "\n\nYour score is now " + str(player_score) + BLACK)

            elif itemCMD == "drop":
                if split[1] == "item":
                    print("\n\n....be more specific")
                if split[1] == "all":
                    alert = input("Are you sure?: ")
                    if alert == "yes":
                        player_inventory = []
                        print("\nInventory destroyed, maybe you can find some more things")
                    else:
                        print("Change of heart!")
                elif split[1] in player_inventory:
                    to_drop = split[1]
                    player_inventory.remove(to_drop)
                    player_score -= currentItem.points
                    print("\n\nItem Dropped!")
                    print(f"You left " + to_drop + " behind.." + "\n\nInventory:")
                    for item in player_inventory:
                        print(item)

                    print("" + GREEN + "\n\nYour score is now " + str(player_score) + BLACK)    
                else:
                    print("..but you don't have that to drop..")

            elif itemCMD == "print":
                print("Inventory:\n")
                print(player_inventory)
                print("Score:" + str(player_score))
                                        
                    #         print(len(inventory))
                        # print(inventory[0])
                        # print(inventory[1])
                    # else:
                    #     print("Please Refrase Request")
                # for word in split:
                #     if word == 
        else:
            print("Not Allowed")

    
    

