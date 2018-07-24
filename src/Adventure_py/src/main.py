from os import system
from player import Player
from location import Location
from item import Item, Weapon

# todo Add more rooms.
# todo Add a way to win.
# todo implement door's and keys
# todo Come up with more stretch goals! Scoring? Monsters?

# create items
lantern = Item(name="lantern", description="a gas powered lantern, looks old.", value=23)

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
gold permeates the air.")
loc_five = Location(
    name="Treasure Chamber",
    description="You've found the long-lost treasure chamber."
        "\n\tSadly, it has already been completely emptied by"
        "\n\tearlier adventurers. The only exit is to the south."
)

# add items to locations
sub_room.items[1] = lantern

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


def clear():
    _ = system('clear')


def command():
    print("""
                    Commands:
                        q - quit
                        m - check map
                        h - get a list of commands
                        i - check inventory
                        p - pick up an item
                        d - drop item
                        1 - move north
                        2 - move south
                        3 - move east
                        4 - move west
                        5 - rest
            """)


def main():
    loc = loc_one
    p = Player(input("Enter your characters name \n"))
    print("player created " + str(p.name))
    command()
    print(loc)
    while True:
        p.location = loc
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
            p.pick_up(int(input("index of item: ")), int(input("index of your bag: ")))
        elif x == "d":
            clear()
            p.show_inventory()
            p.drop_item(int(input("which item would you like to drop? ")))
        elif x == "1":
            if p.can_move():
                if loc.north:
                    clear()
                    loc = loc.north
                    print(loc)
                else:
                    print("cant go there.")
        elif x == "2":
            if p.can_move():
                if loc.south:
                    clear()
                    loc = loc.south
                    print(loc)
                else:
                    print("cant go there.")
        elif x == "3":
            if p.can_move():
                if loc.east:
                    clear()
                    loc = loc.east
                    print(loc)
                else:
                    print("cant go there.")
        elif x == "4":
            if p.can_move():
                if loc.west:
                    clear()
                    loc = loc.west
                    print(loc)
                else:
                    print("cant go there.")

        elif x == "5":
            clear()
            p.wait()


main()