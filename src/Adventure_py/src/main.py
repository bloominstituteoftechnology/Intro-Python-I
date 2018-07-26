from os import system
import platform
from player import Player
from location import Location
from item import Item, Weapon
from door import Door
from playsound import playsound

# todo Add a way to win.
# todo implement door's and keys
# todo Come up with more stretch goals! Scoring? Monsters?

# create items
lantern = Item(name="lantern", description="a gas powered lantern, looks old.", value=2)
sword = Weapon(name="Short Sword", description="a single handed sword, it looks like it has seen battle.", dps=25, value=100)
key = Item(name="key", description="a blue key, i wonder if it fits in any of these doors.", value=10)
door = Door(key=key, status=False)

# create locations.
loc_one = Location(name="Outside Cave Entrance", description="North of you, \n\tthe cave mouth beckons")
sub_room = Location(name="a small hole in the face of a rock.", description="You enter the small lit cave to find that someone has been living here recently.")
loc_two = Location(name="Foyer", description="Dim light filters in from the south. \n\tDusty passages run north and east.")
loc_three = Location(
    name="Grand Overlook",
    description="""A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm."""
)
loc_four = Location(name="Narrow Passage", description="The narrow passage bends here from west to north. \n\tThe smell of \
gold permeates the air.", door=door)
loc_five = Location(
    name="Treasure Chamber",
    description="You've found the long-lost treasure chamber."
        "\n\tSadly, it has already been completely emptied by"
        "\n\tearlier adventurers. The only exit is to the south."
)

# add items to locations
sub_room.items[1] = lantern
loc_three.items[1] = sword
loc_three.items[2] = key


# connect locations
loc_one.north = loc_two
loc_one.east = sub_room
sub_room.south = loc_one
loc_two.north = loc_three
loc_two.south = loc_one
loc_two.east = loc_four
loc_three.south = loc_two
loc_four.west = loc_two
loc_four.north = loc_five
loc_five.south = loc_four


# initialize globally scoped variables

loc = p = None


def clear():
    if platform.system() == 'Linux':
        _ = system('clear')
    elif platform.system() == 'Windows':
        _ = system('cls')



def command():
    print("""
                        Commands:
q - quit                m - check map          h - get a list of commands
i - check inventory     p - pick up an item    d - drop item

1 - move north          2 - move south         3 - move east
4 - move west           5 - rest
            """)


def move(directory):
    global loc, p
    if loc.is_valid_room(directory):
        if getattr(loc, directory).door is not None:
            if getattr(loc, directory).door.is_locked:
                print("door is locked, would you like to try and unlock it?")
                if input("y - yes\nn - no\n") == "y":
                    clear()
                    p.show_inventory()
                    getattr(loc, directory).door.unlock(p.inventory[int(input("which slot is your key in? "))])
            else:
                if p.can_move():
                    clear()
                    loc = getattr(loc, directory)
                    print(loc)
        else:
            if p.can_move():
                clear()
                loc = getattr(loc, directory)
                print(loc)
    else:
        print("cant go there.")


def main():
    global loc, p
    loc = loc_one
    p = Player(input("Enter your characters name \n"))
    clear()
    print("player created " + str(p.name))
    command()
    print(loc)
    while True:
        p.location = loc
        if p.location == loc_five:
            input("press enter to coninue.")
            clear()
            playsound('./Assets/1.mp3')
            print("\n\t\tyou left the dungeon depressed and broke, Congratulations!.\nPlayer Stats \n" + str(p) + "\nInventory: " + str(p.inventory) + "\n")
            break
        x = input("enter your command: ")
        if x == "q":
            break
        elif x == "m":
            clear()
            p.check_map()
        elif x == "h":
            clear()
            command()
        elif x == "i":
            clear()
            p.show_inventory()
        elif x == "p":
            clear()
            p.pick_up(int(input(str(loc.items) + "\nindex of item: ")),
                      int(input(str(p.inventory) + "\nindex of your bag: ")))
        elif x == "d":
            clear()
            p.show_inventory()
            p.drop_item(int(input("which item would you like to drop? ")))
        elif x == "1":
            move("north")
        elif x == "2":
            move("south")
        elif x == "3":
            move("east")
        elif x == "4":
            move("west")
        elif x == "5":
            clear()
            p.wait()
        else:
            clear()
            print("Unrecogonized Command.  Enter 'h' to see a list of commands")


main()
