# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room, inventory=None, equipment=None):
        # initialize a player with room information, inventory, equipment, and coins
        self.room = room
        self.inventory = [] if inventory is None else inventory
        self.equipment = [] if equipment is None else equipment
        self.coin = 0

    def pickup(self, item):
        self.inventory.append(item)

    def drop(self, item):
        del self.inventory[self.inventory.index(item)]

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

    def wallet(self):
        print(f"\n You currently have {self.coin} coins.")

