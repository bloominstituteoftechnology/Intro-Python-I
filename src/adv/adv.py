from room import Room
from room import DarkRoom
from player import Player
from item import Item
from item import Treasure
from item import LightSource
import os

# Declare all the rooms

room = {
    'outside':  Room("outside the Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   DarkRoom("in the Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'torch': LightSource("Blazing Torch", "How is this still on fire?"),
    'treasure': Treasure("Hidden Treasure", "Looks like the previous adventurers missed this!", 100),
    'rock': Item("Blunt Rock", "It's not very sharp..."),
    'sword': Item("Iron Sword", "More sharp than a rock!"),
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

# Place items

room['treasure'].items.append(item['treasure'])
room['outside'].items.append(item['rock'])
room['foyer'].items.append(item['sword'])
room['overlook'].items.append(item['torch'])


def singleChoice(noun):
    if noun == "score":
        print("Your current score is: {}".format(player.score))
        return 1

    if (noun == "north") or (noun == "n"):
        if isinstance(player.room.n_to, DarkRoom):
            if player.hasLightSource() or player.room.n_to.hasLightSource():
                player.room = player.room.n_to
                return 1
            else:
                print("This room looks to be too dark to enter...")
        elif isinstance(player.room.n_to, Room):
            player.room = player.room.n_to
            return 1

    if (noun == "south") or (noun == "s"):
        if isinstance(player.room.s_to, DarkRoom):
            if player.hasLightSource() or player.room.s_to.hasLightSource():
                player.room = player.room.s_to
                return 1
            else:
                print("This room looks to be too dark to enter...")
        elif isinstance(player.room.s_to, Room):
            player.room = player.room.s_to
            return 1

    if (noun == "east") or (noun == "e"):
        if isinstance(player.room.e_to, DarkRoom):
            print(player.hasLightSource())
            if player.hasLightSource() or player.room.e_to.hasLightSource():
                player.room = player.room.e_to
                return 1
            else:
                print("This room looks to be too dark to enter...")
        elif isinstance(player.room.e_to, Room):
            player.room = player.room.e_to
            return 1

    if (noun == "west") or (noun == "w"):
        if isinstance(player.room.w_to, DarkRoom):
            if player.hasLightSource() or player.room.w_to.hasLightSource():
                player.room = player.room.w_to
                return 1
            else:
                print("This room looks to be too dark to enter...")
        elif isinstance(player.room.w_to, Room):
            player.room = player.room.w_to
            return 1

    if (noun == 'i') or (noun == 'inventory'):
        if len(player.items) > 0:
            print("You're currently holding: ")
            for item in player.items:
                print(item)
        else:
            print("You aren't holding anything.")
        return 1

    if noun == "look":
        if len(player.room.items) == 1:
            print(f"There's only a {player.room.items[0]}.")
        if len(player.room.items) > 1:
            print("There appear to be a few items:")
            for item in player.room.items:
                print(item)
        if len(player.room.items) < 1:
            print("You don't see anything.")
        return 1

    if noun == "q":
        return 2
    return 0


def doubleChoice(verb, noun, item):
    if (verb == "get") or (verb == "take") or (verb == "pickup"):
        print(player.room.pickup(player, item[noun]))
        return 1
    if (verb == "go") or (verb == "proceed"):
        return singleChoice(noun)
    if verb == "look":
        return singleChoice(verb)
    if (verb == 'drop') or (verb == 'leave'):
        print(player.room.drop(player, item[noun]))
        return 1
    if (verb == 'inspect') or (verb == 'analyze'):
        print(item[noun].inspect())
        return 1
    return 0


#
# Main
#

player = Player(room['outside'])

os.system("cls")
while True:
    flag = 0
    print(player.room)
    choice = input("What do you do? ")
    choice = choice.split(' ')
    os.system("cls")
    if len(choice) == 1:
        flag = singleChoice(choice[0])
    if len(choice) == 2:
        flag = doubleChoice(choice[0], choice[1], item)
    if flag == 0:
        print("You can't do that.")
    if flag == 2:
        break
    print("\n")
