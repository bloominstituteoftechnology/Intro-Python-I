from room import Room
from player import Player
from item import Item
# Declare all the rooms



weapons = {
    'outside':  Item([
        {
            "Sword": "Strongest steal alloy, killer blade"
        },
        {
            "Machete": "Regular blade, killer knife"
        },
        {
            "Rock": "Regular blade, killer knife"
        }
    ], [
        {
            "Fire": "Strongest steal alloy, killer blade"
        },
        {
            "Spear": "Regular blade, killer knife"
        },
        {
            "Pen": "Regular blade, killer knife"
        }
    ]),

    'foyer':    Item([
        {
            "Paper": "Strongest steal alloy, killer blade"
        },
        {
            "Fork": "Regular blade, killer knife"
        }
    ], [
        {
            "Spoon": "Strongest steal alloy, killer blade"
        },
        {
            "Plate": "Regular blade, killer knife"
        }
    ]),

    'overlook': Item([
        {
            "Electric gun": "Strongest steal alloy, killer blade"
        },
        {
            "Book": "Regular blade, killer knife"
        }
    ], [
        {
            "Pizza": "Strongest steal alloy, killer blade"
        },
        {
            "Burger": "Regular blade, killer knife"
        }
    ]),

    'narrow':   Item([
        {
            "Calculator": "Strongest steal alloy, killer blade"
        },
        {
            "Cell Phone": "Regular blade, killer knife"
        }
    ], [
        {
            "Bag": "Strongest steal alloy, killer blade"
        },
        {
            "Purse": "Regular blade, killer knife"
        }
    ]),

    'treasure': Item([
        {
            "Poison": "Strongest steal alloy, killer blade"
        },
        {
            "Spray": "Regular blade, killer knife"
        }
    ], [
        {
            "A/C": "Strongest steal alloy, killer blade"
        },
        {
            "D/C": "Regular blade, killer knife"
        }
    ]),
}


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", weapons['outside'], weapons['outside']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", weapons['foyer'], weapons['foyer']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", weapons['overlook'], weapons['overlook']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", weapons['narrow'], weapons['narrow']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", weapons['treasure'], weapons['treasure']),
}
# Link rooms together
# room['outside'].append = weapons['outside']
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
new_player = Player('outside')
# Write a loop that:
#
# * Prints the current room name
for key, value in room.iteritems():
    # print(value, key)
    if key == new_player.room_location:
        print "\n"
        print 'Current Room: ', value.room_name
        print 'Description: ', value.room_story
        print "\n"
        for each in value.name_item.name_item:
            for key,value in each.iteritems():
                print "     Weapon choice:", key
                print "         Weapon description:", value
        print "\n"
   
direction_input = 'hey'
def starter(direction_input):
        print(" Please enter directions: 'e' east, 'w' west, 'n' north,' s' south ")
    # print(" Want to change weapon inventory? Enter 'weapon' ")
        print(" Type 'get' + 'item name' or 'take' + 'item name' to add to inventory")
        print(" To quit, enter 'q' ")
        if direction_input.split()[0] == 'i' or direction_input.split()[0] == 'inventory':
            direction_input = raw_input(
        "enter choice:")
        else:

            # print(direction_input.split()[0] == 'i')
            print "Type 'i' or 'inventory' to get current Player INVENTORY", direction_input.split()[0],direction_input.split()[0]
            direction_input = raw_input(
        "enter choice:")
        if direction_input == 'n' or dir == 's' or direction_input == 'e' or direction_input == 'w':
            direction_input = str(direction_input) + '_to'
        else:
            direction_input = direction_input
        return direction_input
