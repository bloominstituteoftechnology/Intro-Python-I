# Write a class to hold player information, e.g. what room they are in
# currently.

"""Return a player object

Player holds player name, room and direction information and movement
methods.
"""
import os
from colorama import Fore
from colorama import Style


class Player:
    # Initialize the properties of the class
    def __init__(self):
        self.game_over = False
        self.room = None
        self.name = None
        self.job = None
        self.sex = 'Male'
        self.direction = 'north'
        self.inventory = []
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.mp = 100
        self.max_mp = 100
        self.weapon = {}
        self.armour = {}
        self.shield = {}
        self.gold = 1000

    # Return a formatted value of the Player class
    def __str__(self):
        return f"Name: {self.name}, Room: {self.room}"

    # Displays the player information onto the screen
    def player_info(self):
        # Inventory Formatting
        os.system('clear')
        info = (f'  NAME: {Fore.GREEN}{self.name}{Style.RESET_ALL} <[{Fore.CYAN}{self.level}{Style.RESET_ALL}]> '
                f'[{self.job.name} - {self.sex}]\n'
                f'   WEAP: {self.weapon.name}\n'
                '   ARMR: Blessed Breast Plate\n'
                '   SHLD: Empty Slot\n'
                f'    VIT: {self.job.vitality}\n'
                f'    INT: {self.job.intelligence}\n'
                f'    DEX: {self.job.dexterity}\n'
                f'    WIS: {self.job.wisdom}\n\n'
                f'  HP {Fore.GREEN}{self.hp}{Style.RESET_ALL}/{Fore.GREEN}{self.max_hp}{Style.RESET_ALL}   '
                f'ATK: {self.job.attack + self.weapon.attack}   MP: <{Fore.CYAN}{self.mp}{Style.RESET_ALL}/{Fore.CYAN}'
                f'{self.max_mp}{Style.RESET_ALL}>   GOLD: {Fore.YELLOW}{self.gold}{Style.RESET_ALL}\n'
                f'  +----------------------------------------------------------------------+\n'
                f'  | INVENTORY:                                                           |\n'
                f'  +----------------------------------------------------------------------+')

        print('')
        print(info)

        if len(self.inventory) < 1:
            print("    No items in inventory")
            print('  +----------------------------------------------------------------------+\n')
            return
        count = 0
        for item in self.inventory:
            count += 1
            print(f'     [{Fore.GREEN}{count}{Style.RESET_ALL}] {item.name} - {item.description}')
        print('  +----------------------------------------------------------------------+\n')

    # Add an item to the inventory
    def pickup_item(self, item):
        if self.room.contains(item):
            print(f'\n{Fore.GREEN}{item.name}{Style.RESET_ALL} Picked up.')
            self.inventory.append(item)
            self.room.remove_item(item)
        else:
            print(f'\n{item.name} not found.')

    # Drop an item from inventory to the current room
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

    def equip_weapon(self, weapon):
        print('equip')
        if weapon in self.inventory and weapon.is_weapon:
            print('equipping')
            self.weapon = weapon
            self.inventory.remove(weapon)
            print('equipped')
        else:
            print('Weapon not in inventory')

    # Look around the current room
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
