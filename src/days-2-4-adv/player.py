# Write a class to hold player information, e.g. what room they are in
# currently.

"""Return a player object

Player holds player name, room and direction information and movement
methods.
"""
import os
from colorama import Fore
from colorama import Style
from items import items


class Player:
    # Initialize the properties of the class
    def __init__(self, name=None, job=None, sex="Male", room=None,):
        self.game_over = False
        self.room = room
        self.name = name
        self.job = job
        self.sex = sex
        self.weapon = {}
        self.armour = {}
        self.shield = {}
        self.direction = 'north'
        self.inventory = []
        self.level = 1
        self.exp = 0
        self.next_exp = 100
        self.hp = 100
        self.max_hp = 100
        self.mp = 100
        self.max_mp = 100
        self.gold = 1000

    # Return a formatted value of the Player class
    def __str__(self):
        return f"Name: {self.name}, Room: {self.room}"

    # Displays the player information onto the screen
    def player_info(self):
        # Inventory Formatting
        vita = self.weapon.vit + self.shield.vit + self.armour.vit
        dext = self.weapon.dex + self.shield.dex + self.armour.dex
        inte = self.weapon.int + self.shield.int + self.armour.int
        wisd = self.weapon.wis + self.shield.wis + self.armour.wis
        atk = self.weapon.attack + self.shield.attack + self.armour.attack
        max_hp = self.hp + self.weapon.hp + self.shield.hp + self.armour.hp
        max_mp = self.mp + self.weapon.mp + self.shield.mp + self.armour.mp

        os.system('clear')
        info = (f'  NAME: {Fore.GREEN}{self.name}{Style.RESET_ALL} <[{Fore.CYAN}{self.level}{Style.RESET_ALL}]> '
                f'[{self.job.name} - {self.sex}] - [{self.room.name}]\n'
                f'   WEAP: {self.weapon.name} - {self.armour.description}\n'
                f'   ARMR: {self.armour.name} - {self.armour.description}\n'
                f'   SHLD: {self.shield.name} - {self.shield.description}\n'
                f'    VIT: [{self.job.vitality}] + {vita}\n'
                f'    INT: [{self.job.dexterity}] + {dext}\n'
                f'    DEX: [{self.job.intelligence}] + {inte}\n'
                f'    WIS: [{self.job.wisdom}] + {wisd}\n\n'
                f'  HP {Fore.GREEN}{self.hp}{Style.RESET_ALL}/{Fore.GREEN}{max_hp}{Style.RESET_ALL}   '
                f'ATK: {Fore.LIGHTRED_EX}[{self.job.attack}] + {atk}{Style.RESET_ALL}   MP: {Fore.CYAN}'
                f'{self.mp}{Style.RESET_ALL}/{Fore.CYAN}{max_mp}{Style.RESET_ALL}   EXP: <{Fore.LIGHTRED_EX}'
                f'{self.exp}{Style.RESET_ALL}/{Fore.LIGHTRED_EX}{self.next_exp}{Style.RESET_ALL}>   GOLD: {Fore.YELLOW}'
                f'{self.gold}{Style.RESET_ALL}\n'
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

    # Equip the weapon
    def equip_weapon(self, weapon):
        if weapon in self.inventory:

            # Checks if we don't have any other weapon equipped, if we do,
            # go ahead and swap the weapons out, bringing the already equipped to the
            # inventory
            if self.weapon == items['EmptyW']:
                self.weapon = weapon
                self.inventory.remove(weapon)
            else:
                self.inventory.append(self.weapon)
                self.inventory.remove(weapon)
                self.weapon = weapon

            print(f'\n{Fore.GREEN}{weapon.name}{Style.RESET_ALL} was equipped.')
        else:
            print(f'{Fore.GREEN}{weapon.name}{Style.RESET_ALL} not in inventory or is not a weapon')

    # Un-equip the weapon
    def unequip_weapon(self, weapon):
        if weapon == self.weapon:
            print(f'\n{Fore.GREEN}{weapon.name}{Style.RESET_ALL} was un-equipped.')
            self.weapon = items['EmptyW']
            self.inventory.append(weapon)
        else:
            print(f'{Fore.GREEN}{weapon.name}{Style.RESET_ALL} not in inventory or is not a weapon')

    # Look around the current room
    def look_around(self):
        if len(self.room.inventory) < 1:
            print("\n You looked around the room, but found no items")
            return

        count = 0
        print(f'\nYou looked around the room and found:')
        for item in self.room.inventory:
            count += 1
            print(f' [{Fore.GREEN}{count}{Style.RESET_ALL}] {Fore.GREEN}{item.name}{Style.RESET_ALL} - '
                  f'{item.description}')

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