while direction_input != 'q':
    tmp = 'default'
    clear = "\n" * 100
    # def starter(hey):
    print(" Please enter directions: 'e' east, 'w' west, 'n' north,' s' south ")
    # print(" Want to change weapon inventory? Enter 'weapon' ")
    print(" Type 'get' + 'item name' or 'take' + 'item name' to add to inventory")
    print "Type 'i' or 'inventory' to get current Player INVENTORY"
    print(" To quit, enter 'q' ")
    direction_input = raw_input(
        "enter choice:")

    if direction_input == "q":
        exit(1)
 
    out_ind = 0
    ind = 0
    #HANDLES 'get' or 'take'
    if len(direction_input.split(' ')) == 2 and (direction_input.split()[0] == 'get' or direction_input.split()[0] == 'take'):
        cmd = direction_input.split()[0]
        itm = direction_input.split()[1]
        for key, value in room.iteritems():
            if key == new_player.room_location:
                
                check = False
                for each in value.name_item.name_item:
                    for key,value in each.iteritems():
                        if key == itm:
                            new_player.weapon_inventory = new_player.weapon_inventory + [{key: value}]
                            room[new_player.room_location].name_item.name_item.pop(ind)
                            
                            print(clear)
                            check = True
                            
                            print("These weapons are in your inventory:")
                            i = 0
                            for each in new_player.weapon_inventory:
                                print "Weapon: ", each, " weapon number: ", i
                                i += 1
        # print("Choose your weapon to use: ")
                            choose_weapon = input("Weapon choice: ")
                            new_player.weapon_choice = new_player.weapon_inventory[choose_weapon]
                            print(clear)
                            direction_input = starter(direction_input)
                            
                        ind += 1
                if check == False:
                    print(clear) 
                    print "The ITEM ", itm, "is NOT AVAILABLE for this ROOM"
            out_ind += 1
    
                            
    #Handles 'drop'
    elif len(direction_input.split(' ')) == 2 and (direction_input.split()[0] == 'drop' ):
        cmd = direction_input.split()[0]
        itm = direction_input.split()[1]
        print "Drop, itm", itm
        for each in new_player.weapon_inventory:
            for key, value in each.iteritems():
                if key == itm:
                    
                    leet = new_player.weapon_inventory.pop(i - 1)
                    room[new_player.room_location].name_item.name_item.append(leet)

            direction_input = starter(direction_input)
           
            i += 1
      
    elif len(direction_input.split(' ')) == 2 and (direction_input.split()[0] != 'get' or direction_input.split()[0] != 'take'):
        print(clear)
        print "Command ", direction_input.split()[0], " is INVALID"
        print "\n"
    
        if direction_input == "q":
            exit(1)
    else:
        if direction_input == 'n' or dir == 's' or direction_input == 'e' or direction_input == 'w':
            direction_input = str(direction_input) + '_to'
        else:
            direction_input = direction_input
        

    if (direction_input.split()[0] == 'i' or direction_input.split()[0] == 'inventory' ):
        i = 0
        for key, value in room.iteritems():
            if key == new_player.room_location:
                print clear
                for key, value in room.iteritems():
                    if key == new_player.room_location:
                        print 'Current Room: ', value.room_name
                        print 'Description: ', value.room_story
                        print "\n"
                        print("     Weapon Choices For This ROOM:")
                        print "\n"
                        for each in value.name_item.name_item:
                            for key,value in each.iteritems():
                                print "     Weapon name:", key
                                print "     DESCRIPTION:", value
                                # print "\n"
                        print "\n"
                        print "\n"
        print('Current Player Inventory:')
        for each in new_player.weapon_inventory:
            print "Weapon: ", each, " weapon number: ", i
            i += 1
        print "\n"
        if i == 0:
            print("No WEAPONS in INVENTORY")
            print "\n"
        # exit(1)
        direction_input = starter(direction_input)
    new_direction = "start"
    if direction_input == "n_to":
        try:
            tmp = new_player.weapon_choice
            tmp_inv = new_player.weapon_inventory
            new_direction = room[(new_player.room_location)].n_to
        except AttributeError, message:
            new_direction = "fail"
            print "FAIL FAIL:", message
            # exit(1)
        # break
    elif direction_input == "s_to":
        try:
            tmp = new_player.weapon_choice
            tmp_inv = new_player.weapon_inventory
            new_direction = room[(new_player.room_location)].s_to
            
        except AttributeError, message:
            new_direction = "fail"
            print "FAIL FAIL:", message
            # exit(1)
        # break
    elif direction_input == "e_to":
        try:
            tmp = new_player.weapon_choice
            tmp_inv = new_player.weapon_inventory
            new_direction = room[(new_player.room_location)].e_to
            
        except AttributeError, message:
            new_direction = "fail"
            print "FAIL FAIL:", message
            # exit(1)
        # break
    else:
        try:
            tmp = new_player.weapon_choice
            tmp_inv = new_player.weapon_inventory
            if direction_input == "w_to":
                new_direction = room[(new_player.room_location)].w_to
            else:
               new_direction = room[(new_player.room_location)].direction_input 
            
        except AttributeError, message:
            new_direction = "fail"
            print "FAIL FAIL:", message
            # exit(1)
    # print(new_direction.room_name)
    if new_direction == "fail":
        tstr = direction_input.split()
        if len(tstr) == 2:
            print "\n   Entry option:", tstr[0], ' with and or argument:', tstr[1] ,"IS INVALID \n"
        else:
            print "\n   Entry option:", tstr[0], "IS INVALID \n"
        
        if tmp != None:
                new_player.weapon_choice = tmp
                new_player.weapon_inventory = tmp_inv
        # direction_input = starter()
        for key, value in room.iteritems():
    # print(value, key)
            if key == new_player.room_location:
                
                print 'Current Room: ', value.room_name
                print 'Description: ', value.room_story
                print "\n"
                print("     Weapon Choices For This ROOM:")
                print "\n"
                for each in value.name_item.name_item:
                    for key,value in each.iteritems():
                        print "     Weapon choice:", key
                        print "         Weapon description:", value
                        print "\n"
    else:
        for key, value in room.iteritems():
            if value.room_name == new_direction.room_name:
                # print "new room", key
                # exit(1)
                new_player = Player(key)
            if tmp != None:
                new_player.weapon_choice = tmp
                new_player.weapon_inventory = tmp_inv
            if key == new_player.room_location:
                print clear
                for key, value in room.iteritems():
                    if key == new_player.room_location:
                        print 'Current Room: ', value.room_name
                        print 'Description: ', value.room_story
                        print "\n"
                        print("     Weapon Choices For This ROOM:")
                        print "\n"
                        for each in value.name_item.name_item:
                            for key,value in each.iteritems():
                                print "     Weapon name:", key
                                print "     DESCRIPTION:", value
                                # print "\n"
                        print "\n"
                        print "\n"
               

# exec("%s = %d" % (direction_input,2))
# print(type(s_to) )
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
