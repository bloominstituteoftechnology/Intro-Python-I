# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room, inventory=None, equipment=None):
        # initialize a player with room information, inventory, equipment, and coins
        self.room = room
        self.inventory = [] if inventory is None else inventory
        self.equipment = [] if equipment is None else equipment
        self.coin = 0
        self.score = 0

    def move(self, room, direction):
        if direction in ['NORTH', 'N'] and room.n_to:
            self.room = room.n_to
            print(f'You move north into the {self.room.name}.')
        elif direction in ['SOUTH', 'S'] and room.s_to:
            self.room = room.s_to
            print(f'You move south into the {self.room.name}.')
        elif direction in ['EAST', 'E'] and room.e_to:
            self.room = room.e_to
            print(f'You move east into the {self.room.name}.')
        elif direction in ['WEST', 'W'] and room.w_to:
            self.room = room.w_to
            print(f'You move west into the {self.room.name}.')
        else:
            print(f'There is nothing in that direction.')

    def pickup(self, item):
        self.inventory.append(item)

    def drop(self, item):
        del self.inventory[self.inventory.index(item)]

    def check_inventory(self):
        if len(self.inventory) == 0:
            print(f'There are no items in your inventory.')
        else:
            print(f'Your inventory contains the following: \n')
            for item in self.inventory:
                print(item.name + '\n')

    def equip(self, item):
        # put item in equipment and remove from inventory
        if item.equippable == True:
            self.equipment.append(item)
            del self.inventory[self.inventory.index(item)]
        else:
            print(f"\n You cannot equip {item}.")

    def unequip(self, item):
        # remove from equipment and put into inventory
        self.inventory.append(item)
        del self.equipment[self.equipment.index(item)]

    def look(self, room):
        if len(room.items) == 0:
            print("====================\nYou don't see anything useful here.\n====================")
        elif len(room.items) > 0:
            print(f'====================\nYou notice the following:\n')
            for i in room.items:
                print(i.name + ': ' + i.description + '\n')
            print('====================')

    def wallet(self):
        print(f"\n You currently have {self.coin} coins.")

