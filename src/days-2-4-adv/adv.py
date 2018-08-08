from room import Room
from player import Player
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["mango"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

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

# Make a new player object that is currently in the 'outside' room.
current_room = 'outside'
player = Player(room[current_room], ["mango"])
# Write a loop that:
#

def print_room_info():
    print(player.room.name + ":")
    print(player.room.description)
    print("Items found in the room: ")
    if len(player.room.items) == 0:
        print("   none")
    else:
        for i in player.room.items:
            print("\t" + i)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
print("\t\tLet the game begin:\n")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

while True:
    moved = False

    print("Current Player Room:")
    print("     " + player.room.name)

    wrapper = textwrap.TextWrapper(width=50)
    description_list = wrapper.wrap(text=player.room.description)

    print("Description: ")
    for desc in description_list:
        print("     " + desc)

    print("\n")

    user_input = input("Please enter....\n\t" +
                       "n,s,e,w to move OR \n\t" +
                       "g [item] to get item OR \n\t" +
                       "d [item] to drop item OR \n\t" +
                       "i to view inventory \n\t" +
                       "q to quit the game \n\n\t" +
                       "Enter: ")

    if user_input == 'q':
        print("\n")
        break

    print("================================================\n")

    parsed_input = user_input.split()

    if len(parsed_input) > 1:
        action = parsed_input[0]
        item = ""
        for i in range(1, len(parsed_input)):
            item += parsed_input[i] + " "
        item = item.strip()

        if action == "g" or action == "grab":
            if item in player.room.items:
                print("...grabbing " + item + "...")
                player.room.items.remove(item)
                player.items.append(item)
            else:
                print("Items are unavailable in room")

    else:
        direction_to = user_input + "_to"
        for r_name in room.keys():
            if hasattr(room[r_name], direction_to):
                if getattr(room[r_name], direction_to) == room[current_room]:
                    player.room = room[r_name]
                    current_room = r_name
                    moved = True
                    break

        if moved:
            print("Moved to room {}\n".format(current_room))
            print("================================================\n\n")
        else:
            print("Movement is not allowed. Try again...")
            print("================================================\n\n")

