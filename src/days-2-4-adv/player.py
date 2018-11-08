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
from item import Treasure, Weapon, Shield, Armour, Item, Lightsource

# TODO: Refactore os.system('clear') to be better implemented - maybe with a DRAW GUI function

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
        self.lightsource = {}
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
                f'   WEAP: {self.weapon.name} - {self.weapon.description}\n'
                f'   ARMR: {self.armour.name} - {self.armour.description}\n'
                f'   SHLD: {self.shield.name} - {self.shield.description}\n'
                f'   LHTS: {self.lightsource.name} - {self.lightsource.description}\n'
                f'    VIT: [{self.job.vitality}] + {vita}\n'
                f'    INT: [{self.job.dexterity}] + {dext}\n'
                f'    DEX: [{self.job.intelligence}] + {inte}\n'
                f'    WIS: [{self.job.wisdom}] + {wisd}\n\n'
                f'    HP {Fore.GREEN}{self.hp}{Style.RESET_ALL}/{Fore.GREEN}{max_hp}{Style.RESET_ALL}   '
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
        os.system('clear')
        if self.room.is_light is False or self.lightsource == items['EmptyL']:
            print('\n Good luck finding that item in the dark!')

        if self.room.contains(item):
            print(f'\n {Fore.GREEN}{item.name}{Style.RESET_ALL} picked up.')
            self.inventory.append(item)
            self.room.remove_item(item)

            if isinstance(item, Treasure):
                print('is treasure')
                if item.is_taken() is False:
                    self.gold += item.gold

                item.on_take()
        else:
            print(f'\n {item.name} not found.')

    # Drop an item from inventory to the current room
    def drop_item(self, item):
        os.system('clear')
        bl = False
        for itm in self.inventory:
            if itm == item:
                bl = True
                if isinstance(item, Lightsource):
                    item.on_drop()

                self.inventory.remove(item)
                self.room.add_item(item)
                print(f'\n {Fore.GREEN}{item.name}{Style.RESET_ALL} {Fore.RED}has been dropped{Style.RESET_ALL}')

        if bl is False:
            print(f'\n {Fore.GREEN}{item.name}{Style.RESET_ALL} {Fore.RED}is not in the inventory{Style.RESET_ALL}')

    # Equip the weapon
    def equip_weapon(self, target):
        os.system('clear')
        if target in self.inventory:

            # Checks if we don't have any other weapon equipped, if we do,
            # go ahead and swap the weapons out, bringing the already equipped to the
            # inventory
            if isinstance(target, Weapon):
                if self.weapon == items['EmptyW']:
                    self.weapon = target
                    self.inventory.remove(target)
                else:
                    self.inventory.append(self.weapon)
                    self.inventory.remove(target)
                    self.weapon = target
            elif isinstance(target, Lightsource):
                if self.lightsource == items['EmptyL']:
                    self.lightsource = target
                    self.inventory.remove(target)
                else:
                    self.inventory.append(self.lightsource)
                    self.inventory.remove(target)
                    self.lightsource = target

            print(f'\n {Fore.GREEN}{target.name}{Style.RESET_ALL} was equipped.')
        else:
            print(f'\n {Fore.GREEN}{target.name}{Style.RESET_ALL} not in inventory')

    # Un-equip the weapon
    def unequip_weapon(self, target):
        os.system('clear')
        if isinstance(target, Weapon):
            if target == self.weapon:
                self.weapon = items['EmptyW']
                self.inventory.append(target)
                print(f'\n {Fore.GREEN}{target.name}{Style.RESET_ALL} was un-equipped.')
        elif isinstance(target, Lightsource):
            if target == self.lightsource:
                self.lightsource = items['EmptyL']
                self.inventory.append(target)
                print(f'\n {Fore.GREEN}{target.name}{Style.RESET_ALL} was un-equipped.')
        else:
            print(f'\n {Fore.GREEN}{target.name}{Style.RESET_ALL} is not equipped')

    # Look around the current room
    def look_around(self):
        os.system('clear')
        if self.room.is_light or self.lightsource != items['EmptyL']:
            if len(self.room.inventory) < 1:
                print("\n You looked around the room, but found no items")
                return

            print(f'\n You looked around the room and found:')
            count = 0
            for item in self.room.inventory:
                count += 1
                print(f' [{Fore.GREEN}{count}{Style.RESET_ALL}] {Fore.GREEN}{item.name}{Style.RESET_ALL} - '
                      f'  {item.description}')
        else:
            print("\n It is pitch black!")

    # Handles the movement of the Player
    # Side Note: I didn't know about the attr method, this makes the
    # movement direction much much simplier
    def movedir(self, direction):
        self.direction = direction
        key = direction[0] + '_to'

        if not hasattr(self.room, key):
            # os.system('clear')
            print(f'\n {self.name} tried to move to {direction} but was blocked. Try another direction.\n')
            return self.room
        else:
            self.room = getattr(self.room, key)
