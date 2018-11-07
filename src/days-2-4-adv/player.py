# Write a class to hold player information, e.g. what room they are in
# currently.

"""Return a player object

Player holds player name, room and direction information and movement
methods.
"""
from colorama import Fore
from colorama import Style


class Player:
    # Initialize the properties of the class
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.previous_room = None
        self.direction = 'north'
        self.inventory = []

    # Return a formatted value of the Player class
    def __str__(self):
        return f"Name: {self.name}, Room: {self.room}"

    def show_inventory(self):
        if len(self.inventory) < 1:
            print("\nNo items in inventory")
            return

        print(f'\n {Fore.GREEN} Inventory {Style.RESET_ALL}')
        print('+----------------------------------------------------------------------+')
        count = 0
        for item in self.inventory:
            count += 1
            print(f' [{Fore.GREEN}{count}{Style.RESET_ALL}] {item.name} - {item.description}')

    def pickup_item(self, item):
        print('pickup item')
        if self.room.contains(item):
            print(f'\n{Fore.GREEN}{item.name}{Style.RESET_ALL} Picked up.')
            self.inventory.append(item)
            self.room.remove_item(item)
        else:
            print(f'\n{item.name} not found.')

    def drop_item(self, item):
        bl = False
        for itm in self.inventory:
            if itm == item:
                bl = True
                self.inventory.remove(item)
                self.room.add_item(item)
                print(f'\n{Fore.GREEN}{item.name}{Style.RESET_ALL} {Fore.RED}has been dropped{Style.RESET_ALL}')

        if bl is False:
            print(f'\n{Fore.GREEN}{item.name}{Style.RESET_ALL} {Fore.RED}is not in the inventory{Style.RESET_ALL}')

    def look_around(self):
        if len(self.room.inventory) < 1:
            print("\n You looked around the room, but found no items")
            return

        print(f'\nYou looked around the room and found:')
        for item in self.room.inventory:
            print(f' [ ] {item.name} - {item.description}')

    # Handles the movement of the Player
    def movedir(self, direction):
        self.direction = direction
        if self.room.n_to and direction == 'north':
            self.room = self.room.n_to
        elif self.room.s_to and direction == 'south':
            self.room = self.room.s_to
        elif self.room.e_to and direction == 'east':
            self.room = self.room.e_to
        elif self.room.w_to and direction == 'west':
            self.room = self.room.w_to
        else:
            print(f'\n{self.name} tried to move to {direction} but was blocked. Try another direction.\n')
